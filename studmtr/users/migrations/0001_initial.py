# Generated by Django 2.1.1 on 2018-11-08 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('year', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth')], default='First', max_length=8)),
                ('branch', models.CharField(choices=[(' Civil Engineering', ' Civil Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Electrical & Electronics Engineering', 'Electrical & Electronics Engineering'), (' Electronics & Communication Engineering', ' Electronics & Communication Engineering'), ('Industrial & Production Engineering ', 'Industrial & Production Engineering'), (' Computer Science & Engineering', ' Computer Science & Engineering'), ('Information Science & Engineering', 'Information Science & Engineering')], max_length=60)),
                ('bio', models.TextField(blank=True)),
                ('mobile', models.CharField(blank=True, max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
