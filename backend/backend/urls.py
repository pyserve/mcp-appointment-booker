from accounts.urls import router as AccountRouter
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.registry.extend(AccountRouter.registry)

urlpatterns = [path("admin/", admin.site.urls), path("", include(router.urls))]
