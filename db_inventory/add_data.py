import psycopg2
from config import config

def add_data():
	''' Connect to PostgreSQL db server '''
	
	conn = None

	try:
		params = config()
		print('Connecting to the PostgreSQL db...')
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		
		# get_version(cur)
		add_row(conn, cur)

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	finally:
		if conn is not None:
			conn.close()
			print('Database connection is closed.')

def add_row(conn, cur):
	# INSERT (create)
	# add row to item table
	data = ''
	cur.execute('INSERT INTO item (name, description, price, images, status) VALUES (%s)', (data, ))
	conn.commit()
	print('Item added succesfully.')
	cur.close()