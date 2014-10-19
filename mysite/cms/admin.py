#!/usr/bin/ python
# -*- coding: utf-8 -*-

from django.contrib import admin
from cms.models import Book, Impression


class BookAdmin(admin.ModelAdmin):
	"""docstring for BookAdmin"""
	list_display = ('id','name','publisher','page',)
	list_display_links = ('id','name',)



class ImpressionAdmin(admin.ModelAdmin):
	"""docstring for ImpressionAdmin"""
	list_display = ('id','comment',)
	list_display_links = ('id','comment',)


admin.site.register(Book,BookAdmin)
admin.site.register(Impression,ImpressionAdmin)
