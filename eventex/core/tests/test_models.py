# coding: utf-8
from django.test import TestCase
from eventex.core.models import Speaker


class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker(name='Henrique Bastos',
                               slug='henrique-bastos',
                               url='http://henriquebastos.net',
                               description='Passionate software developer!')
        self.speaker.save()

    def test_create(self):
        'Speaker instance should be saved.'
        self.assertEqual(1, self.speaker.pk)