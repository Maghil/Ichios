from django.urls import path
from . import views
urlpatterns = [
   path('icreg/',views.reg ,name='icreg'),
   path('iclogon/',views.logon ,name='iclogon'),
   path('ichome/',views.dashboard ,name='ichome'),
   path('iclogs/',views.logging ,name='iclogs'),
   path('ichome/logout',views.logoutUser ,name='logout'),
   path('icrecent',views.recentdo ,name='icrecent'),
   path('iccontent',views.content ,name='iccontent'),
   path('del/<str:hash_value>',views.delete_file)
]