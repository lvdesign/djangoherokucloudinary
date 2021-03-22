from django.db import models
from django.urls import reverse # new



class Upload(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/') 
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,) # manyToOne
    body= models.TextField()
    # dossier Image de cloudinary

    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('image_detail', args=[str(self.id)])
