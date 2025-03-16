import psycopg2
import time
from threading import Thread

def in_place_update():
    conn = psycopg2.connect(dbname="test", user="postgres", password="11111111")
    cursor = conn.cursor()

    for _ in range(10000):
        cursor.execute("UPDATE user_counter SET counter = counter + 1 WHERE user_id = 1")
        conn.commit()

    cursor.close()
    conn.close()

# Create 10 threads for concurrent updates
threads = []
start_time = time.time()

for i in range(10):
    thread = Thread(target=in_place_update)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(f"In-place update time: {end_time - start_time} seconds")
