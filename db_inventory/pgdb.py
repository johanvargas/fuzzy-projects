# postgreslqltutorial.com/postgresql-python/connect/

# First you must initial the postgres service
# postgres -D db/dir - in this case postgres_db/
# then you can run psql to enter databases.
# psql <databasename>

# (From postgresql documentation) Warning Never, never, NEVER use Python string concatenation (+) 
# or string parameters interpolation (%) to pass variables to a 
# SQL query string. Not even at gunpoint.

# only working with one table, inventory, right now
# this all needs to be transfered to a html doc for human friendly display

import psycopg2
from config import config

def get_version(cur):
		# select postgres version
		print('PostgreSQL db version:')
		cur.execute('SELECT version()')
		db_version = cur.fetchone()
		print(db_version)

# INSERT (create)
def add_row(conn, cur, data):
		# add row to item table
		sql = f"INSERT INTO item (name, description, price, images, status) VALUES{data};" 
		cur.execute(sql, data)
		conn.commit()
		print('Item added succesfully.')
		cur.close()

# Get row data (read)
def get_row():
	pass

# update row (update)
# UPDATE datacamp_courses SET course_name = 'Joining Data in SQL'
# WHERE course_instructor = 'Chester Ismay';

def update_row():
	pass

# delete row (delete)
# DELETE from datacamp_courses
# WHERE course_name = 'Deep Learning in Python';

def delete_row():
	pass

def connect():
	''' Connect to PostgreSQL db server '''
	
	conn = None

	try:
		params = config()
		print('Connecting to the PostgreSQL db...')
		conn = psycopg2.connect(**params)
		cur = conn.cursor()

		data = 'Darth Vader Action Figure', '3 1\2 inch, missing weapons', 100.00, 'no images yet', 'on sale'
		
		# get_version(cur)
		add_row(conn, cur, data)

		###### Direct Examples - don't use, use the functions for each of the CRUD methods #######
		# # select postgres version
		# print('PostgreSQL db version:')
		# cur.execute('SELECT version()')
		# db_version = cur.fetchone()
		# print(db_version)
		
		# # add row to item table 
		# cur.execute("INSERT INTO item (name, description, price, images, status) VALUES('Darth Vader Action Figure', '3 1\\2 inch, missing weapons', 100.00, 'no images yet', 'on sale');")
		# conn.commit()
		# print('Item added succesfully.')
		# cur.close()
		####### END ##################

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	finally:
		if conn is not None:
			conn.close()
			print('Database connection is closed.')
		
if __name__ == '__main__':
	connect() 