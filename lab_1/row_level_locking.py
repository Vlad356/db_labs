import psycopg2
import time
from threading import Thread

def row_level_locking():
    conn = psycopg2.connect(dbname="test", user="postgres", password="11111111")
    cursor = conn.cursor()

    for _ in range(10000):
        cursor.execute("SELECT counter FROM user_counter WHERE user_id = 1 FOR UPDATE")
        counter = cursor.fetchone()[0]
        counter += 1
        cursor.execute("UPDATE user_counter SET counter = %s WHERE user_id = %s", (counter, 1))
        conn.commit()

    cursor.close()
    conn.close()

# Create 10 threads for concurrent updates
threads = []
start_time = time.time()

for i in range(10):
    thread = Thread(target=row_level_locking)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(f"Row-level locking time: {end_time - start_time} seconds")
