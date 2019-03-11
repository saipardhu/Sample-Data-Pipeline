from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators import SimpleHttpOperator, HttpSensor, EmailOperator, BashOperator, PythonOperator
#import datetime

def print_hello():
    return 'Hello world!'

dag = DAG('Sample_Test', description='Data Pipeline Application',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), catchup=False)


d = datetime.today()
date = d.strftime('%d-%m-%Y')

ingest = BashOperator(
   task_id='Ingestion_from_S3',
   bash_command='python /home/ec2-user/get_s3data.py',
   dag=dag
 )


#transform = BashOperator(
#   task_id='Data_Preparation',
#   bash_command='',
#   dag=dag
# )

insert = BashOperator(task_id='Data_to_SQL',
    bash_command='bash /home/ec2-user/insert_to_sql.sh',
    dag=dag
 )

#ingest>>transform>>insert
ingest>>insert
