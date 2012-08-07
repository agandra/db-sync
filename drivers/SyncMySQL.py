import MySQLdb
class SyncMySQL:

	def __init__(self, config):
		self.config = config
		self.db = MySQLdb.connect(config['host'], config['username'], config['password'], config['db']) 
		
	def sync(self):
		cursor = self.db.cursor()
		cursor.execute("SELECT * FROM hotels")
		rows = cursor.fetchall()
		
		for row in rows:
			print row
		
		self.db.close()