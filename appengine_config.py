from google.appengine.ext import ndb
from google.appengine.ext import vendor
import os

vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'backend/lib'))
context = ndb.get_context()
context.set_cache_policy(lambda key: False)
context.set_memcache_policy(lambda key: False)
