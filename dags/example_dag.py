from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Definir a função de exemplo que será executada na DAG
def minha_tarefa():
    print("Essa é uma tarefa de exemplo no Airflow!")

# Configurar a DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'exemplo_dag',
    default_args=default_args,
    description='Uma DAG de exemplo',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['exemplo'],
) as dag:

    # Definir uma tarefa com o PythonOperator
    tarefa_exemplo = PythonOperator(
        task_id='minha_tarefa_exemplo',
        python_callable=minha_tarefa,
    )

    # Configurar a sequência das tarefas (nesse caso, é só uma tarefa isolada)
    tarefa_exemplo
