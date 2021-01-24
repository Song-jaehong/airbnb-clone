# Generated by Django 2.2.5 on 2021-01-24 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20210125_0039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenity',
            options={'verbose_name_plural': '편의시설'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'verbose_name_plural': '일반시설'},
        ),
        migrations.AlterModelOptions(
            name='houserule',
            options={'verbose_name_plural': '규칙관리'},
        ),
        migrations.AlterModelOptions(
            name='roomtype',
            options={'verbose_name_plural': '방유형'},
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('caption', models.CharField(max_length=80)),
                ('file', models.ImageField(upload_to='')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.Room')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]