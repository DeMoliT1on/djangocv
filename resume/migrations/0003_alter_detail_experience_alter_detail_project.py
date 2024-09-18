# Generated by Django 5.1.1 on 2024-09-18 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_remove_experience_details_remove_project_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='experience',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expirence_details', to='resume.experience'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_details', to='resume.project'),
        ),
    ]
