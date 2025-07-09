# 🚀 End-to-End Data Engineering Project with dbt, Snowflake, and Apache Airflow

This project demonstrates a complete data engineering pipeline using **dbt Core** for SQL-based data transformation, **Snowflake** as a cloud data warehouse, and **Apache Airflow** for orchestration — all running inside Docker containers.

---

## 📦 Tech Stack

- **Snowflake** – Cloud-based data warehouse  
- **dbt Core** – Data transformation tool using SQL & Jinja  
- **Apache Airflow** – Workflow orchestrator  
- **PostgreSQL** – Metadata DB for Airflow  
- **Docker & Docker Compose** – Containerized development

---

## 📁 Project Structure

end_to_end_project/
├── dags/ # Airflow DAGs
├── dbt/ # dbt project (models, configs)
├── Dockerfile # Custom Airflow image
├── docker-compose.yaml # Service definitions
├── requirements.txt # Python dependencies
├── .env # Snowflake credentials
└── README.md # You're here!




## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
https://github.com/Ahmedwael12345/airflow_snowflake_dbt_project.git
cd end_to_end_project



2. Configure .env File

Create a .env file in the project root with:

SNOWFLAKE_USER=dbt_user
SNOWFLAKE_PASSWORD=dbt_password
SNOWFLAKE_ACCOUNT=fx56113.eu-central-2.aws
SNOWFLAKE_DATABASE=finance_db
SNOWFLAKE_SCHEMA=raw
SNOWFLAKE_ROLE=ACCOUNTADMIN
SNOWFLAKE_WAREHOUSE=finance_wh



Start the Project

docker-compose up --build

    Airflow UI: http://localhost:8088

    DAG ID: dbt_snowflake_workflow



👨‍💻 Author

Ahmed Wael Galal
Email: ahmedwaelgalal2@gmail.com





