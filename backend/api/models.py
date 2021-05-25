from django.db import models
from django.dispatch import receiver
import os

class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

class Author(models.Model):
    name = models.CharField(max_length=20)
    codename = models.CharField(max_length=7)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile/')
    bio = models.TextField()

    def __str__(self):
        return '{}:({})'.format(self.name,self.codename)


class Video(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField()
    video = models.URLField(unique=True)
    image = models.ImageField(upload_to='images/')
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='comments',null=True)
    tag = models.ManyToManyField(Tag,related_name='videos_tag')

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.title


class Doc(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()
    draft = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag,related_name='doc_tag')

    class Meta:
        ordering=['timestamp']
        verbose_name = 'Doc'
        verbose_name_plural = 'Docs'

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()
    video = models.ManyToManyField(Video)
    image = models.ImageField(upload_to='images/')
    doc = models.OneToOneField(Doc,on_delete=models.CASCADE,default=False,null=True)
    paid = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag,related_name='course_tag')

    class Meta:
        ordering = ['timestamp']
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title
    

class Project(models.Model):
    title = models.CharField(max_length=30,blank=True,null=True)
    desc = models.TextField(blank=True,null=True)
    video = models.ManyToManyField(Video)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    doc = models.OneToOneField(Doc,on_delete=models.CASCADE,default=False,null=True)
    paid = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag,related_name='project_tag')

    class Meta:
        ordering = ['timestamp']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title


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