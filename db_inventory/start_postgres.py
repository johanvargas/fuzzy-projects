import os

# Automation of postgres server startup
# Only for local dir, not portable.

def run_postgres_server(db):
	cd_to_documents = os.chdir('/Users/johanvargas/Documents')
	start = 'postgres -D postgres_db'

def main():
	run_postgres_server()

if __name__ == "__main__":
	main()