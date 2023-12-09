from rest_framework.routers import DefaultRouter

from course.apps import CourseConfig
from course.views import CoursesViewSet

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'cours', CoursesViewSet, basename='cours')

urlpatterns = [] + router.urls