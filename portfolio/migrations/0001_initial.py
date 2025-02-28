# Generated by Django 4.2.11 on 2024-09-07 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(upload_to='profile')),
                ('bio', models.TextField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('link', models.URLField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.TextField()),
                ('activities', models.TextField()),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portfolio.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github', models.URLField()),
                ('linkedin', models.URLField()),
                ('facebook', models.URLField()),
                ('instagram', models.URLField()),
                ('spotify', models.URLField()),
                ('discord', models.CharField(max_length=11)),
                ('website', models.URLField()),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portfolio.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=255)),
                ('college', models.CharField(max_length=255)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('score', models.CharField(choices=[('PERCENTAGE', 'Percentage'), ('GPA', 'GPA')], max_length=100)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.profile')),
            ],
        ),
    ]
