import sqlite3

import pandas as pd
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Load Autonomous System data into the database'

    def handle(self, *args, **kwargs):
        # Connection to SQLite database
        conn = sqlite3.connect('db.sqlite3')

        # Loading TSV data into a pandas DataFrame
        df = pd.read_csv('ip2asn-combined.tsv', delimiter='\t', header=None, 
                        names=['range_start', 'range_end', 'as_number', 'country_code', 'as_description'])

        # Insert the DataFrame into the SQLite table
        df.to_sql('as_info', conn, if_exists='append', index=False)

        # Create an index for quick lookups on range_start and range_end
        conn.execute('CREATE INDEX idx_range_start ON as_info(range_start)')
        conn.execute('CREATE INDEX idx_range_end ON as_info(range_end)')
        conn.execute('CREATE INDEX idx_as_number ON as_info(as_number)')

        # Commit changes and close the connection
        conn.commit()
        conn.close()

        # print('Successfully loaded IPtoASN data')
        self.stdout.write(self.style.SUCCESS('Successfully loaded IPtoASN data'))
