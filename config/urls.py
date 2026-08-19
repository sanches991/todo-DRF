
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from todo.views import TodoListCreateView, TodoRetrieveView, TodoDestroyView,TodoUpdateView
from users.views import RegisterCreateAPIView

#genericapiview
#from todo.views import TodoListView, TodoDetailView ,TodoListCreateView


# apiview
# from todo.views import TodoListCreateView , TodoDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("api/register/", RegisterCreateAPIView.as_view()),

    path("api/v1/todo/", TodoListCreateView.as_view()),

    path("api/v1/todo/<int:pk>/", TodoRetrieveView.as_view()),

    path("api/v1/todo/<int:pk>/", TodoUpdateView.as_view()),

    path("api/v1/todo/<int:pk>/", TodoDestroyView.as_view()),

    #genericapiview
    #path('api/v1/todo/', TodoListView.as_view()),
    #path('api/v1/todo/<int:pk>/', TodoDetailView.as_view()),

    # apiview
    # path('api/v1/todo/', TodoListCreateView.as_view()),
    # path('api/v1/todo/<int:pk>/', TodoDetailView.as_view())
]
