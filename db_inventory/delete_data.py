import psycopg2
from config import config

def delete_data():
	''' Connect to PostgreSQL db server '''
	
	conn = None

	try:
		params = config()
		print('Connecting to the PostgreSQL db...')
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		
		# get_version(cur)
		delete_row(conn, cur)

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	finally:
		if conn is not None:
			conn.close()
			print('Database connection is closed.')

def delete_row(conn, cur):
	# delete row (delete)
	# DELETE from datacamp_courses
	# WHERE course_name = 'Deep Learning in Python';
	data= ''
	cur.execute('DELETE from item WHERE id=%s', (data, ))
	conn.commit()
	print('Item deleted succesfully.')
	cur.close()