# coding: utf-8
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def new(request):
    return direct_to_template(request, 'subscriptions/subscription_form.html',
                              {'form': SubscriptionForm()})

def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return direct_to_template(request, 'subscriptions/subscription_form.html',
                                  {'form': form})
    obj = form.save()
    return HttpResponseRedirect('/inscricao/%d/' % obj.pk)

