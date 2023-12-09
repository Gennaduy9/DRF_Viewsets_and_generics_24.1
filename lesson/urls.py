from django.urls import path
from lesson.apps import LessonConfig
from lesson.views import LessonsListView, LessonsCreateView, LessonsUpdateView, LessonsRetrieveView, LessonsDestroyView

app_name = LessonConfig.name

urlpatterns = [
    path('', LessonsListView.as_view(), name='lessons_list'),
    path('create/', LessonsCreateView.as_view(), name='lessons_create'),
    path('update/<int:pk>/', LessonsUpdateView.as_view(), name='lessons_update'),
    path('retrieve/<int:pk>/', LessonsRetrieveView.as_view(), name='lessons_retrieve'),
    path('destroy/<int:pk>/', LessonsDestroyView.as_view(), name='lessons_destroy'),
]