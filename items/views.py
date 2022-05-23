from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Item


class ItemCreateView(CreateView):
    model = Item
    template_name = "items/item_new.html"
    fields = (
        "name",
        "description",
        "quantity",
    )


class ItemDetailView(DetailView):
    model = Item
    template_name = "items/item_detail.html"


class ItemListView(ListView):
    model = Item
    template_name = "items/item_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ItemListView, self).get_context_data(*args, **kwargs)
        context["deleted_items"] = Item.all_objects.filter(deleted_at__isnull=False)
        return context


class ItemUpdateView(UpdateView):
    model = Item
    fields = (
        "name",
        "description",
        "quantity",
    )
    template_name = "items/item_edit.html"


class ItemDeleteView(UpdateView):
    model = Item
    fields = ("deletion_comment",)
    template_name = "items/item_delete.html"
    queryset = Item.all_objects.all()
    success_url = reverse_lazy("item_list")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return super().post(request, *args, **kwargs)


class ItemUndeleteView(UpdateView):
    model = Item
    template_name = "deleted_items/deleted_item_undelete.html"
    fields = []
    queryset = Item.all_objects.all()

    def get_success_url(self):
        return reverse_lazy("item_detail", kwargs={"pk": self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.undelete()
        return super().post(request, *args, **kwargs)


class DeletedItemDetailView(ItemDetailView):
    template_name = "deleted_items/deleted_item_detail.html"
    queryset = Item.all_objects.filter(deleted_at__isnull=False)


class DeletedItemListView(ItemListView):
    template_name = "deleted_items/deleted_item_list.html"
    queryset = Item.all_objects.filter(deleted_at__isnull=False)

    def get_context_data(self, *args, **kwargs):
        context = super(DeletedItemListView, self).get_context_data(*args, **kwargs)
        context["active_items"] = Item.all_objects.filter(deleted_at__isnull=True)
        return context
