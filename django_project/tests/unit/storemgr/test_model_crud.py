import os
import random

import django
from django.apps import apps
from django.test import TestCase
from model_bakery import baker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


class BrandTests(TestCase):
    """test CRUD operations on Brand"""

    def setUp(self):
        self.model = apps.get_model("storemgr", "brand")
        self.to_bake = "storemgr.Brand"
        self.logentry = apps.get_model("auditlog", "LogEntry")

    def bake(self):
        """add row"""
        return baker.make(
            self.to_bake,
        )

    def test_create(self):
        """verify object can be created"""
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)

    def test_create_auditlog(self):
        """verify an auditlog entry is created when new row is created"""
        row = self.bake()
        log = self.logentry.objects.filter(content_type__model=row._meta.model_name, object_pk=row.pk).latest("pk")
        self.assertIsNotNone(log)
        self.assertEqual(log.content_type.model, row._meta.model_name)
        self.assertEqual(log.object_pk, str(row.pk))
        self.assertEqual(log.action, 0)

    def test_read(self):
        """verify object can be read"""
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """verify object can be deleted"""
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)

    def test_delete_auditlog(self):
        """verify an auditlog entry is created when a row is deleted"""
        row = self.bake()
        object_repr = row.__str__()
        object_pk = row.pk
        row.delete()
        log = self.logentry.objects.filter(
            content_type__model=row._meta.model_name, object_repr__icontains=object_repr
        ).latest("pk")
        self.assertIsNotNone(log)
        self.assertEqual(log.content_type.model, row._meta.model_name)
        self.assertEqual(log.action, 2)

    def test_update_name(self):
        """verify name (CharField) can be updated"""
        row = self.bake()
        original_value = row.name
        updated_value = baker.prepare(self.to_bake, _fill_optional=["name"]).name
        setattr(row, "name", updated_value)
        row.save()
        self.assertEqual(getattr(row, "name"), updated_value)
        self.assertNotEqual(getattr(row, "name"), original_value)
        # verify auditlog entry
        log = self.logentry.objects.filter(content_type__model=row._meta.model_name, object_pk=row.pk).latest("pk")
        self.assertIsNotNone(log)
        self.assertEqual(log.content_type.model, row._meta.model_name)
        self.assertEqual(log.object_pk, str(row.pk))
        self.assertEqual(log.action, 1)


class CustomerTests(TestCase):
    """test CRUD operations on Customer"""

    def setUp(self):
        self.model = apps.get_model("storemgr", "customer")
        self.to_bake = "storemgr.Customer"
        self.logentry = apps.get_model("auditlog", "LogEntry")

    def bake(self):
        """add row"""
        return baker.make(
            self.to_bake,
        )

    def test_create(self):
        """verify object can be created"""
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)

    def test_create_auditlog(self):
        """verify an auditlog entry is created when new row is created"""
        row = self.bake()
        log = self.logentry.objects.filter(content_type__model=row._meta.model_name, object_pk=row.pk).latest("pk")
        self.assertIsNotNone(log)
        self.assertEqual(log.content_type.model, row._meta.model_name)
        self.assertEqual(log.object_pk, row.pk)
        self.assertEqual(log.action, 0)

    def test_read(self):
        """verify object can be read"""
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """verify object can be deleted"""
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)

    def test_delete_auditlog(self):
        """verify an auditlog entry is created when a row is deleted"""
        row = self.bake()
        object_repr = row.__str__()
        object_pk = row.pk
        row.delete()
        log = self.logentry.objects.filter(
            content_type__model=row._meta.model_name, object_repr__icontains=object_repr
        ).latest("pk")
        self.assertIsNotNone(log)
        self.assertEqual(log.content_type.model, row._meta.model_name)
        self.assertEqual(log.action, 2)

    def test_update_email(self):
        """verify email (CharField) can be updated"""
        row = self.bake()
        original_value = row.email
        updated_value = baker.prepare(self.to_bake, _fill_optional=["email"]).email
        setattr(row, "email", updated_value)
        row.save()
        self.assertEqual(getattr(row, "email"), updated_value)
        self.assertNotEqual(getattr(row, "email"), original_value)
        # verify auditlog entry
        log = self.logentry.objects.filter(content_type__model=row._meta.model_name, object_pk=row.pk).latest("pk")
        self.assertIsNotNone(log)
        self.assertEqual(log.content_type.model, row._meta.model_name)
        self.assertEqual(log.object_pk, row.pk)
        self.assertEqual(log.action, 1)

    def test_update_first_name(self):
        """verify first_name (CharField) can be updated"""
        row = self.bake()
        original_value = row.first_name
        updated_value = baker.prepare(self.to_bake, _fill_optional=["first_name"]).first_name
        setattr(row, "first_name", updated_value)
        row.save()
        self.assertEqual(getattr(row, "first_name"), updated_value)
        self.assertNotEqual(getattr(row, "first_name"), original_value)
        # verify auditlog entry
        log = self.logentry.objects.filter(content_type__model=row._meta.model_name, object_pk=row.pk).latest("pk")
        self.assertIsNotNone(log)
        self.assertEqual(log.content_type.model, row._meta.model_name)
        self.assertEqual(log.object_pk, row.pk)
        self.assertEqual(log.action, 1)

    def test_update_last_name(self):
        """verify last_name (CharField) can be updated"""
        row = self.bake()
        original_value = row.last_name
        updated_value = baker.prepare(self.to_bake, _fill_optional=["last_name"]).last_name
        setattr(row, "last_name", updated_value)
        row.save()
        self.assertEqual(getattr(row, "last_name"), updated_value)
        self.assertNotEqual(getattr(row, "last_name"), original_value)
        # verify auditlog entry
        log = self.logentry.objects.filter(content_type__model=row._meta.model_name, object_pk=row.pk).latest("pk")
        self.assertIsNotNone(log)
        self.assertEqual(log.content_type.model, row._meta.model_name)
        self.assertEqual(log.object_pk, row.pk)
        self.assertEqual(log.action, 1)


class InvoiceTests(TestCase):
    """test CRUD operations on Invoice"""

    def setUp(self):
        self.model = apps.get_model("storemgr", "invoice")
        self.to_bake = "storemgr.Invoice"

    def bake(self):
        """add row"""
        return baker.make(
            self.to_bake,
        )

    def test_create(self):
        """verify object can be created"""
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)

    def test_read(self):
        """verify object can be read"""
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """verify object can be deleted"""
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)

    def test_update_order(self):
        """verify order (ForeignKey) can be updated"""
        row = self.bake()
        original_value = row.order
        baker.make(self.model.order.field.related_model._meta.label, _fill_optional=True)
        if original_value:
            updated_value = random.choice(self.model.order.field.related_model.objects.exclude(pk=original_value.pk))
        else:
            updated_value = random.choice(self.model.order.field.related_model.objects.all())
        setattr(row, "order", updated_value)
        row.save()
        self.assertEqual(getattr(row, "order"), updated_value)
        self.assertNotEqual(getattr(row, "order"), original_value)

    def test_update_product(self):
        """verify product (ForeignKey) can be updated"""
        row = self.bake()
        original_value = row.product
        baker.make(self.model.product.field.related_model._meta.label, _fill_optional=True)
        if original_value:
            updated_value = random.choice(self.model.product.field.related_model.objects.exclude(pk=original_value.pk))
        else:
            updated_value = random.choice(self.model.product.field.related_model.objects.all())
        setattr(row, "product", updated_value)
        row.save()
        self.assertEqual(getattr(row, "product"), updated_value)
        self.assertNotEqual(getattr(row, "product"), original_value)


class OrderTests(TestCase):
    """test CRUD operations on Order"""

    def setUp(self):
        self.model = apps.get_model("storemgr", "order")
        self.to_bake = "storemgr.Order"
        self.logentry = apps.get_model("auditlog", "LogEntry")

    def bake(self):
        """add row"""
        return baker.make(
            self.to_bake,
        )

    def test_create(self):
        """verify object can be created"""
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)

    def test_create_auditlog(self):
        """verify an auditlog entry is created when new row is created"""
        row = self.bake()
        log = self.logentry.objects.filter(content_type__model=row._meta.model_name, object_pk=row.pk).latest("pk")
        self.assertIsNotNone(log)
        self.assertEqual(log.content_type.model, row._meta.model_name)
        self.assertEqual(log.object_pk, row.pk)
        self.assertEqual(log.action, 0)

    def test_read(self):
        """verify object can be read"""
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """verify object can be deleted"""
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)

    def test_delete_auditlog(self):
        """verify an auditlog entry is created when a row is deleted"""
        row = self.bake()
        object_repr = row.__str__()
        object_pk = row.pk
        row.delete()
        log = self.logentry.objects.filter(
            content_type__model=row._meta.model_name, object_repr__icontains=object_repr
        ).latest("pk")
        self.assertIsNotNone(log)
        self.assertEqual(log.content_type.model, row._meta.model_name)
        self.assertEqual(log.action, 2)

    def test_update_customer(self):
        """verify customer (ForeignKey) can be updated"""
        row = self.bake()
        original_value = row.customer
        baker.make(self.model.customer.field.related_model._meta.label, _fill_optional=True)
        if original_value:
            updated_value = random.choice(self.model.customer.field.related_model.objects.exclude(pk=original_value.pk))
        else:
            updated_value = random.choice(self.model.customer.field.related_model.objects.all())
        setattr(row, "customer", updated_value)
        row.save()
        self.assertEqual(getattr(row, "customer"), updated_value)
        self.assertNotEqual(getattr(row, "customer"), original_value)
        # verify auditlog entry
        log = self.logentry.objects.filter(content_type__model=row._meta.model_name, object_pk=row.pk).latest("pk")
        self.assertIsNotNone(log)
        self.assertEqual(log.content_type.model, row._meta.model_name)
        self.assertEqual(log.object_pk, row.pk)
        self.assertEqual(log.action, 1)

    def test_update_status(self):
        """verify status (ForeignKey) can be updated"""
        row = self.bake()
        original_value = row.status
        baker.make(self.model.status.field.related_model._meta.label, _fill_optional=True)
        if original_value:
            updated_value = random.choice(self.model.status.field.related_model.objects.exclude(pk=original_value.pk))
        else:
            updated_value = random.choice(self.model.status.field.related_model.objects.all())
        setattr(row, "status", updated_value)
        row.save()
        self.assertEqual(getattr(row, "status"), updated_value)
        self.assertNotEqual(getattr(row, "status"), original_value)
        # verify auditlog entry
        log = self.logentry.objects.filter(content_type__model=row._meta.model_name, object_pk=row.pk).latest("pk")
        self.assertIsNotNone(log)
        self.assertEqual(log.content_type.model, row._meta.model_name)
        self.assertEqual(log.object_pk, row.pk)
        self.assertEqual(log.action, 1)


class OrderStatusTests(TestCase):
    """test CRUD operations on OrderStatus"""

    def setUp(self):
        self.model = apps.get_model("storemgr", "orderstatus")
        self.to_bake = "storemgr.OrderStatus"

    def bake(self):
        """add row"""
        return baker.make(
            self.to_bake,
        )

    def test_create(self):
        """verify object can be created"""
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)

    def test_read(self):
        """verify object can be read"""
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """verify object can be deleted"""
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)

    def test_update_name(self):
        """verify name (CharField) can be updated"""
        row = self.bake()
        original_value = row.name
        updated_value = baker.prepare(self.to_bake, _fill_optional=["name"]).name
        setattr(row, "name", updated_value)
        row.save()
        self.assertEqual(getattr(row, "name"), updated_value)
        self.assertNotEqual(getattr(row, "name"), original_value)


class ProductTests(TestCase):
    """test CRUD operations on Product"""

    def setUp(self):
        self.model = apps.get_model("storemgr", "product")
        self.to_bake = "storemgr.Product"
        self.logentry = apps.get_model("auditlog", "LogEntry")

    def bake(self):
        """add row"""
        return baker.make(
            self.to_bake,
        )

    def test_create(self):
        """verify object can be created"""
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)

    def test_create_auditlog(self):
        """verify an auditlog entry is created when new row is created"""
        row = self.bake()
        log = self.logentry.objects.filter(content_type__model=row._meta.model_name, object_pk=row.pk).latest("pk")
        self.assertIsNotNone(log)
        self.assertEqual(log.content_type.model, row._meta.model_name)
        self.assertEqual(log.object_pk, row.pk)
        self.assertEqual(log.action, 0)

    def test_read(self):
        """verify object can be read"""
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """verify object can be deleted"""
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)

    def test_delete_auditlog(self):
        """verify an auditlog entry is created when a row is deleted"""
        row = self.bake()
        object_repr = row.__str__()
        object_pk = row.pk
        row.delete()
        log = self.logentry.objects.filter(
            content_type__model=row._meta.model_name, object_repr__icontains=object_repr
        ).latest("pk")
        self.assertIsNotNone(log)
        self.assertEqual(log.content_type.model, row._meta.model_name)
        self.assertEqual(log.action, 2)

    def test_update_brand(self):
        """verify brand (ForeignKey) can be updated"""
        row = self.bake()
        original_value = row.brand
        baker.make(self.model.brand.field.related_model._meta.label, _fill_optional=True)
        if original_value:
            updated_value = random.choice(self.model.brand.field.related_model.objects.exclude(pk=original_value.pk))
        else:
            updated_value = random.choice(self.model.brand.field.related_model.objects.all())
        setattr(row, "brand", updated_value)
        row.save()
        self.assertEqual(getattr(row, "brand"), updated_value)
        self.assertNotEqual(getattr(row, "brand"), original_value)
        # verify auditlog entry
        log = self.logentry.objects.filter(content_type__model=row._meta.model_name, object_pk=row.pk).latest("pk")
        self.assertIsNotNone(log)
        self.assertEqual(log.content_type.model, row._meta.model_name)
        self.assertEqual(log.object_pk, row.pk)
        self.assertEqual(log.action, 1)

    def test_update_description(self):
        """verify description (CharField) can be updated"""
        row = self.bake()
        original_value = row.description
        updated_value = baker.prepare(self.to_bake, _fill_optional=["description"]).description
        setattr(row, "description", updated_value)
        row.save()
        self.assertEqual(getattr(row, "description"), updated_value)
        self.assertNotEqual(getattr(row, "description"), original_value)
        # verify auditlog entry
        log = self.logentry.objects.filter(content_type__model=row._meta.model_name, object_pk=row.pk).latest("pk")
        self.assertIsNotNone(log)
        self.assertEqual(log.content_type.model, row._meta.model_name)
        self.assertEqual(log.object_pk, row.pk)
        self.assertEqual(log.action, 1)


class ProductAttributeTests(TestCase):
    """test CRUD operations on ProductAttribute"""

    def setUp(self):
        self.model = apps.get_model("storemgr", "productattribute")
        self.to_bake = "storemgr.ProductAttribute"

    def bake(self):
        """add row"""
        return baker.make(
            self.to_bake,
        )

    def test_create(self):
        """verify object can be created"""
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)

    def test_read(self):
        """verify object can be read"""
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """verify object can be deleted"""
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)

    def test_update_key(self):
        """verify key (CharField) can be updated"""
        row = self.bake()
        original_value = row.key
        updated_value = baker.prepare(self.to_bake, _fill_optional=["key"]).key
        setattr(row, "key", updated_value)
        row.save()
        self.assertEqual(getattr(row, "key"), updated_value)
        self.assertNotEqual(getattr(row, "key"), original_value)

    def test_update_value(self):
        """verify value (CharField) can be updated"""
        row = self.bake()
        original_value = row.value
        updated_value = baker.prepare(self.to_bake, _fill_optional=["value"]).value
        setattr(row, "value", updated_value)
        row.save()
        self.assertEqual(getattr(row, "value"), updated_value)
        self.assertNotEqual(getattr(row, "value"), original_value)
