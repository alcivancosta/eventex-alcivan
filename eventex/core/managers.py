# coding: utf-8
from django.db import models


class EmailContactManager(models.Manager):
    def get_query_set(self):
        qs = super(EmailContactManager, self).get_query_set()
        qs = qs.filter(kind='E')
        return qs