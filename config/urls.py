"""twister URL Configuration"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('twister.posts.urls','twister.posts'), namespace='posts')),
    path('notifications/', include(('twister.notifications.urls','twister.notifications'), namespace='notifications')),
    path('inbox/', include(('twister.inbox.urls','twister.inbox'), namespace='inbox')),
    path('accounts/', include(('twister.accounts.urls','twister.accounts'), namespace='accounts')),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)