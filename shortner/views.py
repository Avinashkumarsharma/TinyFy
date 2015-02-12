# Create your views here.
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from shorten import UrlEncoder
from models import links
def showurl(request):
    domain= request.META['HTTP_HOST']
    if 'longurl' in request.POST and request.POST['longurl'] !='':
        lurl= request.POST['longurl']
        ob,bool= links.objects.get_or_create(redirect_url=lurl)
        if bool:
            ID=links.objects.latest('id').id
            upattern= UrlEncoder().encode_url(ID)
            setsurl= links.objects.get(id=ID)
            setsurl.short_url= upattern
            setsurl.save()
            domain=request.META['HTTP_HOST']
            shortURL=domain+"/" +upattern
            
        else:
            upattern= links.objects.get(redirect_url=lurl).short_url
            shortURL=domain+"/" +upattern
        return render_to_response('show.html',{'urlo':request.POST['longurl'], 'shorturl':shortURL}, context_instance=RequestContext(request))    
        
        
    else:
        return render_to_response('index.html', context_instance=RequestContext(request))

def tiny(request):
    return render_to_response('index.html', context_instance=RequestContext(request))
def redirect_to(request,urlpattern):
    ob=links.objects.get(short_url=urlpattern)
    redirectURL=ob.redirect_url
    return redirect(redirectURL)