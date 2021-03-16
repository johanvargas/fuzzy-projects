import psycopg2
from config import config

def add_data(data):
	''' Connect to PostgreSQL db server ''' 
	conn = None

	try:
		params = config()
		print('Connecting to the PostgreSQL db...')
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		
		# get_version(cur)
		add_row(conn, cur, data)

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	finally:
		if conn is not None:
			conn.close()
			print('Database connection is closed.')

def add_row(conn, cur, data):
	# INSERT (create)
	# add row to item table
	# data = 'Wolverine','Marvel Comic/ Hulk 181', 2000.00,'No Image Available','On Sale'
	data_inner = data[0], data[1], data[2], data[3], data[4]
	cur.execute('INSERT INTO item (name, description, price, images, status) VALUES %s', (data_inner, ))

	# cur.execute('INSERT INTO item (name, description, price, images, status) VALUES (%s)', (data, )), prob a safer means of inserting data, safety first!
	conn.commit()
	print('Item added succesfully.')
	cur.close()