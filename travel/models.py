from django.db import models

class Destination(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	image = models.ImageField(upload_to='pics')
	desc = models.CharField(max_length=255)
	price = models.IntegerField('price')
	offer = models.BooleanField('offer', default=False)