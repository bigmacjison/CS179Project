# Generated by Django 2.0.4 on 2018-05-01 04:46

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=50)),
                ('pet_type', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'DOG'), (2, 'CAT'), (3, 'BIRD')], max_length=5)),
                ('pet_breed', models.CharField(max_length=20)),
                ('pet_age', models.IntegerField(default=0)),
                ('pet_gender', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'MALE'), (2, 'FEMALE')], max_length=3)),
                ('pet_description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user_email', models.EmailField(max_length=50)),
                ('user_age', models.IntegerField(default=0)),
                ('user_password', models.CharField(max_length=20)),
                ('user_gender', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'MALE'), (2, 'FEMALE')], max_length=3)),
                ('user_pitch', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AniModels.User'),
        ),
    ]
