from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    read_min = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"
    