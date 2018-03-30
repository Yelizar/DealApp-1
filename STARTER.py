"""will be deleted"""
import os
import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DealApp.settings")
    django.setup()


import USER_CREATER, GOODS_CREATER


GOODS_CREATER.GoodsCreater()