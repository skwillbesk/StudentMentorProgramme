from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Message(models.Model):
	 sender = models.ForeignKey(User,on_delete = models.CASCADE, related_name="sender")
	 reciever = models.ForeignKey(User,on_delete = models.CASCADE, related_name="reciever")
	 msg_content = models.TextField()
	 created_at = models.DateTimeField(default = timezone.now)

	 def __str__(self):
	 	return f'{self.sender,self.reciever} Message'


