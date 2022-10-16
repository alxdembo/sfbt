from time import sleep

import boto3


class Materialized:
    def __init__(self, database, catalog, s3_data_dir, s3_staging_dir, name):
        self.database = database
        self.catalog = catalog
        self.name = name
        self.s3_data_dir = s3_data_dir
        self.s3_staging_dir = s3_staging_dir
        self.bucket = self.s3_data_dir[5:].split('/')[0]

    def run_query(self, query):
        client = boto3.client('athena')

        query_start = client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={'Database': self.database, 'Catalog': self.catalog},
            ResultConfiguration={'OutputLocation': self.s3_staging_dir})

        for i in range(1, 100):
            query_execution = client.get_query_execution(QueryExecutionId=query_start['QueryExecutionId'])
            finish_state = query_execution['QueryExecution']['Status']['State']

            if finish_state == 'RUNNING' or finish_state == 'QUEUED':
                sleep(i)
            else:
                break

    def materialized_table(self, query):
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(self.bucket)
        bucket.objects.filter(Prefix=self.s3_data_dir).delete()

        self.run_query(f'drop table {self.name};')

        ctas = f'''
        create table {self.name}
        with (external_location = self.s3_data_dir, format='parquet') as {query};
        '''

        self.run_query(ctas)

    def materialized_view(self, query):
        self.run_query(f'create or replace view as {self.name}')


def lambda_handler(event, context):
    node = event['node']
    s3_staging_dir = event['s3_staging_dir']
    s3_data_dir = event['s3_data_dir']
    compiled_sql = event['compiled_sql']

    name = node['name']
    database = node['database']
    catalog = node['catalog']
    materialized = node['config']['materialized']

    m = Materialized(database, catalog, s3_data_dir, s3_staging_dir, name)

    match materialized:
        case 'table':
            m.materialized_table(compiled_sql)
        case 'view':
            m.materialized_table(compiled_sql)
        case _:
            raise NotImplemented

    return event
