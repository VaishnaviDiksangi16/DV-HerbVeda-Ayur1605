from django.db import models

class Herb(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    diseases = models.TextField()
    image = models.ImageField(upload_to="herbs/")
    model_3d_url = models.URLField()

    def __str__(self):
        return self.name