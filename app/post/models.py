from sqlalchemy import Integer, String, TEXT
from sqlalchemy.sql.schema import Column

from ..database import Base

class Post(Base):
    __tablename__ = 'post'

    post_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(TEXT)
    content = Column(String)