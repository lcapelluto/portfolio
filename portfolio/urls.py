from django.conf.urls import url
from portfolio import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^education/$', views.education_view, name='education'),
    url(r'^experience/$', views.experience_view, name='experience'),
    url(r'^more/$', views.more_view, name='more'),
    url(r'^contactme/$', views.contact_view, name='contact'),
    url(r'^more/recipes/$', views.recipes_index, name='recipes'),
]
