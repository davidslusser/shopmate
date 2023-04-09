import django
import os
import random
from django.apps import apps
from django.test import TestCase
from model_bakery import baker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


class CustomerTests(TestCase):
    """test CRUD operations on Customer"""

    def setUp(self):
        self.model = apps.get_model("storemgr", "customer")
        self.to_bake = "storemgr.Customer"

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
        entry = self.model.objects.get(id=row.id)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.id, entry.id)

    def test_delete(self):
        """verify object can be deleted"""
        row = self.bake()
        before_count = self.model.objects.count()
        row_id = row.id
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(id=row_id)
        self.assertLess(after_count, before_count)

    def test_update_first_name(self):
        """verify first_name (CharField) can be updated"""
        row = self.bake()
        original_value = row.first_name
        updated_value = baker.prepare(
            self.to_bake, _fill_optional=["first_name"]
        ).first_name
        setattr(row, "first_name", updated_value)
        row.save()
        self.assertEqual(getattr(row, "first_name"), updated_value)
        self.assertNotEqual(getattr(row, "first_name"), original_value)

    def test_update_last_name(self):
        """verify last_name (CharField) can be updated"""
        row = self.bake()
        original_value = row.last_name
        updated_value = baker.prepare(
            self.to_bake, _fill_optional=["last_name"]
        ).last_name
        setattr(row, "last_name", updated_value)
        row.save()
        self.assertEqual(getattr(row, "last_name"), updated_value)
        self.assertNotEqual(getattr(row, "last_name"), original_value)


class OrderTests(TestCase):
    """test CRUD operations on Order"""

    def setUp(self):
        self.model = apps.get_model("storemgr", "order")
        self.to_bake = "storemgr.Order"

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
        entry = self.model.objects.get(id=row.id)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.id, entry.id)

    def test_delete(self):
        """verify object can be deleted"""
        row = self.bake()
        before_count = self.model.objects.count()
        row_id = row.id
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(id=row_id)
        self.assertLess(after_count, before_count)

    def test_update_customer(self):
        """verify customer (ForeignKey) can be updated"""
        row = self.bake()
        original_value = row.customer
        baker.make(
            self.model.customer.field.related_model._meta.label, _fill_optional=True
        )
        if original_value:
            updated_value = random.choice(
                self.model.customer.field.related_model.objects.exclude(
                    id=original_value.id
                )
            )
        else:
            updated_value = random.choice(
                self.model.customer.field.related_model.objects.all()
            )
        setattr(row, "customer", updated_value)
        row.save()
        self.assertEqual(getattr(row, "customer"), updated_value)
        self.assertNotEqual(getattr(row, "customer"), original_value)

    def test_update_product(self):
        """verify product (ForeignKey) can be updated"""
        row = self.bake()
        original_value = row.product
        baker.make(
            self.model.product.field.related_model._meta.label, _fill_optional=True
        )
        if original_value:
            updated_value = random.choice(
                self.model.product.field.related_model.objects.exclude(
                    id=original_value.id
                )
            )
        else:
            updated_value = random.choice(
                self.model.product.field.related_model.objects.all()
            )
        setattr(row, "product", updated_value)
        row.save()
        self.assertEqual(getattr(row, "product"), updated_value)
        self.assertNotEqual(getattr(row, "product"), original_value)

    def test_update_status(self):
        """verify status (ForeignKey) can be updated"""
        row = self.bake()
        original_value = row.status
        baker.make(
            self.model.status.field.related_model._meta.label, _fill_optional=True
        )
        if original_value:
            updated_value = random.choice(
                self.model.status.field.related_model.objects.exclude(
                    id=original_value.id
                )
            )
        else:
            updated_value = random.choice(
                self.model.status.field.related_model.objects.all()
            )
        setattr(row, "status", updated_value)
        row.save()
        self.assertEqual(getattr(row, "status"), updated_value)
        self.assertNotEqual(getattr(row, "status"), original_value)


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
        entry = self.model.objects.get(id=row.id)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.id, entry.id)

    def test_delete(self):
        """verify object can be deleted"""
        row = self.bake()
        before_count = self.model.objects.count()
        row_id = row.id
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(id=row_id)
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
        entry = self.model.objects.get(id=row.id)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.id, entry.id)

    def test_delete(self):
        """verify object can be deleted"""
        row = self.bake()
        before_count = self.model.objects.count()
        row_id = row.id
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(id=row_id)
        self.assertLess(after_count, before_count)

    def test_update_description(self):
        """verify description (CharField) can be updated"""
        row = self.bake()
        original_value = row.description
        updated_value = baker.prepare(
            self.to_bake, _fill_optional=["description"]
        ).description
        setattr(row, "description", updated_value)
        row.save()
        self.assertEqual(getattr(row, "description"), updated_value)
        self.assertNotEqual(getattr(row, "description"), original_value)


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
        entry = self.model.objects.get(id=row.id)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.id, entry.id)

    def test_delete(self):
        """verify object can be deleted"""
        row = self.bake()
        before_count = self.model.objects.count()
        row_id = row.id
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(id=row_id)
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
