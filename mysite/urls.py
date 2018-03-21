
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse


def demo(request):
    return HttpResponse("post_list.html"),

def sum(request, a, b):
    s = int(a) + int(b)
    return HttpResponse(s)

urlpatterns = [
    url(r'^[12]+$',demo),
    url(r'^sum/(?P<a>\d+)/(?P<b>/d+)/$', sum),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
]
