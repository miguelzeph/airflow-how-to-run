
# Minimal Apache Airflow Setup for Basic Functionality

This repository provides a minimal setup to get started with Apache Airflow. It includes the essential configurations and components required to deploy and run Airflow in a development or production-like environment.

---

## Steps to Set Up

### 1. Download `docker-compose.yml`

Run the following command to download the required `docker-compose.yml` file:

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.3/docker-compose.yaml'
```

### 2. Configure the Environment

Create the necessary directories for Airflow:

```bash
mkdir -p ./dags ./logs ./plugins ./config
```

### 3. Initialize the Database

Start the Airflow database initialization process:

```bash
docker compose up airflow-init
```

### 4. Start Services

Run the following command to start all Airflow services:

```bash
docker compose up
```

---

## Troubleshooting

### Clean Up the Environment

If you encounter any issues and want to reset everything, use this command to clean up:

```bash
docker compose down --volumes --remove-orphans
```

### Restart Scheduler

After adding a new DAG, you can restart the scheduler to apply changes without restarting all services:

```bash
docker-compose restart airflow-scheduler
```

---

## Notes

- Ensure that Docker and Docker Compose are properly installed and configured on your machine.
- This setup is designed for basic functionality and can be expanded for production-grade deployments.
