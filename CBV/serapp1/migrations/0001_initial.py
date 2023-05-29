# Generated by Django 4.0.4 on 2023-05-28 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='书籍名称')),
                ('price', models.IntegerField(verbose_name='价格')),
            ],
        ),
    ]
