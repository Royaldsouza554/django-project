from django.urls import path
from .views import project_submission
from django.views.generic import TemplateView

urlpatterns = [
      path('submit_project/', project_submission, name='submit_project'),
      path('project_success/', TemplateView.as_view(template_name ="project_success.html"), name='project_success'),
]