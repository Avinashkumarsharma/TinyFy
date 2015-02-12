'''
Created on Jul 8, 2012

@author: Avi
'''
import os
 
def rel(*arg):
    print os.path.join(os.path.abspath(os.path.dirname(__file__)), *arg).replace('\\', '/')
rel('templates')
import sys
print sys.path
from shortner.models import links
#print links.objects.all().delete()
#ob,bool=links.objects.get_or_create(redirect_url="http://www.google.com")
'''if bool:
    ID=links.objects.latest('id').id
    ob=links.objects.get(id=ID)
    ob.short_url= "867nv"
    ob.save()'''
    
print links.objects.all()
    
    
