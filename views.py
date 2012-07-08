from django.shortcuts import *
from django.http import Http404, HttpResponse


def get_home_page(request):
    context_instance=RequestContext(request)
    return render_to_response('index.html',None,context_instance)

def get_blog_page(request):
    context_instance=RequestContext(request)
    return render_to_response('blog.html',None,context_instance)