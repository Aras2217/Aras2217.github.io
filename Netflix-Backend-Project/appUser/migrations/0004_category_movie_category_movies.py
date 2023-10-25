# Generated by Django 4.2.5 on 2023-10-22 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0003_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Kategori Başlığı')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(max_length=10, null=True)),
                ('image', models.FileField(null=True, upload_to='image', verbose_name='Resim')),
                ('category', models.ManyToManyField(blank=True, to='appUser.category', verbose_name='Kategori')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='movies',
            field=models.ManyToManyField(blank=True, related_name='categories', to='appUser.movie', verbose_name='Movies'),
        ),
    ]