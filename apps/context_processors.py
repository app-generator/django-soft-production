from django.conf import settings

def cfg_assets_root(request):

    if settings.DEBUG:
        return { 'ASSETS_ROOT' : '/static/assets' }        
    else:            
        return { 'ASSETS_ROOT' : settings.ASSETS_BASE }

