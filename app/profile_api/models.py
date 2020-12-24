from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    '''Manages user accounts'''

    def create_user(self, email, firstname, lastname, password):
        '''creates a simple user account'''
        if not email:
            raise ValueError('Email must be set!')
        email   = self.normalize_email(email)

        user    = self.model(email=email, firstname=firstname, lastname=lastname)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, firstname, lastname, password):
        '''creates an admin account'''
        user    = self.create_user(email, firstname, lastname, password)
        user.is_superuser = True
        user.is_staff     = True
        user.save()

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''user profile in database'''

    email       = models.EmailField(max_length=255, unique=True)
    firstname   = models.CharField(max_length=50)
    lastname    = models.CharField(max_length=50)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)

    objects     = UserProfileManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    def get_shortname(self):
        '''shows first name of user'''
        return self.firstname

    def get_fullname(self):
        '''shows fullname of user'''
        return f'{self.firstname} {self.lastname}'

    def __str__(self):
        '''shows user's email for representation'''
        return self.email
