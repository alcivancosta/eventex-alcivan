# coding: utf-8
from django.db import models


class EmailContactManager(models.Manager):
    def get_query_set(self):
        qs = super(EmailContactManager, self).get_query_set()
        qs = qs.filter(kind='E')
        return qs


class PhoneContactManager(models.Manager):
    def get_query_set(self):
        qs = super(PhoneContactManager, self).get_query_set()
        qs = qs.filter(kind='P')
        return qs


class FaxContactManager(models.Manager):
    def get_query_set(self):
        qs = super(FaxContactManager, self).get_query_set()
        qs = qs.filter(kind='F')
        return qs