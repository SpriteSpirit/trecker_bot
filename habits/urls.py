from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import HabitViewSet

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r'', HabitViewSet, basename='habits')

urlpatterns = [] + router.urls
