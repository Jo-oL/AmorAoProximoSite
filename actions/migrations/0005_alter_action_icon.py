# Generated by Django 3.2.5 on 2021-09-10 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0004_auto_20210801_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='icon',
            field=models.CharField(choices=[('ball.png', 'bola'), ('books.png', 'livros'), ('food.png', 'comida'), ('gift.png', 'presente'), ('hat.png', 'chapéu'), ('music.png', 'notas musicais'), ('abc.png', 'quador com ABC'), ('art.png', 'tinta e pincel'), ('ballet.png', 'sapatilha de ballet'), ('berimbau.png', 'berimbau'), ('dance.png', 'pessoas dançando'), ('football_shoes.png', 'chuteira'), ('kimono.png', 'faixa de jiu-jitsu'), ('love.png', 'amor ao próximo'), ('math.png', 'matemática'), ('movie.png', 'plaqueta de filme'), ('plate.png', 'prato com garfo e faca'), ('theatre.png', 'teatro'), ('veggies.png', 'vegetais')], default='love.png', max_length=30),
        ),
    ]
