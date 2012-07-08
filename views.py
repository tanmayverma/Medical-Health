from django.shortcuts import *
from django.http import Http404, HttpResponse


def get_home_page(request):
    context_instance=RequestContext(request)
    return render_to_response('index.html',None,context_instance)

def get_questions_page(request):
    context_instance=RequestContext(request)
    return render_to_response('questions/index.html',None,context_instance)

def get_pathlabs_page(request):
    context_instance=RequestContext(request)
    return render_to_response('pathlabs/index.html',None,context_instance)

def get_about_page(request):
    context_instance=RequestContext(request)
    return render_to_response('about/index.html',None,context_instance)

def get_contact_page(request):
    context_instance=RequestContext(request)
    return render_to_response('contact/index.html',None,context_instance)