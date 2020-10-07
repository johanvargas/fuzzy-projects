# postgreslqltutorial.com/postgresql-python/connect/

# First you must initial the postgres service
# postgres -D db/dir - in this case postgres_db/
# then you can run psql to enter databases.
# psql <databasename>

# (From postgresql documentation) Warning Never, never, NEVER use Python string concatenation (+) 
# or string parameters interpolation (%) to pass variables to a 
# SQL query string. Not even at gunpoint.

import psycopg2
from config import config

def connect():
	''' Connect to PostgreSQL db server '''
	
	conn = None

	try:
		params = config()
		print('Connecting to the PostgreSQL db...')
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		
		# get_version(cur)
		add_row(conn, cur, )

		# # select postgres version
		# print('PostgreSQL db version:')
		# cur.execute('SELECT version()')
		# db_version = cur.fetchone()
		# print(db_version)
		
		# # add row to item table 
		# cur.execute("INSERT INTO item (name, description, price, images, status) VALUES('Music Man Bass', '5-string black, Active Pickups', 200.00, 'no images yet', 'on sale');")
		# conn.commit()
		# print('Item added succesfully.')
		# cur.close()

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	finally:
		if conn is not None:
			conn.close()
			print('Database connection is closed.')

def get_version(cur):
		# select postgres version
		print('PostgreSQL db version:')
		cur.execute('SELECT version()')
		db_version = cur.fetchone()
		print(db_version)

def add_row(conn, cur, data):
		# add row to item table
		data = (data, )
		sql = "INSERT INTO item (name, description, price, images, status) VALUES(data);" 
		cur.execute(sql, data)
		conn.commit()
		print('Item added succesfully.')
		cur.close()
		
if __name__ == '__main__':
	connect() 