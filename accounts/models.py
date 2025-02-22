from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, blank=True, null=True)
    password1 = models.CharField(max_length=256, blank=True, null=True)
    password2 = models.CharField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)

    # 翻訳用
    username_jp = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()



