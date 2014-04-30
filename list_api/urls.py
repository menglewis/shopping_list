from django.conf.urls import patterns, url, include
from . import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'shopping_lists', views.ShoppingListViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'shopping_items', views.ShoppingItemViewSet)
router.register(r'categories', views.CategoryViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
)
