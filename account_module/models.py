from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    image = models.ImageField(upload_to="images/profile", default="images/profile/Profile.png" ,verbose_name='تصویر پروفایل', null=True , blank=True)
    phone_number = models.CharField(max_length=200 , verbose_name='شماره تماس', null=True, blank=True)
  
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name="account_users",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name = "account_users_permissions",
        blank=True
    )



    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


    def __str__(self):
        if self.first_name != '' and self.last_name != '':
            return self.get_full_name()
        
        return self.email