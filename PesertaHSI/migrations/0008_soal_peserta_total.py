# Generated by Django 4.0.3 on 2022-04-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PesertaHSI', '0007_soal_peserta_kunci_soal_peserta_option_four_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='soal_peserta',
            name='Total',
            field=models.IntegerField(null=True),
        ),
    ]