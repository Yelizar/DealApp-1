"""delete when site will be finished"""
import os
import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DealApp.settings")
    django.setup()


import USER_CREATER


quantity = 50
USER_CREATER.UserCreater(quantity)
