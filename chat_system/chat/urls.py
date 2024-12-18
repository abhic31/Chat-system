from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chat.views.thread_views import ThreadViewSet
from chat.views.message_views import MessageViewSet
from chat.views.participant_views import ThreadParticipantViewSet

router = DefaultRouter()
router.register(r'threads', ThreadViewSet, basename='thread')
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'participants', ThreadParticipantViewSet, basename='participant')

urlpatterns = [
    path('', include(router.urls)),
]
