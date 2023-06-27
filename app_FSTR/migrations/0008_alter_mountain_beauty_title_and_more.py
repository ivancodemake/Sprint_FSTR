# Generated by Django 4.2.2 on 2023-06-25 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_FSTR', '0007_alter_mountain_beauty_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mountain',
            name='beauty_title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='mountain',
            name='coordinates',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_FSTR.coordinates'),
        ),
        migrations.AlterField(
            model_name='mountain',
            name='levels',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_FSTR.level'),
        ),
        migrations.AlterField(
            model_name='mountain',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_FSTR.user'),
        ),
    ]
