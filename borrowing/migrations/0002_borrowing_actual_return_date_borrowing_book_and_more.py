# Generated by Django 4.0.4 on 2024-06-13 17:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0001_initial'),
        ('borrowing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowing',
            name='actual_return_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='borrowing',
            name='book',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='borrowings', to='library.book'),
        ),
        migrations.AddField(
            model_name='borrowing',
            name='borrow_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='borrowing',
            name='expected_return_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='borrowing',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='borrowings', to=settings.AUTH_USER_MODEL),
        ),
    ]
