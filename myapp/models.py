from django.db import models

# Create your models here.
class Order(models.Model):

	name = models.CharField(max_length=20)
	quantity = models.CharField(max_length=20)
	rate = models.CharField(max_length=20)
	total = models.CharField(max_length=10)

	def __str__(self):
		return self.name