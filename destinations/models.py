from django.db import models

class Destination(models.Model):
    place_name = models.CharField(max_length=200)
    weather = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.place_name

class DestinationImage(models.Model):
    destination = models.ForeignKey(Destination, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='destination_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return "Image for {self.destination.place_name}"