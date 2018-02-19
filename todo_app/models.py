from django.db import models

class Todo_Plan(models.Model):
	plan = models.CharField(max_length=40)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return "Plan N°{}".format(self.id)