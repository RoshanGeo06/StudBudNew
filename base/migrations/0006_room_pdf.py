# Generated by Django 5.0.2 on 2024-02-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_room_pdf_alter_room_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
