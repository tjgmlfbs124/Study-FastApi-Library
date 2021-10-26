from sqlalchemy import Column
from sqlalchemy.types import INT, VARCHAR, TEXT, DATETIME, FLOAT
from db.databases import Base

class Farm(Base):
    __tablename__ = "farm"

    id = Column(INT, primary_key=True, autoincrement=True, nullable=False, unique=True)
    farmname = Column(TEXT, default="")
    phone = Column(VARCHAR(50), default="")
    # owner = Column(VARCHAR(50), default="")
    # volume= Column(TEXT, default="")
    # total_volume = Column(VARCHAR(50), default="")
    # address = Column(TEXT, default="")
    # info = Column(TEXT, default="")
    # sow_vol = Column(INT, default=0)
    # gilt_vol = Column(INT, default=0)
    # piglet_vol = Column(INT, default=0)
    # porker_vol = Column(INT, default=0)
    # type = Column(INT, default=0)
    # address1 = Column(VARCHAR(50), default="")
    # address2 = Column(VARCHAR(50), default="")
    # address3 = Column(VARCHAR(50), default="")
    # address4 = Column(VARCHAR(50), default="")
    # farmtype = Column(VARCHAR(11), default="")
    # fodder_company = Column(VARCHAR(255), default="")
    # additives_kind = Column(VARCHAR(250), default="")
    # additives_period = Column(VARCHAR(250), default="")
    # disposal_of_excreata = Column(VARCHAR(250), default="")
    # registered = Column(DATETIME, default="")
    # updated = Column(DATETIME, default="")
    # line = Column(INT, default="")
    # latitude = Column(FLOAT, default="")
    # longitude = Column(FLOAT, default="")
    # farm_unique_no = Column(VARCHAR(10), default="")


