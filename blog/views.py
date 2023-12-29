from django.shortcuts import render
from django.views.generic import View
from .forms import PostCreateFrom


class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'blog_list.html', context)


class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }

        return render(request, "blog_create.html", context)
    
    def post(self, request, *args, **kwargs):
        context = {

        }

        return render(request, "blog_create.html", context)