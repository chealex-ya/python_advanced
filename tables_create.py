import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


engine = sqlalchemy.create_engine('postgresql://ruachaj:Tachamasib1@localhost:5432/chealex_db')
engine
connection = engine.connect()

connection.execute("""
CREATE TABLE if not exists VKINDER
(ID serial primary key, user_id integer, other_user_id integer, photo_1 varchar(1000),
photo_2 varchar(1000), photo_3 varchar(1000)
);
""")

# Base = declarative_base()
#
# class Recommendations(Base):
# 	id = Column(Integer, primary_key=True)
# 	user_id = Column(Integer)
# 	other_user_id = Column(Integer)
# 	__tablename__ = 'vkinder'
#
# class UserPictures(Base, Image):
#
# 	user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
# 	user = relationship('Recommendations')
# 	photo_1 = Column(LargeBinary, nullable=True)
# 	photo_2 = Column(LargeBinary, nullable=True)
# 	photo_3 = Column(LargeBinary, nullable=True)
# 	__tablename__ = 'vkinder_pictures'




