from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('plots.urls', 'plots'), namespace='plots')),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
