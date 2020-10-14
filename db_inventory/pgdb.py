# postgreslqltutorial.com/postgresql-python/connect/

# First you must initial the postgres service
# postgres -D db/dir - in this case postgres_db/
# then you can run psql to enter databases.
# psql <databasename>

# (From postgresql documentation) Warning Never, never, NEVER use Python string concatenation (+) 
# or string parameters interpolation (%) to pass variables to a 
# SQL query string. Not even at gunpoint.

# only working with one table, item, right now
# this all needs to be transfered to a html doc for human friendly display
# These are all 'provisional' sql functions, until I have a better model,
# or until I decide to completely shift to Django/PostGreSQL

import psycopg2
from config import config

def get_version(cur):
		# select postgres version
		print('PostgreSQL db version:')
		cur.execute('SELECT version()')
		db_version = cur.fetchone()
		print(db_version)


def add_row(conn, cur):
	# INSERT (create)
	# add row to item table
	data = 'Princess Leia', '3 inches, Obiwone Plea Outfit', 234.60, 'no images yet', 'on sale'
	sql = f'INSERT INTO item (name, description, price, images, status) VALUES {data}'
	cur.execute(sql, data)
	conn.commit()
	print('Item added succesfully.')
	cur.close()


def get_row(conn, cur):
	# Get row data (read), based on id number
	data = input('Select an ID number: ')

	sql = ('SELECT * FROM item WHERE id=%s', (data,))
	cur.execute(sql, data)
	conn.commit()
	print('Item added succesfully.')
	cur.close()


def update_row(conn, cur):
	# update row (update)
	# UPDATE datacamp_courses SET course_name = 'Joining Data in SQL'
	# WHERE course_instructor = 'Chester Ismay';
	data = ''
	row = 0
	sql = f'UPDATE item SET description={data} WHERE id={row}'
	cur.execute(sql, data)
	conn.commit()
	print('Item added succesfully.')
	cur.close()


def delete_row(conn, cur):
	# delete row (delete)
	# DELETE from datacamp_courses
	# WHERE course_name = 'Deep Learning in Python';
	data= ''
	sql = f'DELETE from item WHERE id={data}'
	cur.execute(sql, data)
	conn.commit()
	print('Item deleted succesfully.')
	cur.close()


def connect():
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