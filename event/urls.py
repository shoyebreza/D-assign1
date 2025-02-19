from django.urls import path

from event.views import home, about, service, faq, event, blog, gallery

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('faq/', faq, name='faq'),
    path('event/', event, name='event'),
    path('blog/', blog, name='blog'),
    path('gallery/', gallery, name='gallery'),
]
