from django.db import models

# Create your models here.
class links(models.Model):
    redirect_url= models.URLField(unique=True)
    short_url=models.CharField(max_length= 5, blank= False)
    
    def __unicode__(self):
        return u'redirecr_url=%s, short_url=%s' %(self.redirect_url,self.short_url)
    