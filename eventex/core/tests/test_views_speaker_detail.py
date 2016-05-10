# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r


class SpeakerDetailTest(TestCase):
    def setUp(self):
        url = r('core:speaker_detail', kwargs={'slug': 'henrique-bastos'})
        self.resp = self.client.get(url)

    def test_get(self):
        'GET should result in 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Template should be core/speaker_detail.html'
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        'Html must contain data.'
        self.assertContains(self.resp, 'Henrique Bastos')
        self.assertContains(self.resp, 'Passionate software developer!')
        self.assertContains(self.resp, 'http://henriquebastos.net')