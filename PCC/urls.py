from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("usuario/", include('usuario.urls')),
    path("accounts/", include(urls)),
    path("sistema/", include('sistema.urls')),
    path("turma/", include('turmas.urls')),
    path("atividades/", include('atividades.urls')),
    path("comentarios/", include('comentarios.urls')),
    path("", include('home.urls')),
    path("bate_papo/", include('bate_papo.urls')),


] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
