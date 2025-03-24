from django.contrib import admin
from django.urls import include, path
from jool import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("", include("jool.urls")),
    path("art/", include("art.urls")),
    path("music/", include("music.urls")),
    path("collabo/", include("collabo.urls")),
    path("shop/", include("shop.urls")),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
