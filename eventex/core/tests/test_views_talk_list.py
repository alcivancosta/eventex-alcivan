# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r


class TalkListTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:talk_list'))

    def test_get(self):
        'GET must result in 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Template should be core/talk_list.html'
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        'Html should list talks.'
        self.assertContains(self.resp, u'Título da palestra', 2)
        self.assertContains(self.resp, u'/palestras/1/')
        self.assertContains(self.resp, u'/palestras/2/')
        self.assertContains(self.resp, u'/palestrantes/henrique-bastos/', 2)
        self.assertContains(self.resp, u'Passionate software developer!', 2)
        self.assertContains(self.resp, u'Henrique Bastos', 2)
        self.assertContains(self.resp, u'Descrição da palestra', 2)

    def test_morning_talks_in_context(self):
        self.assertIn('morning_talks', self.resp.context)

    def test_afternoon_talks_in_context(self):
        self.assertIn('afternoon_talks', self.resp.context)