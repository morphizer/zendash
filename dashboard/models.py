from django.db import models
from django import forms

class Configuration(models.Model):
    zenoss_instance = models.CharField(max_length=60)
    zenoss_username = models.CharField(max_length=30)
    zenoss_password = models.CharField(max_length=60)
    show_acknowledged = models.BooleanField(default=False, blank=True)

class ConfigurationForm(forms.ModelForm):
    class Meta:
        model = Configuration
        widgets = {
                'zenoss_password': forms.PasswordInput(),
        }
