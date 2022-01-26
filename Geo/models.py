from django.db import models

# Create your models here.
class Movie(models.Model):
	movie_title = models.CharField(max_length=150)
	release_year = models.IntegerField()
	director = models.CharField(max_length=100)
	movie_poster = models.ImageField(upload_to='images/')
	movie_plot = models.TextField()
	

	def __str__(self):
		return self.movie_title