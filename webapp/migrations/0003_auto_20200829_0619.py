# Generated by Django 2.2 on 2020-08-29 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200829_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pol',
            name='question',
            field=models.TextField(max_length=2000, verbose_name='Вопрос'),
        ),
    ]