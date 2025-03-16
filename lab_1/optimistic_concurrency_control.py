import psycopg2
import time
from threading import Thread

def optimistic_concurrency_control():
    conn = psycopg2.connect(dbname="test", user="postgres", password="11111111")
    cursor = conn.cursor()

    for _ in range(10000):
        while True:
            cursor.execute("SELECT counter, version FROM user_counter WHERE user_id = 1")
            counter, version = cursor.fetchone()
            counter += 1
            cursor.execute("UPDATE user_counter SET counter = %s, version = %s WHERE user_id = %s AND version = %s", (counter, version + 1, 1, version))
            conn.commit()
            if cursor.rowcount > 0:
                break

    cursor.close()
    conn.close()

# Create 10 threads for concurrent updates
threads = []
start_time = time.time()

for i in range(10):
    thread = Thread(target=optimistic_concurrency_control)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(f"Optimistic concurrency control time: {end_time - start_time} seconds")
