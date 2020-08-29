"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, PolView, PolCreatView, PolUpdateView,PolDeleteView, PolChoicesCreateView,\
    ChoiceUpdateView, ChoiceDeleteView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pol/<int:pk>/', PolView.as_view(), name='pol_view'),
    path('pol/add/', PolCreatView.as_view(), name='pol_create'),
    path('pol/<int:pk>/update/', PolUpdateView.as_view(), name='pol_update'),
    path('pol/<int:pk>/delete/', PolDeleteView.as_view(), name='pol_delete'),

    path('pol/<int:pk>/choice/add/', PolChoicesCreateView.as_view(), name='choice_create'),
    path('pol/<int:pk>/choice/update/', ChoiceUpdateView.as_view(), name='choice_update'),
    path('pol/<int:pk>/choice/delete/',ChoiceDeleteView.as_view(), name='choice_delete')

]
