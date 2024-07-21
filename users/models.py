from django.db import models

class User(models.Model):
    idusuario = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    class Meta:
        db_table = 'usuarios'
        
    def to_dict(self):
        return {
            'idusuario': self.idusuario,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
        }
        