# Generated by Django 4.0.1 on 2023-04-19 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_shop_shopitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('text', models.TextField()),
            ],
        ),
    ]