# coding: utf-8
from django.views.generic.simple import direct_to_template


def homepage(request):
    return direct_to_template(request, template='index.html')


def speaker_detail(request, slug):
    return direct_to_template(request, 'core/speaker_detail.html')