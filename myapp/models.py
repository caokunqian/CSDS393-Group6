from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name="user")
    nick_name = models.CharField(max_length=20,verbose_name="nick name")
    avatar = models.FileField(upload_to='avatar', default="avatar/default_avatar.png", null=True,blank=True,verbose_name="avatar")
    gender = models.PositiveSmallIntegerField(
        default=2,
        choices=((1, ("Male")), (2, ("Female"))),
        verbose_name="Gender"
    )
    signature = models.CharField(max_length=100,null=True,blank=True,verbose_name="signature")
    email = models.EmailField(max_length=50,null=True,blank=True,verbose_name="email")
    birthday = models.DateField(null=True,blank=True,verbose_name="birthday")


    class Meta:
        verbose_name = "UserInfo"
        verbose_name_plural = verbose_name
        db_table = "va_userinfo"
