import time

timeout = 5
start_time = time.time()

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time > timeout:
        break

    print(f"Geçen süre: {elapsed_time:.2f} saniye")
    time.sleep(1)

print(f"Döngüden çıkıldı. Toplam geçen süre: {elapsed_time:.2f} saniye")