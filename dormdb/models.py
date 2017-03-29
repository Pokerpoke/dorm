from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class Dorm(models.Model):
    devID = models.PositiveIntegerField(null=True)
    devName = models.CharField(max_length=4, null=True)
    devStatus = models.PositiveIntegerField(null=True)
    roomName = models.PositiveIntegerField(null=True)
    nRelays = models.PositiveIntegerField(null=True)
    relay1 = models.PositiveIntegerField(null=True)
    relay2 = models.PositiveIntegerField(null=True)
    relay3 = models.PositiveIntegerField(null=True)
    relay4 = models.PositiveIntegerField(null=True)
    relay5 = models.PositiveIntegerField(null=True)
    # time = models.DateTimeField(default=timezone.now)
    time = models.DateTimeField(auto_now = True)

    def getRouter(self):
        if self.nRelays == 1:
            pass