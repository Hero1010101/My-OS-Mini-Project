def main():
    # Taking the number of processes
    n = int(input("Enter number of processes: "))
    # Matrix for storing Process Id, Arrival Time, Burst Time, Waiting Time, Turn Around Time, Completion Time.
    A = [[0 for _ in range(6)] for _ in range(n)]
    total_wt, total_tat = 0, 0

    print("Enter Arrival Time and Burst Time:")
    for i in range(n):  # User Input Arrival Time and Burst Time and alloting Process Id.
        A[i][1] = int(input(f"P{i+1} Arrival Time: "))
        A[i][2] = int(input(f"P{i+1} Burst Time: "))
        A[i][0] = i + 1

    # Sorting processes based on their Arrival Time.
    A.sort(key=lambda x: x[1])

    start_time = A[0][1]  # Start time is the arrival time of the first process
    gantt_chart = []

    for i in range(n):
        if start_time < A[i][1]:  # If there's an idle state between processes
            gantt_chart.append(('Idle', A[i][1] - start_time))
            start_time = A[i][1]
        gantt_chart.append((f'P{A[i][0]}', A[i][2]))
        start_time += A[i][2]
        A[i][5] = start_time  # Completion time

    for i in range(n):
        A[i][3] = A[i][5] - A[i][1] - A[i][2]  # Waiting time
        A[i][4] = A[i][5] - A[i][1]  # Turnaround time

    total_wt = sum([A[i][3] for i in range(n)])
    total_tat = sum([A[i][4] for i in range(n)])

    avg_wt = total_wt / n
    avg_tat = total_tat / n

    # Printing Gantt Chart
    print("\nGantt Chart:")
    print("-" * 40)
    for process, duration in gantt_chart:
        print(f"| {process} ", end="")
    print("|\n" + "-" * 40)

    # Printing the table
    print("\nP\tAT\tBT\tWT\tTAT\tCT")
    for i in range(n):
        print(f"P{A[i][0]}\t{A[i][1]}\t{A[i][2]}\t{A[i][3]}\t{A[i][4]}\t{A[i][5]}")

    print(f"\nAverage Waiting Time: {avg_wt}")
    print(f"Average Turnaround Time: {avg_tat}")


if __name__ == "__main__":
    main()
