from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'ahmed',
    'depends_on_past': False,
    'start_date': datetime(2024, 6, 20),
    'retries': 1,
    'retry_delay': timedelta(minutes=3),
}

dag = DAG(
    'dbt_snowflake_pipeline',
    default_args=default_args,
    description='Run dbt models against Snowflake',
    schedule_interval='@daily',
    catchup=False,
)

# ✅ Update this to your actual DBT project directory
DBT_DIR = "/Users/ahmedwael/Documents/dbt-snowflacke/snowfalke_data_project"

dbt_run = BashOperator(
    task_id='run_dbt',
    bash_command=f'cd {DBT_DIR} && dbt run',
    dag=dag,
)

dbt_test = BashOperator(
    task_id='test_dbt',
    bash_command=f'cd {DBT_DIR} && dbt test',
    dag=dag,
)

dbt_run >> dbt_test
