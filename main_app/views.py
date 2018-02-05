# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Snippet
from .forms import SnippetForm
# Http imports a specific class from a module


# Create your views here.
# Map your views to a URL
def index(request):
    snippets = Snippet.objects.all()
    form = SnippetForm()
    return render(request, 'index.html',
                             {'snippets':snippets, 'form':form})

def post_snippet(request):
    form = SnippetForm(request.POST)
    if form.is_valid():
        snippet = Snippet(title = form.cleaned_data['title'],
                          language = form.cleaned_data['language'],
                          img_url = form.cleaned_data['img_url'],
                          description = form.cleaned_data['description'])
        snippet.save()
    return HttpResponseRedirect('/')

# class Snippet:
#     def __init__(self, title, language, img_url, description):
#         self.title = title
#         self.language = language
#         self.img_url = img_url
#         self.description = description

# snippets = [
#     Snippet('Installing Django', 'django', 'https://swapnilkadam.files.wordpress.com/2017/03/django1.png?w=683', 'Make sure Python is installed. Then use pip to install Django'),
#     Snippet('Creating a Django Project', 'django', 'https://i.ytimg.com/vi/8KWVEc6vFgA/maxresdefault.jpg', 'to install and create the Django project. Like create react app'),
#     Snippet('Running the Project', 'python', 'https://i0.wp.com/www.computersnyou.com/wp-content/uploads/2015/07/virtualenv.jpeg?resize=902%2C274&ssl=1', 'Use this code to run your python project')

# ]
