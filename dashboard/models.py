from django.db import models

class Configuration(models.Model):
    zenoss_instance = models.CharField(max_length=60)
    zenoss_username = models.CharField(max_length=30)
    zenoss_password = models.CharField(max_length=60)
    show_acknowledged = models.NullBooleanField()

