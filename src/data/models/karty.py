from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime

from ..database import db
from ..mixins import CRUDModel

class karty(CRUDModel):
    __tablename__ = 'karty'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    CISLO_KARTY = Column(String, nullable=False, index=False)
    TIME = Column(DateTime, nullable=False)
    WTIME= Column(DateTime, nullable=False)



    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        self.WTIME = datetime.utcnow()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
    @staticmethod
    def find_by_CISLO_KARTY(CISLO_KARTY):
        return db.session.query(karty).filter_by(CISLO_KARTY  = CISLO_KARTY).all()

