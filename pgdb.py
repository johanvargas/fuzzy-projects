# postgreslqltutorial.com/postgresql-python/connect/

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
		print('PostgreSQL db version:')
		cur.execute('SELECT version()')
		db_version = cur.fetchone()
		print(db_version)
		cur.close()


	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	finally:
		if conn is not None:
			conn.close()
			print('Database connection is closed.')

if __name__ == '__main__':
	connect() 