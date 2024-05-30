from django.db import models


class Author(models.Model):
    fullname = models.CharField(unique=True, null=False)
    born_date = models.CharField(max_length=50, null=False)
    born_location = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return self.fullname


class Quote(models.Model):
    quote = models.CharField(max_length=255, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.quote
