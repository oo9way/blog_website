from typing import Iterable
from django.db import models
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
import requests


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
    

class Resume(models.Model):
    body = RichTextField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.body[:100]
    

    def clean(self):
        if self.is_active and Resume.objects.filter(is_active=True).exclude(id=self.pk).exists():
            raise ValidationError(
                {"is_active": "Sizda allaqachon aktiv rezyume mavjud"}
            )
        
class Message(models.Model):
    phone = models.CharField(max_length=255)
    text = models.TextField()

    def save(self, *args, **kwargs):
        token = ":"
        chat_id = None
        text = "Website orqali xabar \n\n"
        text += f"Telefon raqam: {self.phone}\n"
        text += f"Xabar: {self.text}"

        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
        requests.get(url)

        return super().save(*args, **kwargs)