# Generated by Django 4.0.3 on 2022-04-11 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='autore_post',
            new_name='author_post',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='citta',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='contenuto',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='data_creazione',
            new_name='creation_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='distanza',
            new_name='distance',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='immagine',
            new_name='image',
        ),
    ]