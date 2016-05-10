# coding: utf-8
from django.views.generic.simple import direct_to_template
from eventex.core.models import Speaker


def homepage(request):
    return direct_to_template(request, template='index.html')


def speaker_detail(request, slug):
    context = {'speaker': Speaker()}
    return direct_to_template(request, 'core/speaker_detail.html',
                              context)