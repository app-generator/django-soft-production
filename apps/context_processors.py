from django.conf import settings

def cfg_assets_root(request):

    if settings.DEBUG:
        return { 'ASSETS_BASE' : '/static/assets' }        
    else:            
        return { 'ASSETS_BASE' : settings.ASSETS_BASE }

