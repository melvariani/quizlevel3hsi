# Generated by Django 4.0.3 on 2022-03-29 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminHSI', '0003_alter_soal_option_five_alter_soal_option_four'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soal',
            name='option_five',
        ),
    ]