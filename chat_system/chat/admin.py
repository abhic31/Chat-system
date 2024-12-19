from django.contrib import admin
from chat.models import Thread, ThreadParticipant, Message  # Import your models

# Register your models here.
admin.site.register(Thread)
admin.site.register(ThreadParticipant)
admin.site.register(Message)