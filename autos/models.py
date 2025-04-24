from django.contrib.auth.password_validation import MinimumLengthValidator
from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Make(models.Model):
    name=models.CharField(
        max_length=100,
        help_text='Enter a make',
        validators=[
            MinimumLengthValidator(2,"Make name is more than 1 character")
        ]
    )
    def __str__(self):
        return self.name
class Auto(models.Model):
    nickename=models.CharField(
        max_length=200,
        validators=[
            MinimumLengthValidator(2,"auto name is more than 1 chracter")
        ]
    )
    mileage=models.PositiveIntegerField()
    comment=models.CharField(max_length=300)
    make=models.ForeignKey(Make,on_delete=models.CASCADE)

    def __str__(self):
        return self.nickename

