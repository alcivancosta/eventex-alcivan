# coding: utf-8
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/inscricao/%d/' % 1)
    else:
        return direct_to_template(request,
                                  'subscriptions/subscription_form.html',
                                  {'form': SubscriptionForm()})
