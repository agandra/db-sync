__author__ = 'agandra'

import sys, os.path, argparse
location = os.path.basename(sys.argv[0])

class SyncAction(argparse.Action):
	def __call__(self, parser, namespace, values, option_string=None):
		if option_string == '-migration':
			if values == 0:
				print 'Not a valid migration command'
			else:
				try:
					call = getattr(self, 'migration_'+values[0])
					call(values)
				except Exception:
					print 'Not a valid migraiton command, please consult help'
	
	def migration_create(self, values): 
		print values
		
if __name__=="__main__":
	if len(sys.argv) > 0:
		parser = argparse.ArgumentParser(description='DB Syncing script')
		parser.add_argument('-migration', nargs='*', default=0, action=SyncAction, help='Migration commands')
		parser.parse_args()
	else:
		print 'Not a valid command, please consult help'
			
		