from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework.routers import SimpleRouter

from users.views import *
from lores.views import *
import api.v1.lores.views as lores_api_views
import api.v1.users.views as users_api_views
from api.services.api_url_maker import MakeAPIUrlFromPackage

from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView


make_url = MakeAPIUrlFromPackage()
router = SimpleRouter()

router.register(make_url(users_api_views), users_api_views.UserView)
router.register(make_url(lores_api_views, 'heroes'), lores_api_views.APIHeroView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('', include('lores.urls')),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
