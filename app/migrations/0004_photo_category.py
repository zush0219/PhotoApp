# Generated by Django 2.2.1 on 2019-05-02 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.Category'),
            preserve_default=False,
        ),
    ]
