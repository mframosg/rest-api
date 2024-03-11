from django.http import JsonResponse
from .model import User
import random

class UserFormatter:
    @staticmethod
    def format(user):
        return {
            'nombre': user.name,
            'edad': user.age
        }

class RandomUserGenerator:
    NAMES = ['Juan', 'Maria', 'Pedro', 'Ana', 'Luis', 'Sofia', 'Diego', 'Laura', 'Carlos', 'Miguel']

    @staticmethod
    def generate_name():
        return random.choice(RandomUserGenerator.NAMES)

    @staticmethod
    def generate_age():
        return random.randint(18, 70)

def users_api(request):
    users = User.objects.all()
    formatted_users = [UserFormatter.format(user) for user in users]
    return JsonResponse(formatted_users, safe=False)

def fill_table(request, num_entries):
    User.objects.all().delete()  # Truncate the table

    for _ in range(int(num_entries)):
        name = RandomUserGenerator.generate_name()
        age = RandomUserGenerator.generate_age()
        User.objects.create(name=name, age=age)

    response = {
        'message': f'Se han insertado {num_entries} usuarios en la base de datos.'
    }
    return JsonResponse(response)