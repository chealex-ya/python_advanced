import sqlalchemy

def datawriter(user_id, other_user_id, img1, img2, img3):
	engine = sqlalchemy.create_engine('postgresql://ruachaj:Tachamasib1@localhost:5432/chealex_db')
	with engine.connect() as connection:
		result = connection.execute(f"""INSERT INTO VKINDER (user_id, other_user_id, photo_1, photo_2, photo_3) values ({user_id},{other_user_id},{img1},{img2},{img3})""")