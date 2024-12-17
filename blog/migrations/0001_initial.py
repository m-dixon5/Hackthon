# Generated by Django 4.2.17 on 2024-12-17 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('rock', 'Rock'), ('pop', 'Pop'), ('hip-hop', 'Hip-Hop'), ('jazz', 'Jazz'), ('classical', 'Classical'), ('electronic', 'Electronic'), ('blues', 'Blues'), ('metal', 'Metal'), ('reggae', 'Reggae'), ('folk', 'Folk'), ('punk', 'Punk'), ('indie', 'Indie'), ('rnb', 'R&B'), ('country', 'Country'), ('soul', 'Soul'), ('funk', 'Funk'), ('latin', 'Latin'), ('world', 'World Music'), ('house', 'House'), ('techno', 'Techno')], max_length=30, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.FileField(upload_to='media/blog')),
                ('slug', models.SlugField(default='')),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=30)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.category')),
            ],
        ),
    ]
