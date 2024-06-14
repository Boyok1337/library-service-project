# Generated by Django 4.0.4 on 2024-06-14 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('borrowing', '0006_borrowing_expected_return_date_gte_borrow_date_and_more'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='type',
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(choices=[('PAYMENT', 'Payment'), ('FINE', 'Fine')], default='PAYMENT', max_length=7),
        ),
        migrations.AlterField(
            model_name='payment',
            name='borrowing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='borrowing.borrowing'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('PAID', 'Paid')], default='PENDING', max_length=7),
        ),
    ]
