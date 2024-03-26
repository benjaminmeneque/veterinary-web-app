# Generated by Django 5.0.3 on 2024-03-26 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_veterinaryinstance_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veterinaryinstance',
            name='status',
            field=models.CharField(choices=[('Pending', 'pending'), ('Approved', 'approved'), ('Declined', 'declined')], default='Pending', max_length=10),
        ),
    ]
