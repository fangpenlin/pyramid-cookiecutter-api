from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import object_session


class Model(object):

    def __repr__(self):
        columns = self.__mapper__.c.keys()
        class_name = self.__class__.__name__
        items = ', '.join([
            '%s=%s' % (col, repr(getattr(self, col))) for col in columns
        ])
        return '%s(%s)' % (class_name, items)

    @property
    def session(self):
        return object_session(self)


Base = declarative_base(cls=Model)
