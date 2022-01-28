"""sample1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# Third Party Library
from django.urls import path
from django.views.generic import TemplateView

# Local Library
from .views import RequestPostAllListView
from .views import RequestPostCreateView
from .views import RequestPostDetailView
from .views import RequestPostListView
from .views import RequestPostUpdateView
from .views import approve_request_post

urlpatterns = [
    path("", view=TemplateView.as_view(template_name="join_request/home.html"), name="join_request_home"),
    path("posts/", view=RequestPostListView.as_view(), name="join_request_list"),
    path("posts_all/", view=RequestPostAllListView.as_view(), name="join_request_list_all"),
    path("create/", view=RequestPostCreateView.as_view(), name="join_request_create"),
    path(route="posts/<int:pk>/", view=RequestPostDetailView.as_view(), name="join_request_detail"),
    path(route="posts/<int:pk>/update/", view=RequestPostUpdateView.as_view(), name="join_request_update"),
    path(route="posts/<int:pk>/approve/", view=approve_request_post, name="join_request_approve"),
]
