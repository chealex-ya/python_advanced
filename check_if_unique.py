import sqlalchemy

def check(id):
	engine = sqlalchemy.create_engine('postgresql://ruachaj:Tachamasib1@localhost:5432/chealex_db')
	with engine.connect() as connection:
		sel = connection.execute(f"""SELECT other_user_id FROM VKINDER""").fetchall()

	for i in sel:
		y =  i[0]
		if id == y:
			return True
		else:
			return False

