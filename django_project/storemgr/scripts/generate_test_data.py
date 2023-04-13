import sys
import os
import traceback
import argparse
import logging
import datetime
import django
import environ
import random


__version__ = "0.0.1"

__doc__ = """ Script for generating database entries for test purposes. """

# setup django
sys.path.append(str(environ.Path(__file__) - 3))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

# import models
from django.contrib.auth.models import Group, User
from storemgr.models import Brand, Customer, Order, OrderStatus, Product, ProductAttribute


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


def create_brands():
    """add some brands to the database"""
    data_list = [
        {"name": "CuperSool"},
        {"name": "ChillLife"},
        {"name": "Ironic"},
        {"name": "NewWorld"},
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


def get_random_first_name():
    """get a random first name"""
    name_list = [
        "Alan",
        "Amber",
        "Brandon",
        "Barbara",
        "Charlie",
        "Candice",
        "Dan",
        "Diane",
        "Edward",
        "Elena",
        "Grant",
        "Gale",
        "Henry",
        "Heather",
        "Ian",
        "Ingrid",
        "Jack",
        "Jill",
        "Kim",
        "Ken",
        "Larry",
        "Lisa",
        "Mark",
        "Margret",
        "Nate",
        "Nancy",
        "Peter",
        "Patricia",
        "Walter",
        "Wilma",
    ]
    return random.choice(name_list)


def get_random_last_name():
    """get a random last name"""
    name_list = [
        "Smith",
        "Jones",
        "Kim",
        "Martin",
        "Black",
        "Yee",
        "House",
        "Johnson",
        "Williams",
        "Brown",
        "Garcia",
        "Miller",
        "Davis",
    ]
    return random.choice(name_list)


def get_random_domain():
    """get a random domain to use in an email address"""
    domain_list = ["blah.nat", "bork.io", "totallynotfake.nope", "working.bug", "foo.bar"]
    return random.choice(domain_list)


def create_customers(qty=1):
    """add some customer entries to the database"""
    for i in range(qty):
        first_name = get_random_first_name()
        last_name = get_random_last_name()
        email_options_list = [
            f"{first_name}.{last_name}",
            f"{first_name[0]}{last_name}",
            f"{last_name}_{first_name[0]}",
            f"{first_name}{last_name[0]}",
        ]
        email = f"{random.choice(email_options_list)}@{get_random_domain()}"
        data = dict(first_name=first_name, last_name=last_name, email=email)
        Customer.objects.get_or_create(**data, defaults=data)


def create_orders(qty=1):
    """add some order entries to the database"""
    for i in range(qty):
        order = Order.objects.create(
            status=OrderStatus.objects.get_random_row(),
            customer=Customer.objects.get_random_row(),
        )
        for i in range(random.randint(1, 4)):
            order.products.add(Product.objects.get_random_row())


def generate_test_data():
    """generate some data for testing purposes"""
    create_users_and_groups()
    create_product_attributes()
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
