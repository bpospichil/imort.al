#!/usr/bin/python2

from mongoengine import *
from datetime import datetime
import string
import random

def create_token(size=6):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(size))



class Entry(Document):
    active = BooleanField(required=True, default=True)
    confiable = BooleanField(required=True, default=False)
    short_url = StringField(max_length=20, required=True, unique=True, default=create_token(6))
    admin_token = StringField(max_length=10, required=True, default=create_token(5))
    long_url = URLField(required=True)
    owner = EmailField(required=False)
    last_use = DateTimeField(required=False)
    creation = DateTimeField(default=datetime.now)


