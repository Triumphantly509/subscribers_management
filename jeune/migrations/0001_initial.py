# Generated by Django 4.1.7 on 2023-02-16 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
