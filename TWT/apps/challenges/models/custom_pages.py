from django.db import models
from martor.models import MartorField
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class CustomPage(models.Model):

    page_id = models.AutoField(primary_key=True)
    linkName = models.CharField(max_length=200, unique=True, validators=[alphanumeric])
    page_menu_name = models.CharField(max_length=100)
    title = models.CharField(max_length=1000)
    content = MartorField()
    public = models.BooleanField(default=False)
    only_staff = models.BooleanField(default=False)
    def __str__(self):
        return self.title