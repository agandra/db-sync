from subprocess import Popen, PIPE
import MySQLdb
import os

class SyncMySQL:

	def __init__(self, config):
		self.config = config
		self.db = MySQLdb.connect(config['host'], config['username'], config['password'], config['db']) 
		
	def sync(self):
		cursor = self.db.cursor()
		rows = []
		try:
			cursor.execute("SELECT * FROM `db-sync`")
			rows = cursor.fetchall()
		except Exception, e:
			self._createTable(cursor)

		for row in rows:
			print row
		
		self.db.close()

	def _createTable(self, cursor):
		cursor.execute("""
							CREATE TABLE IF NOT EXISTS `db-sync` (
							  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
							  `added` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
							  `name` varchar(260) NOT NULL DEFAULT '',
							  PRIMARY KEY (`id`)
							) ENGINE=InnoDB DEFAULT CHARSET=utf8;
						""")