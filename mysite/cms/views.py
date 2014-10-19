#!/usr/bin/ python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import RequestContext
from cms.models import Book
from cms.forms import BookForm
from django.views.generic.list import ListView

def book_list(request):
#	return HttpResponse(u'書籍の一覧')
	books = Book.objects.all().order_by('id')
	return render_to_response('cms/book_list.html',
								{'books': books},
								context_instance=RequestContext(request))

def book_edit(request ,book_id = None):
#	return HttpResponse(u'書籍の編集')
	if book_id:
		book = get_object_or_404(Book, pk=book_id)
	else:
		book = Book()

	if request.method == 'POST':
		form = BookForm(request.POST,instance=book)
		if form.is_valid():
			book = form.save(commit = False)
			book.save()
			return redirect('cms:book_list')
	else:
		form = BookForm(instance = book)

	return render_to_response('cms/book_edit.html',
								dict(form=form,book_id=book_id),
								context_instance=RequestContext(request))

def book_del(request , book_id):
#	return HttpResponse(u'書籍の削除')
	book = get_object_or_404(Book, pk=book_id)
	book.delete()
	return redirect('cms:book_list')

class ImpressionList(ListView):
	context_object_name = 'impressions'
	template_name = 'cms/impression_list.html'
	paginate_by = 2  # １ページは最大2件ずつでページングする

	def get(self, request , *args ,**kwargs):
		book = get_object_or_404(Book, pk=kwargs['book_id'])# 親の書籍を読む
		impressions = book.impressions.all().order_by('id') # 書籍の子供の、感想を読む
		self.object_list = impressions
		context = self.get_context_data(object_list = self.object_list,book = book)
		return self.render_to_response(context)









