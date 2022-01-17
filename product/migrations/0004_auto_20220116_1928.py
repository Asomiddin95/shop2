# Generated by Django 3.2.9 on 2022-01-16 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20220116_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='SizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=3, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'size',
                'verbose_name_plural': 'sizes',
            },
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='razmerlar',
        ),
        migrations.DeleteModel(
            name='SizesModel',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='sizes',
            field=models.ManyToManyField(related_name='products', to='product.SizeModel'),
        ),
    ]
