from django.test import TestCase
from decouple import config

USER_ID = config('USER_ID', default='')
SECRET_KEY = config('SECRET_KEY', default='')

print(USER_ID, SECRET_KEY)

