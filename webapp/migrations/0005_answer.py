# Generated by Django 2.2 on 2020-08-29 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20200829_0620'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creat_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='webapp.Pol', verbose_name='Ответ')),
                ('possible_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='webapp.Choice', verbose_name='Ответ')),
            ],
        ),
    ]
