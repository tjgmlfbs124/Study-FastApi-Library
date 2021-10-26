from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DB 인스턴스, 다른 DB를 사용하는경우 수정해야하는 라인
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:emsys1001@localhost:3306/lab"

# SQLAlchemy 엔진. 다른곳에서 사용
# connect_args : SQLite에서만 필요. 다른 DB는 필요하지 않다.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# 클래스 자체는 아직 데이터베이스 세션이 아닌나, SessionLocal 인스턴스를 사용하는 순간 실제 데이터베이스의 세션이 된다.
# Session과 구분하기 위해, SessionLocal로 변수이름을 지었다.
# sessionMaker를 사용하는순간 클래스가 생성됨.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 나중에 이 클래스에서 상속하여 각 데이터베이스 모델 또는 클래스(ORM 모델)를 생성합니다.
Base = declarative_base()

def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()
