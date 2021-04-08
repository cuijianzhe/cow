from django.urls import path

from account.apis import user as user_api


urlpatterns = [
    path('user/login/', user_api.LoginApi.as_view()),
    path('user/', user_api.UserApi.as_view()),
    path('user/list/', user_api.ListUserApi.as_view()),
    path('user/create/', user_api.CreateUserApi.as_view()),

]
