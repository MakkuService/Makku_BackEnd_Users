from django.test import TestCase

# Create your tests here.
from django.conf import settings

settings.configure()
sc = settings.SECRET_KEY
print(sc)