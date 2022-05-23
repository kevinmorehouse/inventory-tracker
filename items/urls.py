from django.urls import path

from .views import (
    ItemCreateView,
    ItemDetailView,
    ItemListView,
    ItemUpdateView,
    ItemDeleteView,
    ItemUndeleteView,
    DeletedItemDetailView,
    DeletedItemListView,
)

urlpatterns = [
    path("", ItemListView.as_view(), name="item_list"),
    path("deleted", DeletedItemListView.as_view(), name="deleted_item_list"),
    path("new/", ItemCreateView.as_view(), name="item_new"),
    path("<int:pk>/", ItemDetailView.as_view(), name="item_detail"),
    path(
        "<int:pk>/deleted",
        DeletedItemDetailView.as_view(),
        name="deleted_item_detail",
    ),
    path("<int:pk>/edit/", ItemUpdateView.as_view(), name="item_edit"),
    path("<int:pk>/delete/", ItemDeleteView.as_view(), name="item_delete"),
    path(
        "<int:pk>/undelete/", ItemUndeleteView.as_view(), name="deleted_item_undelete"
    ),
]
