from django.db import models
from rest_framework import serializers
from django.dispatch import receiver
import os
class Author(models.Model):
    name = models.CharField(max_length=20)
    codename = models.CharField(max_length=7)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile/')
    bio = models.TextField()

    def __str__(self):
        return '{}:({})'.format(self.name,self.codename)


class Video(models.Model):
    """Model definition for Video."""

    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    image = models.ImageField(upload_to='images/')
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='comments',null=True)
    class Meta:
        """Meta definition for Video."""

        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.title

class Course(models.Model):
    """Model definition for Course."""
    slug =  models.SlugField(unique=True)
    title = models.CharField(max_length=30)
    desc = models.TextField()
    video = models.ManyToManyField(Video)
    image = models.ImageField(upload_to='images/')
    paid = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Course."""
        ordering = ['timestamp']
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title

    def _isPaid(self):
        return self.paid
    
    def _courseUrl(self):
        return reverse("core:course", kwargs={
            'slug': self.slug
        })

class Comment(models.Model):
    video = models.ForeignKey(Video,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=15,null=True,blank=True)
    comment = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
    def __str__(self):
        return 'Comment by {} : {}'.format(self.name, self.comment)

@receiver(models.signals.post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes video and image from filesystem
    when corresponding `Video` object is deleted.
    """
    if instance.video:
        if os.path.isfile(instance.video.path):
            os.remove(instance.video.path)

    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)