import psycopg2
from config import config

def update_data():
	''' Connect to PostgreSQL db server '''
	
	conn = None

	try:
		params = config()
		print('Connecting to the PostgreSQL db...')
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		
		# get_version(cur)
		update_row(conn, cur)

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	finally:
		if conn is not None:
			conn.close()
			print('Database connection is closed.')

def update_row(conn, cur):
	# update row (update)
	# UPDATE datacamp_courses SET course_name = 'Joining Data in SQL'
	# WHERE course_instructor = 'Chester Ismay';
	data = input('')
	row = 0
	cur.execute('UPDATE item SET description = %s WHERE name = ', (data, ))
	conn.commit()
	print('Item added succesfully.')
	cur.close()