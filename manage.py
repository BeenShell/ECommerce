"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
execute_from_command_line(sys.argv)