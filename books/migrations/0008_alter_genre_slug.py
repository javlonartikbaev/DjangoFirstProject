# Generated by Django 5.0.2 on 2024-02-17 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0007_genre_slug_alter_orderitems_book_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="genre",
            name="slug",
            field=models.SlugField(blank=True, default="", max_length=255),
        ),
    ]