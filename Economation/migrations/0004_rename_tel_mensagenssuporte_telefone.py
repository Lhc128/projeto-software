# Generated by Django 5.1.3 on 2024-11-26 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Economation', '0003_mensagenssuporte'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensagenssuporte',
            old_name='tel',
            new_name='telefone',
        ),
    ]
