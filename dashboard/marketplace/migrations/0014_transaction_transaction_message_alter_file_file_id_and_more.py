# Generated by Django 4.1.3 on 2023-10-01 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0013_alter_file_file_id_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_message',
            field=models.CharField(default='', max_length=25, verbose_name='Transaction message'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_id',
            field=models.CharField(default='ebbcfa8de3', max_length=10, primary_key=True, serialize=False, verbose_name='File ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('canceled', 'Canceled'), ('confirmed', 'Confirmed'), ('in_process', 'In process')], max_length=10, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_status',
            field=models.CharField(choices=[('canceled', 'Canceled'), ('confirmed', 'Confirmed'), ('in_process', 'In process')], default='In process', max_length=10, verbose_name='Status'),
        ),
    ]
