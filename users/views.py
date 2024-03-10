from django.http import JsonResponse
from .model import User
import random

def users_api(request):
    # Obtener todos los usuarios desde la base de datos
    users = User.objects.all()
    
    # Formatear los datos de los usuarios en el formato deseado
    formatted_users = []
    for user in users:
        formatted_user = {
            'nombre': user.name,
            'edad': user.age
        }
        formatted_users.append(formatted_user)
    
    # Devolver la respuesta JSON
    return JsonResponse(formatted_users, safe=False)

def fill_table(request):
    # Función para generar un nombre aleatorio
    def generar_nombre():
        nombres = ['Juan', 'Maria', 'Pedro', 'Ana', 'Luis', 'Sofia', 'Diego', 'Laura', 'Carlos', 'Miguel']
        return random.choice(nombres)

    # Función para generar una edad aleatoria entre 18 y 70 años
    def generar_edad():
        return random.randint(18, 70)

    # Insertar 10,000 usuarios en la base de datos
    for _ in range(100000):
        nombre = generar_nombre()
        edad = generar_edad()
        User.objects.create(name=nombre, age=edad)

    response = {
        'message': 'Se han insertado 100000 usuarios en la base de datos.'
    }
    return JsonResponse(response)
