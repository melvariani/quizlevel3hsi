# Generated by Django 4.0.3 on 2022-04-09 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PesertaHSI', '0006_alter_soal_peserta_soal_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='soal_peserta',
            name='kunci',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='soal_peserta',
            name='option_four',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='soal_peserta',
            name='option_one',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='soal_peserta',
            name='option_three',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='soal_peserta',
            name='option_two',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='soal_peserta',
            name='Choice',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='soal_peserta',
            name='Soal_ID',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
