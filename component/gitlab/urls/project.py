from django.urls import path

from component.gitlab.apis import project as project_api


urlpatterns = [
    path('gitlab/project/list/', project_api.ListGitlabProjectApi.as_view()),
]
