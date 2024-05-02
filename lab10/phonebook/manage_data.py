import csv
import psycopg2
from pb import insert_data, query_data, delete_data, update_data, enter_data, upload_csv

conn = psycopg2.connect(
    host="127.0.0.1",
    user="postgres",
    password="Aminashh2",
    database="suppliers"
)
cur = conn.cursor()




# enter_data()
#upload_csv('numbers.csv')
#enter_data()

delete_data(name='Amina')

query_data()