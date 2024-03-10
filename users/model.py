from django.db import models

class User(models.Model):
    idusuario = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    class Meta:
        db_table = 'usuarios'
        