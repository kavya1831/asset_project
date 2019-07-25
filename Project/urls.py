from django.conf.urls import url
from django.contrib import admin

# import testview from sample_app/view
from asset_mt.views import test_view
from asset_mt.views import asset_db_test

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^testview/', test_view),
    url(r'^asset/db/view/', asset_db_test),
]