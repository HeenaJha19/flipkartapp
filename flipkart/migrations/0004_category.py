# Generated by Django 4.1.3 on 2022-12-03 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0003_alter_registration_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('images', models.ImageField(upload_to='upload/category/')),
            ],
        ),
    ]
