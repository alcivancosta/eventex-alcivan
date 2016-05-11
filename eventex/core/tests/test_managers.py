# coding: utf-8
from django.test import TestCase
from eventex.core.models import Contact, Speaker


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Henrique Bastos',
                                   slug='henrique-bastos', url='http://henriquebastos.net')
        s.contact_set.add(Contact(kind='E', value='henrique@bastos.net'))

    def test_emails(self):
        qs = Contact.emails.all()
        expected = ['<Contact: henrique@bastos.net>']
        self.assertQuerysetEqual(qs, expected)