import datetime
from django.db import models


class Utilisateurs(models.Model):
    code_user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    actifs = models.BooleanField()
    dateCreation = models.DateTimeField(default=datetime.datetime.now)

    @classmethod
    def create_user(cls, code_user, password, email):
        user = cls(Code_Utilisateur=code_user, Password=password, Email=email, Actifs=True, DateCreation=datetime.datetime.now())
        user.save()
        return True
    @classmethod
    def login_user(cls, code_user, password):
        try:
          user = cls.objects.get(code_user=code_user, password=password)
          if user.code_user == code_user and user.password == password:
             user_info = {
                'id': user.id,
                'code_user': user.code_user,
                'password': user.password,
                'email': user.email,
            }
             return user_info, True
          else:
            return None, False
        except cls.DoesNotExist:
          return None, False

    @classmethod
    def get_user_id(cls,id_user):
        try:
            user = cls.objects.get(id=id_user)
            if user.id == id_user:
                 user_info = {
                'id': user.id,
                'code_user': user.code_user,
                'password': user.password,
                'email': user.email,
            }
                 return user_info, True
            else:
                 return None, False
        except cls.DoesNotExist:
          return None, False

# #------------------------------------Programme-----------------------------------------------------------------------
# class programme(models.Model):
#     titre=models.CharField(max_length=150,unique=True)
#     type_admission=models.CharField(max_length=50)
#     cycle=models.IntegerField()
#     credit=models.IntegerField()
#     campus=models.CharField(max_length=150)
#     description=models.TextField(max_length=500)
#     code=models.IntegerField(unique=True)
# class Trimestre(models.Model):
#    titre = models.CharField()
#    date_Debut  = models.DateTimeField()
#    date_Fin = models.DateTimeField()
#    Programme = models.ForeignKey(programme,to_field="id")
class Programme(models.Model):
    titre = models.CharField(max_length=150, unique=True)
    type_admission = models.CharField(max_length=50)
    cycle = models.IntegerField()
    credit = models.IntegerField()
    campus = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    code = models.IntegerField(unique=True)
class Trimestre(models.Model):
    titre = models.CharField(max_length=150) 
    date_Debut = models.DateTimeField()
    date_Fin = models.DateTimeField()
    Programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    





