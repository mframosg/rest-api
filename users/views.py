from django.http import JsonResponse, HttpResponseBadRequest
from .models import User
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from faker import Faker
import json

fake = Faker()

def users_api(request):
    gender = request.GET.get('gender', '').upper()
    age = request.GET.get('age')
    criteria = request.GET.get('criteria', 'equal')

    valid_genders = ['M', 'F']
    criteria_map = {'greater': 'gt', 'less': 'lt', 'equal': ''} 

    if gender and gender not in valid_genders:
        return HttpResponseBadRequest(f"Invalid gender, must be one of {valid_genders}")

    query = Q()
    if gender:
        query &= Q(gender=gender)

    if age:
        try:
            age = int(age)
            if not 18 <= age <= 70:
                return HttpResponseBadRequest("Age must be between 18 and 70.")
            if criteria in criteria_map:
                filter_lookup = f'age__{criteria_map[criteria]}' if criteria_map[criteria] else 'age'
                query &= Q(**{filter_lookup: age})
            else:
                return HttpResponseBadRequest("Invalid criteria provided. Must be one of ['greater', 'less', 'equal'].")
        except ValueError:
            return HttpResponseBadRequest("Invalid age provided.")

    users = User.objects.filter(query)
    users_list = list(users.values('name', 'age', 'gender'))

    return JsonResponse(users_list, safe=False)
    
@csrf_exempt
@require_POST
def fill_table(request):
    try:
        data = json.loads(request.body)
        num_entries = int(data.get('num_entries', 0))
        if num_entries <= 0:
            return HttpResponseBadRequest("Number of entries must be greater than 0.")
    except (ValueError, TypeError):
        return HttpResponseBadRequest("Invalid data provided.")
    users = []
    User.objects.all().delete()
    for _ in range(num_entries):
        gender = fake.random_element(elements=['M', 'F'])
        name = fake.name_male() if gender == 'M' else fake.name_female()
        age = fake.random_int(min=18, max=70)
        users.append(User(name=name, age=age, gender=gender))
    
    try:
        User.objects.bulk_create(users)
    except Exception as e:
        return HttpResponseBadRequest(f"Error al insertar usuarios: {str(e)}")

    response = {
        'message': f'Se han insertado {num_entries} usuarios en la base de datos.'
    }
    return JsonResponse(response)