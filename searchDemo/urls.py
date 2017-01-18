from django.conf.urls import url
from django.contrib import admin
from .views import HomeView, ProductView, FacetedSearchView, autocomplete
from .settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^product/(?P<slug>[\w-]+)/$', ProductView.as_view(), name='product'),
    url(r'^search/autocomplete/$', autocomplete),
    url(r'^find/', FacetedSearchView.as_view(), name='haystack_search'),
    
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
