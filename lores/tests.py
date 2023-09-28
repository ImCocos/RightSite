from django.test import TestCase

from lores.serializers import StorySerializer, PageObjectSerializer
from lores.models import PageObject, Story

from pprint import pprint


class StorySerializerTest(TestCase):
    def setUp(self):
        pos = []
        for i in range(5):
            po = PageObject(text=f'test text {i}')
            po.save()
            pos.append(po)
        
        self.story = Story()
        self.story.page_objects = [po.pk for po in reversed(pos)]
        self.story.save()

        self.json_story = {
            'id': self.story.pk,
            'page_objects': [
                {
                    'id': PageObject.objects.get(pk=i).pk,
                    'text': PageObject.objects.get(pk=i).text,
                    'photo': None,
                } for i in self.story.page_objects
            ],
            'created': str(self.story.created),
        }

    def test_ok(self):
        serialized_data = dict(StorySerializer(self.story).data)
        self.assertEqual(self.json_story['id'], serialized_data['id'])
        self.assertEqual(self.json_story['created'], serialized_data['created'])
        self.assertEqual(self.json_story['page_objects'], serialized_data['page_objects'])


class PageObjectSerializerTest(TestCase):
    def setUp(self):
        self.page_object = PageObject(
            text='Test text 1',
            photo='Screenshot_from_2023-09-07_19-22-40.png',
        )
        self.page_object.save()

    def test_ok(self):
        serialized_data = dict(PageObjectSerializer(self.page_object).data)
        print(serialized_data['photo'])
        self.assertEqual(serialized_data['id'], 1)
        self.assertEqual(serialized_data['text'], 'Test text 1')
        self.assertEqual(serialized_data['photo'], '/media/Screenshot_from_2023-09-07_19-22-40.png')
