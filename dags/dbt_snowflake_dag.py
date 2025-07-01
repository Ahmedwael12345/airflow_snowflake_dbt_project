from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "ahmedwael",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="dbt_snowflake_workflow",
    default_args=default_args,
    description="Run dbt transformations on Snowflake using Airflow",
    schedule_interval=None,
    start_date=datetime(2024, 6, 24),
    catchup=False,
    tags=["dbt", "snowflake"],
) as dag:

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /opt/airflow/dbt/snowflake_data_project && dbt run"
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /opt/airflow/dbt/snowflake_data_project && dbt test"
    )



    dbt_run >> dbt_test
