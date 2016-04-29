# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):
    def test_has_fields(self):
        'Form must have 4 fields.'
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'cpf', 'email', 'phone'], form.fields)

    def test_cpf_is_digit(self):
        'CPF must only accept digits.'
        data = dict(name='Henrique Bastos', email='henrique@bastos.net',
                     cpf='12345678901', phone='21-96186180')
        data.update({'cpf': 'ABCD5678901'})
        form = SubscriptionForm(data)
        form.is_valid()

        self.assertItemsEqual(['cpf'], form.errors)