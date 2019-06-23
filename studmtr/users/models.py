from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.urls import reverse



class Profile(models.Model):

	year_choices = (
		('First','First'),
		('Second','Second'),
		('Third','Third'),
		('Fourth','Fourth')
		)
	branch_choices = (
		(' Civil Engineering',' Civil Engineering'),
		('Mechanical Engineering','Mechanical Engineering'),
		('Electrical & Electronics Engineering','Electrical & Electronics Engineering'),
		(' Electronics & Communication Engineering',' Electronics & Communication Engineering'),
		('Industrial & Production Engineering ','Industrial & Production Engineering'),
		(' Computer Science & Engineering',' Computer Science & Engineering'),
		('Information Science & Engineering','Information Science & Engineering')
		)
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	image = models.ImageField(default = 'default.jpg',upload_to = 'profile_pics')
	year = models.CharField(max_length = 8,choices = year_choices,default = 'First')
	branch = models.CharField(max_length = 60,choices = branch_choices)
	bio = models.TextField(blank = True)
	mobile = models.CharField(max_length = 15,blank = True)
	
	def __str__(self):
		return f'{self.user.username}  Profile'  

	def save(self, **kwargs):
		super().save()

		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)

