# Generated by Django 5.0.3 on 2024-03-28 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0002_email_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='attachment',
            field=models.FileField(blank=True, upload_to='email_attachments/'),
        ),
    ]
