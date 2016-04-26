# coding: utf-8
from django.utils.datetime_safe import datetime
from django.contrib import admin
from eventex.subscriptions.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'email','phone', 'created_at',
                    'subscribed_today')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'email', 'phone', 'created_at')

    def subscribed_today(self, obj):
        return obj.created_at.date() == datetime.today().date()

admin.site.register(Subscription, SubscriptionAdmin)