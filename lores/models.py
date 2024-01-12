from django.db import models

from users.models import User


class Category(models.Model):
    link = models.CharField(max_length=500)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, default='Without description')
    photo = models.ImageField(upload_to='images/categories/', blank=True, null=True)

    def __str__(self):
        return f'{self.__class__.__name__}-{self.name}'


class Effect(models.Model):
    link = models.CharField(max_length=500)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, default='Without description')
    photo = models.ImageField(upload_to='images/effects/', blank=True, null=True)

    def __str__(self):
        return f'{self.__class__.__name__}-{self.name}'


class Unit(models.Model):
    link = models.CharField(max_length=500)
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



class AbilityType(models.Model):
    mode = models.CharField(default='active', max_length=50)

    def __str__(self):
        return f'{self.__class__.__name__}-{self.mode}'


class Per(models.Model):
    unit = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.__class__.__name__}-{self.unit}'


class AbilityCost(models.Model):
    cost = models.PositiveIntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    per = models.ForeignKey(Per, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.__class__.__name__}-{self.cost}\
                {self.unit.name}/{self.per.unit}'


class Ability(models.Model):
    link = models.CharField(max_length=500)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, default='Without description')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    effects = models.ManyToManyField(Effect, blank=True)
    ab_type = models.ForeignKey(AbilityType, on_delete=models.SET_NULL, null=True)
    costs = models.ManyToManyField(AbilityCost)
    photo = models.ImageField(upload_to='images/abilities/', blank=True, null=True)
    def __str__(self):
        return f'{self.__class__.__name__}-{self.name}'


class ItemClass(models.Model):
    link = models.CharField(max_length=500)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, default='Without description')
    photo = models.ImageField(upload_to='images/itemclasses/', blank=True, null=True)

    def __str__(self):
        return f'{self.__class__.__name__}-{self.name}'


class Item(models.Model):
    link = models.CharField(max_length=500)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, default='Without description')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    item_class = models.ForeignKey(ItemClass, on_delete=models.SET_NULL, null=True)
    effects = models.ManyToManyField(Effect, blank=True)
    photo = models.ImageField(upload_to='images/items/', blank=True, null=True)

    def __str__(self):
        return f'{self.__class__.__name__}-{self.name}'


class HeroClass(models.Model):
    link = models.CharField(max_length=500)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, default='Without description')
    photo = models.ImageField(upload_to='images/heroesclasses/', blank=True, null=True)

    def __str__(self):
        return f'{self.__class__.__name__}-{self.name}'


class Hero(models.Model):
    link = models.CharField(max_length=500)
    name = models.CharField(max_length=250)
    description = models.TextField(default='Without description')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    abilities = models.ManyToManyField(Ability, blank=True)
    photo = models.ImageField(upload_to='images/heroes/', blank=True, null=True)
    items = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return f'{self.__class__.__name__}-{self.name}'
