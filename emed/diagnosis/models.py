from django.db import models

class Symptom(models.Model):
	name = models.CharField(max_length=250)
	weight = models.IntegerField()

	class Meta:
		unique_together = ("name", "weight")

	def __unicode__(self):
		return self.name

class Disease(models.Model):
	name = models.CharField(max_length=250)
	symptom1 = models.ForeignKey(Symptom, related_name='Symptom 1')
	symptom2 = models.ForeignKey(Symptom, related_name='Symptom 2')
	symptom3 = models.ForeignKey(Symptom, related_name='Symptom 3')
	domain = models.CharField(max_length=250)

	class Meta:
		unique_together = ("name", "symptom3", "symptom2", "symptom1")

	def __unicode__(self):
		return self.name

class Doctor(models.Model):
	name = models.CharField(max_length=250, unique=True)
	place = models.CharField(max_length=250)
	domain = models.CharField(max_length=250)
	contact = models.TextField()

	def __unicode__(self):
		return self.name

	
	    
