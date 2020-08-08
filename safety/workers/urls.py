'''
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
'''
from django.urls import path

# from rest_framework.routers import DefaultRouter


from .views import (
    WorkerListView,
    # WorkerModelViewSetView,
)


# router = DefaultRouter()
# router.register(r'', WorkerModelViewSetView)

urlpatterns = [
    path('', WorkerListView.as_view()),
    # path('', include(router.urls)),
]
