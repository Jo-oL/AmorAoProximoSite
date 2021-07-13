# Generated by Django 3.2.4 on 2021-07-13 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0002_alter_action_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='category',
            field=models.CharField(choices=[('EDU', 'Educação'), ('ESP', 'Esporte'), ('CLT', 'Cultura'), ('CNM', 'Comida na mesa')], default='EDU', max_length=3),
        ),
    ]