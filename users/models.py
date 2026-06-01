from django.db import models
from django.contrib.auth.models import AbstractUser


# AbstractUser: add/modify any fields
#AbstractBaseUser: we use this if we want to full control over oyr user model
#BaseUserManager: Employee.objacts = Manager => he is the one who carries out all of the actions on model

class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
    

