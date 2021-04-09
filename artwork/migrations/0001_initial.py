# Generated by Django 3.1.7 on 2021-04-06 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350)),
                ('description', models.TextField(blank=True)),
                ('canvas_dimension', models.CharField(max_length=30)),
                ('canvas_type', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price_discounted', models.DecimalField(decimal_places=2, max_digits=6)),
                ('review', models.TextField(blank=True)),
                ('image', models.URLField(max_length=1500)),
                ('medium', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='artwork.medium')),
            ],
        ),
    ]