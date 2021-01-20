from django.contrib import admin
from .models import User, Lead, Agent

# Register models.

admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
