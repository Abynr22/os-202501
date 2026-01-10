import time

print("Mulai uji resource Docker", flush=True)
data = []

for i in range(1, 50):
    data.append("X" * 10_000_000)  # 10 MB
    print(f"Alokasi memori: {i*10} MB", flush=True)
    time.sleep(0.3)

print("Selesai")
