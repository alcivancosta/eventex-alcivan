# coding: utf-8
from django.contrib import admin
from eventex.subscriptions.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'phone', 'created_at')

admin.site.register(Subscription, SubscriptionAdmin)