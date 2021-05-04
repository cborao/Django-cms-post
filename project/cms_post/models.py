from django.db import models


# Create your models here.
class Content(models.Model):
    key = models.CharField(max_length=64)
    value = models.TextField()

    def __str__(self):
        return self.key + ": " + self.value


class Comment(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=False)
    date = models.DateTimeField('published')

    def __str__(self):
        return self.content.key + ": " + self.title
