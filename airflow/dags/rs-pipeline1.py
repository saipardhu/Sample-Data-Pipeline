"""
Code that goes along with the Airflow tutorial located at:
https://github.com/apache/airflow/blob/master/airflow/example_dags/tutorial.py
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'saipardhu',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'schedule_interval': '10 0 * * *',
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('Rescale',description='Rescale Data Pipeline Application', default_args=default_args, schedule_interval=timedelta(days=1))

ingest = BashOperator(
   task_id='Ingestion_from_S3',
   bash_command='python /home/ec2-user/get_s3data.py',
   dag=dag
 )

insert = BashOperator(
    task_id='Data_to_SQL',
    bash_command='/home/ec2-user/insert_to_sql.sh ',
    dag=dag
 )


insert.set_upstream(ingest)
