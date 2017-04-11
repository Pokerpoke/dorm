from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class Dorm(models.Model):
    """
    Device status database.
    """
    devID = models.PositiveIntegerField(null=True)
    devName = models.CharField(max_length=4, null=True)
    devStatus = models.PositiveIntegerField(null=True)
    roomName = models.PositiveIntegerField(null=True)
    nRelays = models.PositiveIntegerField(null=True)
    relay = models.CharField(max_length=30, null=True)
    # time = models.DateTimeField(default=timezone.now)
    time = models.DateTimeField(auto_now=True, null=True)

    def get_router(self):
        """
        Get router.
        """
        if self.nRelays == 1:
            pass


# class User(models.Model):
#     """
#     User and password database.
#     """
#     username = models.CharField(max_length=100, unique=True)
#     password = models.CharField(max_length=100)
#     roomname = models.PositiveIntegerField(null=True)
