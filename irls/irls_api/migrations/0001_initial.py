# Generated by Django 4.2.5 on 2023-10-05 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200)),
                ('city', models.CharField(blank=True, default='', max_length=200)),
                ('address', models.CharField(blank=True, default='', max_length=200)),
                ('zip_code', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, default='', max_length=200)),
                ('first_name', models.CharField(blank=True, default='', max_length=200)),
                ('email_address', models.EmailField(blank=True, default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=200)),
                ('date', models.DateTimeField(blank=True)),
                ('players_number', models.IntegerField(blank=True)),
                ('sport', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='irls_api.sport')),
                ('structure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='irls_api.structure')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='irls_api.user')),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
    ]
