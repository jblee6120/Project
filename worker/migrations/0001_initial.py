# Generated by Django 3.2.5 on 2021-09-08 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0002_alter_booklist_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoadBook',
            fields=[
                ('booklist_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.booklist')),
            ],
            options={
                'db_table': 'Book',
            },
            bases=('common.booklist',),
        ),
    ]
