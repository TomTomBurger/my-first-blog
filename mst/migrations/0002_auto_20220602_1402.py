# Generated by Django 3.2.13 on 2022-06-02 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mst', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('code', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='グループ名')),
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='cd',
        ),
        migrations.RemoveField(
            model_name='member',
            name='name',
        ),
        migrations.AddField(
            model_name='member',
            name='full_name',
            field=models.CharField(default='', max_length=150, verbose_name='名前'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='auth',
            field=models.BooleanField(default=False, verbose_name='権限A'),
        ),
        migrations.AddField(
            model_name='member',
            name='group',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mst.group'),
            preserve_default=False,
        ),
    ]
