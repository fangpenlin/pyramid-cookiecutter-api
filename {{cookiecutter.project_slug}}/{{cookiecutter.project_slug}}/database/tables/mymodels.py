from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import Unicode

from . import metadata
from ..enum import DeclEnum
from ..utc_dt import UTCDateTime
from ..guid_factory import GUIDFactory


class MyModelType(DeclEnum):
    TYPE1 = 'TYPE1', 'Type 1'
    TYPE2 = 'TYPE2', 'Type 2'


mymodels = Table(
    'mymodels',
    metadata,
    Column('guid', Unicode(64), primary_key=True, default=GUIDFactory('MD')),
    Column(
        'type',
        MyModelType.db_type(),
        nullable=False,
        index=True,
    ),
    Column(
        'created_at',
        UTCDateTime,
        nullable=False,
        default=UTCDateTime.utcnow,
    ),
    Column(
        'updated_at',
        UTCDateTime,
        nullable=False,
        default=UTCDateTime.utcnow,
        onupdate=UTCDateTime.utcnow,
    ),
)
