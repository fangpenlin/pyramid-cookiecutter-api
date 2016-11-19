import uuid

import base58


class GUIDFactory(object):
    """Object for making prefixed GUID

    """

    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self):
        return self.prefix + base58.b58encode(uuid.uuid4().bytes)
