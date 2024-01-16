# myapp/management/commands/create_dynamic_table.py

from django.core.management.base import BaseCommand
from excel_api.utils import create_dynamic_table

class Command(BaseCommand):
    help = 'Create dynamic table'

    def handle(self, *args, **options):
        data = [
            {'Name': 'John', 'Age': 25, 'IsStudent': True},
            {'Name': 'Jane', 'Age': 30, 'IsStudent': False},
        ]
        create_dynamic_table('DynamicTable', data)
        self.stdout.write(self.style.SUCCESS('Dynamic table created successfully.'))
