from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime
from django.apps import AppConfig


class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	score=models.IntegerField(default=0)
	curr_round=models.IntegerField(default=1)
	submit_time =  models.DateTimeField(auto_now_add=True)
	phone =models.CharField(max_length=10, default="197")
	def __str__(self):
		return self.user.username


	

	
        
@receiver(post_save,sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	#response = kwargs['response']
	#backend = kwargs['backend']
	if created:
		Profile.objects.create(user=instance)
    #if created:
		#response = kwargs['response']

     #   Profile.objects.create(user=instance,image= response['picture'])

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




