from django.urls import path


from celery_app.views import MainView, SaveUserView, MessageView


app_name = 'main'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('save_form/', SaveUserView.as_view(), name='save'),
    path('masseges/', MessageView.as_view(), name='masseges')
]

