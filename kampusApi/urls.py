"""
URL configuration for kampusApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts import views as accountViews
from commerce import views as commerceViews
from community import views as communityViews
from forum import views as forumViews
from jobs import views as jobViews
from lost_and_find_items import views as LFIViews
from job_intern import views as internViews
from django.conf import settings
from django.conf.urls.static import static


# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r"accounts", accountViews.UserViewSet, basename="user")
router.register(r"commerce", commerceViews.ProductViewSet, basename="product")
router.register("commerce-categories", commerceViews.ProductCategoryViewSet, basename="product_category")
router.register(r"communities", communityViews.CommunityViewSet, basename="community")
router.register("communities-announcements", communityViews.CommunityAnnouncementViewSet, basename="community_announcement")
router.register(r"forum", forumViews.EntryViewSet, basename="forum_entry")
router.register("forum-comments", forumViews.EntryCommentViewSet, basename="forum_comment")
router.register("forum-likes", forumViews.EntryLikeViewSet, basename="forum_like")
router.register(r"jobs", jobViews.DiscountViewSet, basename="jobs")
router.register(r"lfis", LFIViews.ItemViewSet, basename="lfis")
router.register(r"intern", internViews.InternPlaceViewSet, basename="intern-places")
router.register("intern-announcements", internViews.InternAnnouncementViewSet, basename="intern_announcements")


# The API URLs are now determined automatically by the router.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/", include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
