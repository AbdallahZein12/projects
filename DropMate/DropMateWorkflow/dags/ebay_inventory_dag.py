from airflow import DAG 
from airflow.operators.python import PythonOperator 
from datetime import datetime, timedelta 

def scrape_amazon():
    print("Scraping Amazon...")

def scrape_reviews():
    print("Scraping reviews...")
    
def sentiment_analysis():
    print("Analyzing sentiment...")
    
def filter_products(): 
    print("Filtering products...")
    
def save_to_db():
    print("Saving to DB...")
    
default_args = {
    'owner': 'zeindev',
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='Ebay_Inventory_Pipeline',
    default_args=default_args,
    description='Pipeline for Updating Ebay Inventory',
    start_date=datetime(2025,4,14),
    schedule_interval='@daily',
    catchup=False 
) as dag: 
    t1 = PythonOperator(task_id='scrape_amazon',python_callable=scrape_amazon)
    t2 = PythonOperator(task_id='scrape_reviews',python_callable=scrape_reviews)
    t3 = PythonOperator(task_id='sentiment_analysis', python_callable=sentiment_analysis)
    t4 = PythonOperator(task_id='filter_products',python_callable=filter_products)
    t5 = PythonOperator(task_id='save_to_db',python_callable=save_to_db)
    
    t1 >> t2 >> t3 >> t4 >> t5