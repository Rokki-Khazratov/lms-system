# Generated by Django 5.0.2 on 2024-05-01 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='teacher_images/')),
                ('is_tutor', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('language', models.IntegerField(choices=[(1, 'Uzbek'), (2, 'Russian'), (3, 'English')])),
                ('group_type', models.IntegerField(choices=[(1, 'Zaochniy'), (2, 'Ochniy')])),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=55)),
                ('phone_number', models.CharField(max_length=55)),
                ('pasport_id', models.CharField(max_length=255)),
                ('balance', models.IntegerField()),
                ('deboting', models.BooleanField()),
                ('group', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='student.group')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='student.user')),
            ],
        ),
    ]
