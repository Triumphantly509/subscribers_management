# Generated by Django 4.1.7 on 2023-02-16 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeune', '0003_alter_subscribers_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('message', models.TextField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='statusDescription',
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]