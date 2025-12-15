from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('tasks/', views.task_list_create.as_view(), name='task-list-create'),
    path('task/<int:task_id>/' , views.Mark_task_as_completed.as_view(), name='mark_as_completed'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
