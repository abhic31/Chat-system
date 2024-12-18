from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chat.views.thread_views import ThreadViewSet
from chat.views.message_views import MessageViewSet
from chat.views.participant_views import ThreadParticipantViewSet

router = DefaultRouter()
router.register(r'threads', ThreadViewSet, basename='thread')

urlpatterns = [
    path('', include(router.urls)),
    path('threads/<int:thread_id>/', ThreadViewSet.as_view({'get': 'retrieve'}), name='thread-detail'),
    path('threads/<uuid:thread_id>/messages/', MessageViewSet.as_view({'get': 'list', 'post': 'create'}), name='message-list-create'),
    path('threads/<uuid:thread_id>/participants/', ThreadParticipantViewSet.as_view({'get': 'list', 'post': 'create'}), name='participants-list-create')
    
]
