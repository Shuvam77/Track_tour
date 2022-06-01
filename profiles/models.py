from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    """
    Our UserProfile model extends the build-in Django User Model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    address = models.CharField(verbose_name="Address", max_length=100, null=True)
    town = models.CharField(verbose_name="Town/City", max_length=100, null=True)
    county = models.CharField(verbose_name="County", max_length=100, null=True)
    post_code = models.CharField(verbose_name="Post_Code", max_length=8, null=True)
    country = models.CharField(verbose_name="Country", max_length=100, null=True)
    Longtitude = models.CharField(verbose_name="Longtitude", max_length=50, null=True)
    latitude = models.CharField(verbose_name="Latitude", max_length=50, null=True)

    captcha_score = models.FloatField(default=0.0)
    has_profile = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)


    def __str__(self) -> str:
        return f"{self.user}"

