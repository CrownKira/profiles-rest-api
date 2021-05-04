from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

# Create your models here.
# this means that this class extends BaseUserManager
# so django knows how to work with the model
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        # print('name:', name)
        # print('email:', email)
        # password is optional field here, if none then none
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")

        # make use of parent method, this.method
        email = self.normalize_email(email)
        # create a user model
        # set to the model that the manager is for
        # model method creates a model object for you
        user = self.model(email=email, name=name)

        # convert password to hash
        # set password of the user
        # dont do this: user.password = password
        user.set_password(password)
        # specify the db that we are using
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        # self is auto passed in
        user = self.create_user(email, name, password)
        # is_superuser is auto created by the PermissionsMixin
        # ie. already in parent class of userProfile (from what it inherits)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# custom user model
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # determine if user is active
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    # instance method, need self
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""

    # on delete, delete all the items!!
    # user_profile is not editable
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text
