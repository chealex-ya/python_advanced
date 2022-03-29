import sqlalchemy
import json

def datawriter():
	engine = sqlalchemy.create_engine('postgresql://ruachaj:Tachamasib1@localhost:5432/chealex_db')
	with open('data.json', 'r') as f:
		data = json.load(f)
		a = "'"
		b = "'"
		photo1 = str(data['links'][0])
		photo2 = str(data['links'][1])
		photo3 = str(data['links'][2])
		res_str1 = "%s %s %s" % (a, photo1, b)
		res_str2 = "%s %s %s" % (a, photo2, b)
		res_str3 = "%s %s %s" % (a, photo3, b)
		with engine.connect() as connection:
			result = connection.execute(f"""INSERT INTO VKINDER (user_id, other_user_id, photo_1, photo_2, photo_3) values ({data['user_id']},{data['other_user_id']}, {res_str1}, {res_str2}, {res_str3})""")