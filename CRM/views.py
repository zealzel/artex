from django.http import HttpResponse
from django.template import Context,loader
from django.shortcuts import render_to_response
from django.shortcuts import render

def hello(request,var):
    r1=request.path
    #import pdb;pdb.set_trace()
    value=request.META.items()
    
    template=loader.get_template('hello.html')
    context=Context({'heading':var,'items':value,})
    
    if len(var)==1:
        html=[]
        for k,v in value:
            html.append('<tr><td>%s</td><td>%s</td></tr>' % (k,v))

        content='<h1>%s</h1>'%var
        content=content + '\n'.join(html)
        content='<table>%s</table>' % content
        return HttpResponse(content)
    elif len(var)==2:
        return HttpResponse(template.render(context))
    else:
        return render_to_response('hello.html',var,context)
        
def myForm(request):
    path=request.path
    return render_to_response('myform.html',{'path':path,})


def search(request):
    if 'q' in request.GET:
        message='you type %s' % request.GET['q']
    else:
        message='you submitted an empty form'
    return HttpResponse(message)
