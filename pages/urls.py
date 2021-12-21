from django.urls import path
from .views import ContactCreatView, AboutTemplateView, HomeTemplateView

app_name = 'pages'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name="home"),
    path('contact/', ContactCreatView.as_view(), name="contact"),
    path('about/', AboutTemplateView.as_view(), name="about")
]
