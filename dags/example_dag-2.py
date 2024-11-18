from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import random

# Função para gerar um número aleatório
def gerar_numero():
    numero = random.randint(1, 100)
    print(f"Número gerado: {numero}")
    return numero

# Função para exibir o número gerado
def exibir_numero(**context):
    numero = context['ti'].xcom_pull(task_ids='gerar_numero')
    print(f"O número gerado foi: {numero}")

# Configurações padrão da DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Definição da DAG
with DAG(
    'exemplo_dag2',
    default_args=default_args,
    description='Uma segunda DAG de exemplo com múltiplas tarefas',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['exemplo'],
) as dag:

    # Tarefa 1: Gerar um número aleatório
    gerar_numero_task = PythonOperator(
        task_id='gerar_numero',
        python_callable=gerar_numero,
    )

    # Tarefa 2: Exibir o número gerado
    exibir_numero_task = PythonOperator(
        task_id='exibir_numero',
        python_callable=exibir_numero,
        provide_context=True,
    )

    # Definindo a sequência de execução das tarefas
    gerar_numero_task >> exibir_numero_task
