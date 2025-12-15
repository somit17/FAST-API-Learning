from sqlalchemy import Column,Integer,String
from database import Base

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    description = Column(String)