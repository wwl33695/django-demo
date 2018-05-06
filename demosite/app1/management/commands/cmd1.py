from django.core.management.base import BaseCommand,CommandError
import time

class Command(BaseCommand):
	def handle(self, *args, **options):
		while True:
			print "cmd1 is running"
			time.sleep(3)