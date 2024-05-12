def main():
    a = []  # Arrival time
    b = []  # Burst time
    x = []  # Copy of burst time
    waiting = []  # Waiting time
    turnaround = []  # Turnaround time
    completion = []  # Completion time
    smallest = 0
    count = 0
    time = 0
    avg = 0
    tt = 0

    # Input
    n = int(input("Enter the number of Processes: "))
    for i in range(n):
        a.append(int(input(f"Enter arrival time of process {i+1}: ")))
    for i in range(n):
        b.append(int(input(f"Enter burst time of process {i+1}: ")))

    x = b.copy()
    b.append(9999)

    # Scheduling
    while count != n:
        smallest = n
        for i in range(n):
            if a[i] <= time and b[i] < b[smallest] and b[i] > 0:
                smallest = i
        b[smallest] -= 1

        if b[smallest] == 0:
            count += 1
            end = time + 1
            completion.append(end)
            waiting.append(end - a[smallest] - x[smallest])
            turnaround.append(end - a[smallest])
        
        time += 1

    # Output
    print("Process\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time\tCompletion Time")
    for i in range(n):
        print(f"p{i+1}\t\t{x[i]}\t\t{a[i]}\t\t{waiting[i]}\t\t{turnaround[i]}\t\t{completion[i]}")
        avg += waiting[i]
        tt += turnaround[i]
    
    print(f"\nAverage waiting time = {avg/n}")
    print(f"Average Turnaround time = {tt/n}")


if __name__ == "__main__":
    main()
