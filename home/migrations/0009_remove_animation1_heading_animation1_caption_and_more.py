# Generated by Django 4.2.7 on 2023-11-29 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_animation1_score_remove_quize_quize_quize_minigames_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animation1',
            name='heading',
        ),
        migrations.AddField(
            model_name='animation1',
            name='caption',
            field=models.CharField(default='caption', max_length=100),
        ),
        migrations.AlterField(
            model_name='animation1',
            name='video1',
            field=models.FileField(null=True, upload_to='video1/%y'),
        ),
    ]
