from django.conf.urls import url
from ext import views

urlpatterns = [
    url(r'^$',views.show_pdf,name='show_pdf'),
    url(r'^edit/$', views.GeneratePDF.as_view(), name='pdf_edit')
    ]
