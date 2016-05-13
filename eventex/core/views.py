# coding: utf-8
from datetime import time
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from eventex.core.models import Speaker, Talk


def homepage(request):
    return direct_to_template(request, template='index.html')


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    context = {'speaker': speaker}
    return direct_to_template(request, 'core/speaker_detail.html',
                              context)


def talk_list(request):
    midday = time(12)
    context = {
        'morning_talks': Talk.objects.filter(start_time__lt=midday),
        'afternoon_talks': Talk.objects.filter(start_time__gte=midday),
    }
    return direct_to_template(request, 'core/talk_list.html', context)
