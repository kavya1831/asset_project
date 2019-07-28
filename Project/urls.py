from django.conf.urls import url
from src.views.userview import UserView

# import testview from sample_app/view
from asset_mt.views import test_view
from asset_mt.views import asset_db_test

urlpatterns = [
    url(r'^user/', UserView.as_view()),
]