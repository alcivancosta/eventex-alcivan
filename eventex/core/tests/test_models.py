# coding: utf-8
from django.test import TestCase
from eventex.core.models import Speaker, Contact


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


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(name='Henrique Bastos',
                                              slug='henrique-bastos', url='http://henriquebastos.net',
                                              description='Passionate software developer!')

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='E',
                                         value='henrique@bastos.net')
        self.assertEqual(1, contact.pk)

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='P',
                                         value='21-1234567890')
        self.assertEqual(1, contact.pk)

    def test_fax(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='F',
                                         value='21-12345678')
        self.assertEqual(1, contact.pk)

    def test_unicode(self):
        'Speaker string representation should be the same.'
        self.assertEqual(u'Henrique Bastos', unicode(self.speaker))