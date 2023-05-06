from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class CustomuserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email field is required")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extrafields):
        extrafields.setdefault("is_staff", True)
        extrafields.setdefault("is_active", True)
        extrafields.setdefault("is_superuser", True)
        extrafields.setdefault("name", "admin")

        if extrafields.get("is_staff") is not True:
            raise ValueError("is_staff must be true")
        
        if extrafields.get("is_superuser") is not True:
            raise ValueError("is_superuser must be true")

        return self.create_user(email, password, **extrafields)


class Customuser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    objects = CustomuserManager()

    def __str__(self):
        return self.email

class Customuserprofile(models.Model):
    user = models.OneToOneField(Customuser, on_delete=models.CASCADE, related_name="user_profile")
    profile_pic = models.ImageField(upload_to="profile_pics")
    date = models.DateField()