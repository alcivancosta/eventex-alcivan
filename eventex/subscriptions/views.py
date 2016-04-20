# coding: utf-8
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        if not form.is_valid():
            return direct_to_template(request,
                                      'subscriptions/subscription_form.html',
                                      {'form': form})
        obj = form.save()
        return HttpResponseRedirect('/inscricao/%d/ ' % obj.pk)
    else:
        return direct_to_template(request,
                                'subscriptions/subscription_form.html',
                                {'form': SubscriptionForm()})
