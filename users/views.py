from django.http import JsonResponse, HttpResponseBadRequest
from .models import User
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from faker import Faker
import json

fake = Faker()

def users_api(request):
    users = User.objects.values('name', 'age')
    return JsonResponse(list(users), safe=False)

@csrf_exempt
@require_POST
def fill_table(request):
    try:
        data = json.loads(request.body)
        num_entries = data['num_entries']
    except (KeyError, json.JSONDecodeError):
        return HttpResponseBadRequest('Invalid request body')
    
    User.objects.all().delete()  # Truncate the table

    users = (User(name=fake.name(), age=fake.random_int(min=18, max=70)) for _ in range(int(num_entries)))
    User.objects.bulk_create(users)

    num_inserted_users = User.objects.count()

    response = {
        'message': f'Se han insertado {num_inserted_users} usuarios en la base de datos.'
    }
    return JsonResponse(response)