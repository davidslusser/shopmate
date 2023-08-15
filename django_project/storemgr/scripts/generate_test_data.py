import sys
import os
import traceback
import argparse
import logging
import datetime
import django
import environ
import random

from faker import Faker


__version__ = "0.0.1"

__doc__ = """Script for generating database entries for test purposes."""


# setup django
sys.path.append(str(environ.Path(__file__) - 3))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

# import models
from django.contrib.auth.models import Group, User
from storemgr.models import Brand, Customer, Invoice, Manufacturer, Order, OrderStatus, Product, ProductAttribute


def get_opts():
    """Return an argparse object."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        "--verbose",
        default=logging.INFO,
        action="store_const",
        const=logging.DEBUG,
        help="enable debug logging",
    )
    parser.add_argument("--version", action="version", version=__version__, help="show version and exit")
    parser.add_argument(
        "--clean",
        action="store_true",
        required=False,
        help="delete existing database entries",
    )
    args = parser.parse_args()
    logging.basicConfig(level=args.verbose)
    return args


def create_users_and_groups():
    """add some user and group entries to the database"""
    group_map = {
        "admin": ["admin", "Lisa", "David", "Sara"],
        "product_managers": ["Lisa", "Bob", "Janet", "Roy"],
        "orderers": ["Alex", "Deanna", "Roy"],
    }
    for group_name, user_list in group_map.items():
        group = Group.objects.get_or_create(name=group_name)[0]
        for user_name in user_list:
            user = User.objects.get_or_create(username=user_name, defaults=dict(username=user_name, password="app123"))[
                0
            ]
            user.groups.add(group)
            if group_name in ["admin"]:
                user.is_superuser = True
                user.is_staff = True
            user.save()


def create_manufacturers():
    data_list = [
        {"name": "Acme"},
        {"name": "Equity"},
        {"name": "Mega"},
        {"name": "WorldWide"},
    ]
    for data in data_list:
        Manufacturer.objects.get_or_create(**data, defaults=data)


def create_brands():
    """add some brands to the database"""
    data_list = [
        {"name": "CuperSool", "manufacturer": Manufacturer.objects.get_random_row()},
        {"name": "ChillLife", "manufacturer": Manufacturer.objects.get_random_row()},
        {"name": "Dunno", "manufacturer": Manufacturer.objects.get_random_row()},
        {"name": "Ironic", "manufacturer": Manufacturer.objects.get_random_row()},
        {"name": "Justify", "manufacturer": Manufacturer.objects.get_random_row()},
        {"name": "MakeMe", "manufacturer": Manufacturer.objects.get_random_row()},
        {"name": "NewWorld", "manufacturer": Manufacturer.objects.get_random_row()},
    ]
    for data in data_list:
        Brand.objects.get_or_create(**data, defaults=data)


def create_product_attributes():
    """add some product attributes to the database"""
    data_list = [
        {"key": "size", "value": "small"},
        {"key": "size", "value": "medium"},
        {"key": "size", "value": "large"},
        {"key": "color", "value": "blue"},
        {"key": "color", "value": "green"},
        {"key": "color", "value": "red"},
        {"key": "color", "value": "purple"},
        {"key": "color", "value": "black"},
        {"key": "color", "value": "white"},
        {"key": "style", "value": "formal"},
        {"key": "style", "value": "casual"},
        {"key": "style", "value": "retro"},
        {"key": "style", "value": "business"},
    ]
    for data in data_list:
        ProductAttribute.objects.get_or_create(**data, defaults=data)


def create_products(qty=1):
    """add some product entries to the database"""
    item_list = [
        "shirt",
        "jacket",
        "hat",
        "sweater",
        "pants",
        "dress",
        "scarf",
        "skirt",
        "vest",
    ]

    # for item in item_list:
    for i in range(qty):
        item = random.choice(item_list)
        color = ProductAttribute.objects.get_random_row(key="color")
        size = ProductAttribute.objects.get_random_row(key="size")
        style = ProductAttribute.objects.get_random_row(key="style")
        description = f"{item}; {color.value}; size {size.value}"
        product = Product.objects.create(brand=Brand.objects.get_random_row(), description=description)
        product.attributes.add(color, size, style)
        product.save()


def create_order_statuses():
    """add order status to the database"""
    data_list = [
        {"name": "created"},
        {"name": "processing"},
        {"name": "shipped"},
        {"name": "cancelled"},
        {"name": "hold"},
    ]
    for data in data_list:
        OrderStatus.objects.get_or_create(**data, defaults=data)

def create_customers(qty=1):
    """add some customer entries to the database"""
    fake = Faker()
    for _ in range(qty):
        profile = fake.simple_profile()
        data = dict(first_name=profile["name"].split()[0], last_name=profile["name"].split()[1], email=profile["mail"])
        Customer.objects.get_or_create(**data, defaults=data)


def create_orders(qty=1):
    """add some order entries to the database"""
    for i in range(qty):
        order = Order.objects.create(
            status=OrderStatus.objects.get_random_row(),
            customer=Customer.objects.get_random_row(),
        )
        # randomize order created_at 
        order.created_at = order.created_at - datetime.timedelta(days=random.randint(0, 365))
        order.save()

        # add products to order
        for j in range(random.randint(1, 4)):
            Invoice.objects.create(order=order, product=Product.objects.get_random_row())
            # order.products.add(Product.objects.get_random_row())
    

def generate_test_data():
    """generate some data for testing purposes"""
    create_users_and_groups()
    create_product_attributes()
    create_manufacturers()
    create_brands()
    create_products(30)
    create_customers(10)
    create_order_statuses()
    create_orders(200)


def clean():
    """delete all prior data"""
    Order.objects.all().delete()
    Product.objects.all().delete()
    ProductAttribute.objects.all().delete()
    OrderStatus.objects.all().delete()


def main():
    """script entry point"""
    try:
        opts = get_opts()
        start = datetime.datetime.now()
        if opts.clean:
            clean()
        generate_test_data()
        end = datetime.datetime.now()
        logging.info(f"script completed in: {end - start}")
    except Exception as err:
        logging.error(err)
        traceback.print_exc()
        return 255


if __name__ == "__main__":
    sys.exit(main())
