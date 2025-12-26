import csv

def read_csv(filename):
    processes = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            processes.append({
                'pid': row['pid'],
                'arrival': int(row['arrival_time']),
                'burst': int(row['burst_time'])
            })
    return processes

def fcfs(processes):
    time = 0
    total_waiting = 0
    total_turnaround = 0

    processes.sort(key=lambda x: x['arrival'])  # Urutkan berdasarkan arrival time

    print("=== FCFS Scheduling ===")
    print("PID | Start | Finish | Waiting | Turnaround")
    print("-------------------------------------------")

    for p in processes:
        if time < p['arrival']:
            time = p['arrival']

        start = time
        finish = time + p['burst']
        waiting = start - p['arrival']
        turnaround = finish - p['arrival']

        total_waiting += waiting
        total_turnaround += turnaround

        print(f"{p['pid']:>3} | {start:>5} | {finish:>6} | {waiting:>7} | {turnaround:>10}")

        time = finish

    avg_waiting = total_waiting / len(processes)
    avg_turnaround = total_turnaround / len(processes)
    print(f"\nAverage Waiting Time    = {avg_waiting}")
    print(f"Average Turnaround Time = {avg_turnaround}")


def sjf(processes):
    time = 0
    completed = 0
    n = len(processes)
    total_waiting = 0
    total_turnaround = 0
    is_completed = [False]*n

    print("\n=== SJF Non-Preemptive Scheduling ===")
    print("PID | Start | Finish | Waiting | Turnaround")
    print("-------------------------------------------")

    while completed < n:
        idx = -1
        min_burst = float('inf')
        for i in range(n):
            if processes[i]['arrival'] <= time and not is_completed[i]:
                if processes[i]['burst'] < min_burst:
                    min_burst = processes[i]['burst']
                    idx = i
                elif processes[i]['burst'] == min_burst:
                    if processes[i]['arrival'] < processes[idx]['arrival']:
                        idx = i

        if idx == -1:
            time +=1
            continue

        start = time
        finish = time + processes[idx]['burst']
        waiting = start - processes[idx]['arrival']
        turnaround = finish - processes[idx]['arrival']

        total_waiting += waiting
        total_turnaround += turnaround

        print(f"{processes[idx]['pid']:>3} | {start:>5} | {finish:>6} | {waiting:>7} | {turnaround:>10}")

        time = finish
        is_completed[idx] = True
        completed += 1

    avg_waiting = total_waiting / n
    avg_turnaround = total_turnaround / n
    print(f"\nAverage Waiting Time    = {avg_waiting}")
    print(f"Average Turnaround Time = {avg_turnaround}")

if __name__ == "__main__":
    filename = "Data set.csv"
    processes = read_csv(filename)

    # FCFS
    fcfs(processes.copy())

    # SJF Non-Preemptive
    sjf(processes.copy())
