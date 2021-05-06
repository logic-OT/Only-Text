from django.db import models

class Room_name(models.Model):
	Name = models.CharField(max_length=50,null=True)

	def __str__(self):
		return self.Name


# Create your models here
