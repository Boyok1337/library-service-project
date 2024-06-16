# Generated by Django 4.0.4 on 2024-06-15 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('borrowing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowing',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='borrowing',
            constraint=models.CheckConstraint(check=models.Q(('expected_return_date__gte', django.db.models.expressions.F('borrow_date'))), name='expected_return_date_gte_borrow_date'),
        ),
        migrations.AddConstraint(
            model_name='borrowing',
            constraint=models.CheckConstraint(check=models.Q(('actual_return_date__gte', django.db.models.expressions.F('borrow_date'))), name='actual_return_date_gte_borrow_date'),
        ),
    ]
