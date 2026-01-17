import csv
import os

# ===============================
# BACA DATASET CSV (ANTI ERROR)
# ===============================
def read_csv(filename):
    processes = []

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename)

    print("Membaca file:", file_path)

    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            processes.append({
                'process': row['process'],
                'arrival': int(row['arrival_time']),
                'burst': int(row['burst_time'])
            })

    return processes


# ===============================
# FCFS SCHEDULING
# ===============================
def fcfs(processes):
    time = 0
    result = []

    processes = sorted(processes, key=lambda x: x['arrival'])

    for p in processes:
        if time < p['arrival']:
            time = p['arrival']

        completion = time + p['burst']
        turnaround = completion - p['arrival']
        waiting = turnaround - p['burst']

        result.append((p['process'], completion, turnaround, waiting))
        time = completion

    return result


# ===============================
# SJF NON-PREEMPTIVE
# ===============================
def sjf(processes):
    time = 0
    completed = []
    ready_queue = processes.copy()

    while ready_queue:
        available = [p for p in ready_queue if p['arrival'] <= time]

        if not available:
            time += 1
            continue

        shortest = min(available, key=lambda x: x['burst'])
        ready_queue.remove(shortest)

        completion = time + shortest['burst']
        turnaround = completion - shortest['arrival']
        waiting = turnaround - shortest['burst']

        completed.append((shortest['process'], completion, turnaround, waiting))
        time = completion

    return completed


# ===============================
# CETAK HASIL
# ===============================
def print_result(title, data):
    print(f"\n{title}")
    print("Process | Completion | Turnaround | Waiting")
    print("--------------------------------------------")

    total_wt = 0
    total_tat = 0

    for p in data:
        print(f"{p[0]:<7} | {p[1]:<10} | {p[2]:<10} | {p[3]}")
        total_wt += p[3]
        total_tat += p[2]

    n = len(data)
    print("--------------------------------------------")
    print(f"Average Waiting Time    : {total_wt / n:.2f}")
    print(f"Average Turnaround Time : {total_tat / n:.2f}")


# ===============================
# MAIN PROGRAM
# ===============================
if __name__ == "__main__":
    filename = "dataset.csv"

    processes = read_csv(filename)

    fcfs_result = fcfs(processes)
    sjf_result = sjf(processes)

    print_result("FCFS Scheduling", fcfs_result)
    print_result("SJF Scheduling", sjf_result)
