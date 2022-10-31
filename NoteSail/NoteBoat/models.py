from django.db import models

# Create your models here.

class Documents(models.Model):
	docname = models.CharField(max_length=30)
	text = models.TextField(blank=True)
	def __str__(self):
		return f"{self.docname}"

class Userdata(models.Model):
	username = models.CharField(max_length=64)
	email = models.CharField(max_length=64)
	fname = models.CharField(max_length=24)
	security = models.CharField(max_length=16)
	rcode = models.PositiveIntegerField(blank=True)
	docs = models.ManyToManyField(Documents, blank=True, related_name="documents")
	pinned = models.CharField(max_length=30)

	def __str__(self):
		return f"Username:{self.username} First name:{self.fname} Security Answer:{self.security} Recovery Code:{self.rcode}"

class Feedback(models.Model):
	name = models.CharField(max_length=64)
	comment = models.TextField()
	datetime = models.CharField(max_length=24)

	def __str__(self):
		return f"From {self.name} at {self.datetime} -- {self.comment}"

