from django.contrib import admin
from jeune .models import subscribers, MailMessage

# Register your models here.
@admin.register(subscribers, MailMessage)
class AuthorAdmin(admin.ModelAdmin):
    pass
