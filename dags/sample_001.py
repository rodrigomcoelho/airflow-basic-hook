from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from pendulum import timezone

with DAG(
    dag_id="sample_001",
    start_date=datetime(2023, 2, 1, tzinfo=timezone("America/Sao_Paulo")),
    catchup=False,
    default_args={
        "owner": "data.engineering",
    },
    schedule_interval="@daily",
) as dag:
    jobs = {
        "start": EmptyOperator(task_id="start"),
        "stop": EmptyOperator(task_id="stop"),
    }

    for task_id in ["task_001"]:
        jobs[task_id] = EmptyOperator(task_id=task_id)

        jobs[task_id].set_upstream(jobs["start"])
        jobs[task_id].set_downstream(jobs["stop"])
