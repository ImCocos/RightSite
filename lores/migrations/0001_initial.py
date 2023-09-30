# Generated by Django 4.2.5 on 2023-09-30 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(default='Without description', max_length=250)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/abilities/')),
            ],
        ),
        migrations.CreateModel(
            name='AbilityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(default='active', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(default='Without description', max_length=250)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/categories/')),
            ],
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(default='Without description', max_length=250)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/effects/')),
            ],
        ),
        migrations.CreateModel(
            name='HeroClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(default='Without description', max_length=250)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/heroesclasses/')),
            ],
        ),
        migrations.CreateModel(
            name='ItemClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(default='Without description', max_length=250)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/itemclasses/')),
            ],
        ),
        migrations.CreateModel(
            name='Per',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(default='Without description', max_length=250)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/units/')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(default='Without description', max_length=250)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/items/')),
                ('effects', models.ManyToManyField(blank=True, to='lores.effect')),
                ('item_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lores.itemclass')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(default='Without description', max_length=250)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/heroes/')),
                ('abilities', models.ManyToManyField(blank=True, to='lores.ability')),
                ('categories', models.ManyToManyField(blank=True, to='lores.category')),
                ('items', models.ManyToManyField(blank=True, to='lores.item')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.PositiveIntegerField()),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lores.unit')),
            ],
        ),
        migrations.CreateModel(
            name='AbilityCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.PositiveIntegerField()),
                ('per', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lores.per')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lores.unit')),
            ],
        ),
        migrations.AddField(
            model_name='ability',
            name='ab_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lores.abilitytype'),
        ),
        migrations.AddField(
            model_name='ability',
            name='costs',
            field=models.ManyToManyField(to='lores.abilitycost'),
        ),
        migrations.AddField(
            model_name='ability',
            name='effects',
            field=models.ManyToManyField(blank=True, to='lores.effect'),
        ),
        migrations.AddField(
            model_name='ability',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
