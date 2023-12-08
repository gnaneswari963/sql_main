# Generated by Django 4.2.7 on 2023-12-08 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salgrade',
            old_name='high_sal',
            new_name='highsal',
        ),
        migrations.RenameField(
            model_name='salgrade',
            old_name='low_sal',
            new_name='lowsal',
        ),
        migrations.AddField(
            model_name='salgrade',
            name='id',
            field=models.BigAutoField(auto_created=True, default=123, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='salgrade',
            name='grade',
            field=models.PositiveIntegerField(),
        ),
    ]
