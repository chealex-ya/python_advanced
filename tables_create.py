import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship


engine = sqlalchemy.create_engine('postgresql://ruachaj:Tachamasib1@localhost:5432/chealex_db')
engine
connection = engine.connect()

connection.execute("""
CREATE TABLE if not exists VKINDER
(ID serial primary key, user_id integer, other_user_id integer, photo_1 varchar(1000),
photo_2 varchar(1000), photo_3 varchar(1000)
);
""")






