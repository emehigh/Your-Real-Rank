# Generated by Django 3.0.4 on 2020-05-27 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('division', models.CharField(blank=True, default='Unranked', max_length=12)),
                ('division_img', models.ImageField(default='UNRANKED.png', upload_to='division_imgs')),
                ('profile_img', models.ImageField(default='noob.png', upload_to='profile_imgs')),
                ('stripe_id', models.CharField(blank=True, max_length=200, null=True)),
                ('product', models.ManyToManyField(blank=True, to='products.Product')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
