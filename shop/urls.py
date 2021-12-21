from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('posts.urls', namespace='posts')),
    path('', include('pages.urls', namespace='pages')),  # namespace bu pages-urls-ichida-yoziladi
    path('product/', include('product.urls', namespace='product')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
