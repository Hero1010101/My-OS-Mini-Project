def findWaitingTime(processes, n, bt, wt, quantum): 
    rem_bt = [0] * n

    # Copy the burst time into rem_bt[] 
    for i in range(n): 
        rem_bt[i] = bt[i]
    t = 0 # Current time 

    # Keep traversing processes in round robin manner until all of them are not done. 
    while True:
        done = True

        # Traverse all processes one by one repeatedly 
        for i in range(n):
            # If burst time of a process is greater than 0 then only need to process further 
            if rem_bt[i] > 0:
                done = False # There is a pending process
                
                # If burst time is greater than the time quantum, it will execute for a time quantum 
                if rem_bt[i] > quantum:
                    t += quantum 
                    rem_bt[i] -= quantum 
                # If burst time is smaller than or equal to quantum, the process will be completed
                else:
                    t = t + rem_bt[i] 
                    wt[i] = t - bt[i] # Waiting time is current time minus time used by this process 
                    rem_bt[i] = 0 # As the process gets fully executed, its remaining burst time becomes 0

        # If all processes are done 
        if done:
            break
            
def findTurnAroundTime(processes, n, bt, wt, tat, ct):
    for i in range(n):
        tat[i] = bt[i] + wt[i] 
        ct[i] = tat[i] # Completion time is the sum of burst time and waiting time

def findavgTime(processes, n, bt, quantum): 
    wt = [0] * n
    tat = [0] * n 
    ct = [0] * n # List to store completion time

    # Find waiting time of all processes 
    findWaitingTime(processes, n, bt, wt, quantum) 

    # Find turn around time for all processes 
    findTurnAroundTime(processes, n, bt, wt, tat, ct) 

    # Display processes along with all details 
    print("Processes Burst Time Waiting Time Turn-Around Time Completion Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt += wt[i] 
        total_tat += tat[i] 
        print(f"  {processes[i]} \t\t {bt[i]} \t\t {wt[i]} \t\t {tat[i]} \t\t {ct[i]}")

    print(f"\nAverage waiting time = {total_wt / n}") 
    print(f"Average turn around time = {total_tat / n}") 

# Driver code 
if __name__ == "__main__":
    # Take input for the time quantum
    quantum = int(input("Enter the time quantum: "))
    
    # Take input for the number of processes
    n = int(input("Enter the number of processes: "))
    
    # Take input for the burst time of each process
    burst_time = []
    for i in range(n):
        bt = int(input(f"Enter the burst time for process {i + 1}: "))
        burst_time.append(bt)

    # Process id's 
    proc = [i + 1 for i in range(n)]

    findavgTime(proc, n, burst_time, quantum)
