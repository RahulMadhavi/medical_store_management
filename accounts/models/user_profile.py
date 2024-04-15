from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    class UserRoles(models.TextChoicesModel):
        ADMIN = 'admin', ('Admin')
        OWNER = 'owner', ('Owner')
        VIEWONLY = 'view_only', ('View Only')
        SUPERUSER = 'superuser', ('Super User')
        STAFFUSER = 'staff', ('Staff User')
        QAUSER = 'qauser', ('QA User')
        BOTUSER = 'botuser', ('Bot User')

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile')
    role = models.CharField(max_length=20, choices=UserRoles)
