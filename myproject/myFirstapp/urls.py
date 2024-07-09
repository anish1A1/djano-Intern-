
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views 


urlpatterns = [
    path('', views.firstfun, name='home'),
    path('blog/', views.blog, name = 'Blog'),
    path('blog/create_blog/', views.create_blog, name='create_blog'),
    path('blog/update_blog/<int:b_id>', views.update_blog, name='update_blog'),
    path('blog/delete_blog/<int:b_id>', views.delete_blog, name='delete_blog'),
   
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)