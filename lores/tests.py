from django.test import TestCase

from .serializers import *
from .models import *

from pprint import pprint


class APIHeroTest(TestCase):
    def setUp(self):
        self.hero = Hero.objects.create(
            link='testlink',
            name='testname')
        
        self.json_hero = {
            'abilities': [],
            'categories': [],
            'description': 'Without description',
            'id': 1,
            'items': [],
            'link': 'testlink',
            'name': 'testname',
            'owner': None,
            'photo': None
            }
    
    def test_ok(self):
        serialized_data = dict(HeroSerializer(self.hero).data)
        
        self.assertEqual(serialized_data['name'], self.hero.name)
        self.assertEqual(serialized_data['link'], self.hero.link)
        self.assertEqual(serialized_data['description'], self.hero.description)
        self.assertEqual(serialized_data['id'], self.hero.id)
        self.assertEqual(serialized_data['items'], list(self.hero.items.all()))
        self.assertEqual(serialized_data['abilities'], list(self.hero.abilities.all()))
        self.assertEqual(serialized_data['categories'], list(self.hero.categories.all()))
        self.assertEqual(serialized_data['owner'], self.hero.owner)
        self.assertEqual(serialized_data['photo'], self.hero.photo)
