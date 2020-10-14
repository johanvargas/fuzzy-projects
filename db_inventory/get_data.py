import psycopg2
from config import config

def get_data():
	''' Connect to PostgreSQL db server '''
	
	conn = None

	try:
		params = config()
		print('Connecting to the PostgreSQL db...')
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		
		# get_version(cur)
		get_single_row(conn, cur)

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	finally:
		if conn is not None:
			conn.close()
			print('Database connection is closed.')

def get_all_rows(conn, cur):
	# Get all rows and data
	cur.execute('SELECT * FROM item;')
	print("The number of parts: ", cur.rowcount)
	row = cur.fetchone()
	while row is not None:
		print(row)
		row = cur.fetchone()

	cur.close()

def get_single_row(conn, cur):
	# Get a single row from table, based on id.
	data = input('Select id: ')

	cur.execute('SELECT name FROM item WHERE id=%s', (data, ))
	row = cur.fetchone()
	print(row)

	cur.close()

# ALTER TABLE <tablename>
# 	ALTER <column> TYPE <new data type>

# \dt - to see all tables
# \d <tablename> to see columns and data types