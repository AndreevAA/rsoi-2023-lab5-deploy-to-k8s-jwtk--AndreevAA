# Generated by Django 4.1.1 on 2022-10-31 22:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookLibraryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_count', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('condition', models.CharField(choices=[('EXCELLENT', 'Excellent'), ('GOOD', 'Good'), ('BAD', 'Bad')], default='EXCELLENT', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('library_uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('books', models.ManyToManyField(through='source.BookLibraryModel', to='source.bookmodel')),
            ],
        ),
        migrations.AddField(
            model_name='booklibrarymodel',
            name='book_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='source.bookmodel'),
        ),
        migrations.AddField(
            model_name='booklibrarymodel',
            name='library_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='library', to='source.librarymodel'),
        ),
    ]
