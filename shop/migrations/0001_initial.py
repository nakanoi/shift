# Generated by Django 3.2.5 on 2021-07-31 13:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200, verbose_name='shopname')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='email')),
                ('tel', models.CharField(max_length=30, verbose_name='tel')),
            ],
        ),
    ]
