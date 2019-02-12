from django.db import models
from django.urls import reverse

class Page(models.Model):

	title = models.CharField(max_length = 30)
	content = models.TextField()
	last_update = models.DateTimeField()
		
	def get_absolute_url(self):
		
		return reverse("page-detail", args = [self.id])
		# return render(request, "list.html", context)
		# return ("Title: %s\n Description: %s\n Last update: %s\n" % (self.title, self.Description, self.last_update))
		

		
		