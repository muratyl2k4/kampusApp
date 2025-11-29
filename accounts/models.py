from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class KampusUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, Username, StudentID, Role='Student', password=None, **extra_fields):
        if not Username:
            raise ValueError("Username must be set")
        user = self.model(Username=Username, StudentID=StudentID, Role=Role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, Username, StudentID, Role='Admin', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(Username, StudentID, Role, password, **extra_fields)

def user_profile_picture_path(instance, filename):
    
    return f"profile_pictures/user_{instance.id}/{filename}"

class KampusUser(AbstractUser):

    class Meta: 
        ordering = ['Username']
    username = None
    Username = models.CharField(max_length=20, unique=True , blank= False)
    StudentID = models.CharField(max_length=50,unique=True , blank = False)
    Profile_Picture = models.ImageField(upload_to=user_profile_picture_path,  blank=True)
    Phone_Number = models.CharField(max_length=20 , blank=True)
    Faculty = models.CharField(blank=True)
    Department = models.CharField(blank=True)

    ##IF USER IS COMM_AGENT
    ##Community = models.OneToOneRelationship....

    
    rolelist = (
        ('Admin' , 'Admin'),
        ('Student' , 'Student'),
        ('comm_agent' , 'comm_agent'),

    )

    Role = models.CharField(choices=rolelist, default='Student' ,blank=False)

    USERNAME_FIELD = 'Username'
    REQUIRED_FIELDS = ['StudentID' , 'Role']

    objects = KampusUserManager()
    @property
    def is_student(self):

        return self.Role == 'Student' 
    
    @property
    def is_admin(self):
        return self.Role == 'Admin' 
    
    @property
    def is_comm_agent(self):
        return self.Role == 'comm_agent' 
    
    def __str__(self):
        return self.Username
    

from django.contrib.auth.models import BaseUserManager

