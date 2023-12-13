from django.db import models

# Create your models here.
class MovieModel(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(null=True)
  release_date = models.DateField()
  year = models.IntegerField()
  created_at =  models.DateTimeField(auto_now=True)
  
class ActorModel(models.Model):
  fname = models.CharField(max_length=200)
  lname = models.CharField(max_length=200)
  
class MovieActorModel(models.Model):
  movie_id = models.ForeignKey(MovieModel, on_delete=models.CASCADE)
  actor_id = models.ForeignKey("ActorModel", on_delete=models.CASCADE)
  