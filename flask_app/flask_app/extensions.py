# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_bcrypt import Bcrypt
from flask_caching import Cache
from spectree import SpecTree

bcrypt = Bcrypt()
cache = Cache()
api_spec = SpecTree("flask")
