__author__ = 'agandra'

import sys, os.path, argparse, time, unicodedata, re, config
location = os.path.basename(sys.argv[0])

class SyncAction(argparse.Action):
		
	def __call__(self, parser, namespace, values, option_string=None):
		self.config = config.config
		
		if option_string == '-migration':
			try:
				call = getattr(self, 'migration_'+values[0])
				call(values[1:])
			except Exception:
				print 'Not a valid migration command, please consult help'
	
	def migration_create(self, values): 
		if len(values) == 1:
			now = int(time.time())

			slug = self.slugify(values[0])
			
			file = open('migrations/'+str(now)+'-'+slug,'w+')
			file.close()
		else:
			print 'Please pass file description as one arugment'
			
	def migration_sync(self, values):
		type = self.config['type']
		sys.path.append('./drivers')
		driver = __import__('Sync'+type)
		dbo = getattr(driver, 'Sync'+type)
		dbo(self.config).sync()
		
	def slugify(self, value):
		s = unicode(value)
		slug = unicodedata.normalize('NFKD', s)
		slug = slug.encode('ascii', 'ignore').lower()
		slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
		slug = re.sub(r'[-]+', '-', slug)
		return slug
		
if __name__=="__main__":
	if len(sys.argv) > 0:
		parser = argparse.ArgumentParser(description='DB Syncing script')
		parser.add_argument('-migration', nargs='*', action=SyncAction, help='Migration commands - create or sync')
		parser.parse_args()
	else:
		print 'Not a valid command, please consult help'
			
		