# coding: utf-8
from django.test import TestCase
from eventex.core.models import Contact, Speaker


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Henrique Bastos',
                                   slug='henrique-bastos', url='http://henriquebastos.net')
        s.contact_set.add(Contact(kind='E', value='henrique@bastos.net'),
                          Contact(kind='P', value='21-96186180'),
                          Contact(kind='F', value='21-12345678'))

    def test_emails(self):
        qs = Contact.emails.all()
        expected = ['<Contact: henrique@bastos.net>']
        self.assertQuerysetEqual(qs, expected)

    def test_phones(self):
        qs = Contact.phones.all()
        expected = ['<Contact: 21-96186180>']
        self.assertQuerysetEqual(qs, expected)

    def test_faxes(self):
        qs = Contact.faxes.all()
        expected = ['<Contact: 21-12345678>']
        self.assertQuerysetEqual(qs, expected)