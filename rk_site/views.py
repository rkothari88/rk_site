from django.http import HttpResponse
from django.shortcuts import render_to_response

def home_page(request):
    return render_to_response('resources/index.html', self.context, RequestContext(self.request))

