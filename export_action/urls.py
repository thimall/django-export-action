from django.urls import path, include, re_path
from django.contrib.admin.views.decorators import staff_member_required
from .views import AdminExport

app_name = 'export_action'
view = staff_member_required(AdminExport.as_view())
urlpatterns = [
   re_path(r'^export/$', view, name="export"),
]
