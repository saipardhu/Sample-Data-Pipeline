from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
    return 'Hello world!'

dag = DAG('hello_world', description='Simple tutorial DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

#dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

#hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

#dummy_operator >> hello_operator

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

