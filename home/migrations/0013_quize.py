# Generated by Django 4.2.7 on 2023-12-02 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_delete_quize'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_name', models.CharField(max_length=120)),
                ('topic', models.CharField(max_length=120)),
                ('number_of_questions', models.IntegerField()),
                ('time', models.IntegerField(help_text='duration of the quiz in minutes')),
                ('required_score_to_pass', models.IntegerField(help_text='required score in %')),
                ('difficulty', models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], max_length=6)),
            ],
        ),
    ]
