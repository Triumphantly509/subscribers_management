from django.db import models

# Create your models here.

class subscribers(models.Model):
    email = models.EmailField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.BooleanField(default=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class MailMessage(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title
