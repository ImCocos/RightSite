from django.db import models
from django.contrib.postgres.fields import ArrayField
from users.models import User


class PageObject(models.Model):
    text = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='images/stories/', blank=True, null=True)

    def __str__(self):
        return f'{self.__class__.__name__}-{self.pk}'


class Story(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateField(name='created', auto_created=True, auto_now=True)
    page_objects = ArrayField(models.IntegerField(), name='page_objects', null=True)

    def __str__(self):
        return f'{self.__class__.__name__}-{self.pk}'


class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, default='Without description')
    photo = models.ImageField(upload_to='images/categories/', blank=True, null=True)

    def __str__(self):
        return f'{self.__class__.__name__}-{self.name}'


class Effect(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, default='Without description')
    photo = models.ImageField(upload_to='images/effects/', blank=True, null=True)

    def __str__(self):
        return f'{self.__class__.__name__}-{self.name}'


class Unit(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, default='Without description')
    photo = models.ImageField(upload_to='images/units/', blank=True, null=True)

    def __str__(self):
        return f'{self.__class__.__name__}-{self.name}'


class Cost(models.Model):
    cost = models.PositiveIntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.__class__.__name__}-{self.cost}-{self.unit.name}'


class Ability(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, default='Without description')
    effects = models.ManyToManyField(Effect, blank=True)
    is_passive = models.BooleanField() 
    costs = models.ManyToManyField(Cost)
    photo = models.ImageField(upload_to='images/abilities/', blank=True, null=True)

    def __str__(self):
        return f'{self.__class__.__name__}-{self.name}'


class ItemClass(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, default='Without description')
    photo = models.ImageField(upload_to='images/itemclasses/', blank=True, null=True)

    def __str__(self):
        return f'{self.__class__.__name__}-{self.name}'


class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, default='Without description')
    item_class = models.ForeignKey(ItemClass, on_delete=models.SET_NULL, null=True)
    effects = models.ManyToManyField(Effect, blank=True)
    photo = models.ImageField(upload_to='images/items/', blank=True, null=True)

    def __str__(self):
        return f'{self.__class__.__name__}-{self.name}'


class Hero(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    name = models.CharField(max_length=250)
    description = models.TextField(default='Without description')
    abilities = models.ManyToManyField(Ability, blank=True)
    photo = models.ImageField(upload_to='images/heroes/', blank=True, null=True)
    items = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return f'{self.__class__.__name__}-{self.name}'
