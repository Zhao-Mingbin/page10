# Generated by Django 2.0.4 on 2020-03-09 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_members_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linktab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('mail', models.CharField(max_length=100, verbose_name='邮箱')),
                ('message', models.CharField(max_length=1000, verbose_name='信息')),
            ],
            options={
                'verbose_name': '联系方式',
                'verbose_name_plural': '联系方式',
                'db_table': 'Linktab',
            },
        ),
    ]
