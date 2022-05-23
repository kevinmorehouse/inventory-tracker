from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models.query import QuerySet


class SoftDeleteQuerySet(QuerySet):
    def delete(self):
        for obj in self:
            obj.deleted_at = timezone.now()
            obj.save()

    def undelete(self):
        for obj in self:
            obj.deleted_at = None
            obj.save()


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    deletion_comment = models.TextField(null=True, blank=True)
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        return super(SoftDeleteQuerySet, self).delete()

    def undelete(self):
        self.deleted_at = None
        self.deletion_comment = None
        self.save()

    class Meta:
        abstract = True


class Item(SoftDeleteModel):
    name = models.CharField(max_length=280)
    description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})
