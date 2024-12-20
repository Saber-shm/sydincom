# Generated by Django 5.1.4 on 2024-12-17 18:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_complaint_document_expense_legalcase_owner_payment_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Propriétaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('phone_number', models.CharField(blank=True, max_length=120)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Propriéter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=120)),
                ('propriéter_type', models.CharField(choices=[('propriéter', 'Propriéter'), ('loyer', 'Loyer')], max_length=120)),
                ('description', models.TextField(blank=True)),
                ('propriétaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.propriétaire')),
            ],
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='document',
            name='residence',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='residence',
        ),
        migrations.RemoveField(
            model_name='legalcase',
            name='property',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='residence',
        ),
        migrations.RemoveField(
            model_name='property',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='property',
        ),
        migrations.RemoveField(
            model_name='property',
            name='residence',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='residence',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
        migrations.RemoveField(
            model_name='workorder',
            name='residence',
        ),
        migrations.RemoveField(
            model_name='residence',
            name='address',
        ),
        migrations.RemoveField(
            model_name='residence',
            name='description',
        ),
        migrations.AddField(
            model_name='residence',
            name='adress',
            field=models.CharField(default='none value', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='residence',
            name='balance',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='residence',
            name='name',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='propriéter',
            name='residence',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.residence'),
        ),
        migrations.DeleteModel(
            name='Complaint',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
        migrations.DeleteModel(
            name='LegalCase',
        ),
        migrations.DeleteModel(
            name='Owner',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
        migrations.DeleteModel(
            name='Reminder',
        ),
        migrations.DeleteModel(
            name='WorkOrder',
        ),
    ]
