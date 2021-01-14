# Generated by Django 3.1.5 on 2021-01-14 16:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receitas',
            fields=[
                ('id_receita', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=60)),
                ('autor', models.CharField(max_length=60)),
                ('ingredientes', models.CharField(max_length=255)),
                ('modo', models.CharField(max_length=255)),
                ('tempo', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
