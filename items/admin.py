from django.contrib import admin
from .models import Item


class SoftDeleteAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = self.model.all_objects
        ordering = self.get_ordering(request)
        if ordering:
            queryset = queryset.order_by(*ordering)
        return queryset

    def delete_model(self, request, obj):
        obj.hard_delete()


class ItemAdmin(SoftDeleteAdmin):
    list_display = ("name", "description", "quantity", "deleted_at")


admin.site.register(Item, ItemAdmin)
