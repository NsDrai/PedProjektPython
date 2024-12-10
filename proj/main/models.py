from django.db import models

class Author(models.Model):

    name = models.CharField(max_length=100)
    mail = models.EmailField(primary_key=True)

class Post (models.Model):

    POST_TYPES = [('c', 'copyrighte'), ('a' , 'add')]

    def __str__(self):
        return self.mail

    title = models.CharField(max_length=100)
    content = models.TextField()
    issued = models.DateTimeField()
    post_type = models.CharField(max_length=1, choices=POST_TYPES)
    image = models.ImageField(upload_to='uploads')

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
