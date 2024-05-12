# Function to find the waiting 
# time for all processes
def findWaitingTime(n, bt, wt):

    # waiting time for 
    # first process is 0
    wt[0] = 0

    # calculating waiting time
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1] 

# Function to calculate turn
# around time
def findTurnAroundTime(n, bt, wt, tat):

    # calculating turnaround 
    # time by adding bt[i] + wt[i]
    for i in range(n):
        tat[i] = bt[i] + wt[i]

# Function to calculate
# average time
def findavgTime(n, bt):

    wt = [0] * n
    tat = [0] * n 
    ct = [0] * n
    total_wt = 0
    total_tat = 0

    # Function to find waiting 
    # time of all processes
    findWaitingTime(n, bt, wt)

    # Function to find turn around 
    # time for all processes
    findTurnAroundTime(n, bt, wt, tat)
    
    # Calculate completion time
    for i in range(n):
        if i == 0:
            ct[i] = bt[i]
        else:
            ct[i] = ct[i - 1] + bt[i]

    # Display processes along
    # with all details
    print("Processes Burst time Waiting time Turn around time Completion time")

    # Calculate total waiting time 
    # and total turn around time
    for i in range(n):
    
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" " + str(i + 1) + "\t\t" +
                    str(bt[i]) + "\t " +
                    str(wt[i]) + "\t\t " +
                    str(tat[i]) + "\t\t " +
                    str(ct[i])) 

    print("Average waiting time = " +
                str(total_wt / n))
    print("Average turn around time = " +
                    str(total_tat / n))

    # Print Gantt chart
    print("\nGantt Chart:")
    print("-" * (sum(bt) + 7))
    for i in range(n):
        print("| P" + str(i + 1) + " ", end="")
    print("|")
    print("-" * (sum(bt) + 7))
    start_time = 0
    for i in range(n):
        print(start_time, end="\t")
        start_time += bt[i]
    print(start_time)


# Driver code
if __name__ == "__main__":
    
    # Take input for number of processes
    n = int(input("Enter the number of processes: "))

    # Take input for burst time of each process
    burst_time = []
    for i in range(n):
        bt = int(input("Enter the burst time for process {}: ".format(i+1)))
        burst_time.append(bt)

    findavgTime(n, burst_time)

# This code is contributed 
# by ChitraNayal
