#encoding:utf-8
from django.http import HttpResponse
import Image,ImageDraw,ImageFont,random,StringIO
import os
from django.shortcuts import render_to_response as render
from DjangoVerifyCode import Code

def code(request):
    code =  Code(request)
    code.words = ['hello','world','helloworld']
    #code.type = 'world'
    code.type = 'number'
    return code.display()

def index(request):
    _code = request.GET.get('code') or ''
    if not _code:
        return render('index.html',locals())

    code = Code(request)
    if code.check(_code):
        return HttpResponse("""<h1>^_^</h1>""")
    return HttpResponse("""<h1>:-(</h1>""")

