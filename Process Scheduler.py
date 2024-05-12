import tkinter as tk
from tkinter import messagebox

# Define the main GUI window
window = tk.Tk()
window.title("Scheduling Simulator")
window.geometry('800x800')

# Function to handle the button click event
def run_simulation():
    algorithm = algorithm_var.get()
    num_processes = int(num_processes_entry.get())

    # Retrieve process details from the input fields
    process_list = get_process_details(num_processes)

    if algorithm == "FCFS":
        fcfs_schedule(process_list)
    elif algorithm == "SJF":
        sjf_schedule(process_list)
    elif algorithm == "SRTN":
        srt_n_schedule(process_list)
    elif algorithm == "RR":
        rr_schedule(process_list)
    else:
        messagebox.showerror("Error", "Invalid algorithm selection!")

# Function to retrieve process details from the input fields
def get_process_details(num_processes):
    process_list = []
    for i in range(num_processes):
        process_id = int(pid_entries[i].get())
        arrival_time = int(arrival_entries[i].get())
        burst_time = int(burst_entries[i].get())
        process_list.append({'pid': process_id, 'arrival_time': arrival_time, 'burst_time': burst_time})
    return process_list

# Function to run the FCFS scheduling algorithm
def fcfs_schedule(process_list):
    process_list.sort(key=lambda x: x['arrival_time'])  # Sort the processes based on arrival time
    completion_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, "Pid\tAT\tBT\tCT\tTAT\tWT\n")
    gantt_chart = "Gantt Chart:\n"
    time_points = set()
    for process in process_list:
        pid, arrival_time, burst_time = process['pid'], process['arrival_time'], process['burst_time']
        if arrival_time > completion_time:
            time_points.add(completion_time)
            completion_time = arrival_time
        time_points.add(completion_time)
        completion_time += burst_time
        time_points.add(completion_time)
        turnaround_time = completion_time - arrival_time
        waiting_time = turnaround_time - burst_time
        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time
        output_text.insert(tk.END, f"{pid}\t{arrival_time}\t{burst_time}\t{completion_time}\t{turnaround_time}\t{waiting_time}\n")
        gantt_chart += f"P{pid} |{'-' * burst_time}| "
    avg_turnaround_time = total_turnaround_time / len(process_list)
    avg_waiting_time = total_waiting_time / len(process_list)
    output_text.insert(tk.END, f"Average Turn Around Time = {avg_turnaround_time:.2f}\n")
    output_text.insert(tk.END, f"Average Waiting Time = {avg_waiting_time:.2f}\n")
    output_text.insert(tk.END, "Ended\n\n")
    output_text.insert(tk.END, gantt_chart)
    output_text.insert(tk.END, "\nTime Points: " + " ".join(str(t) for t in sorted(time_points)))

# Function to run the SJF scheduling algorithm
def sjf_schedule(process_list):
    process_list.sort(key=lambda x: x['burst_time'])  # Sort the processes based on burst time
    completion_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, "Pid\tAT\tBT\tCT\tTAT\tWT\n")
    gantt_chart = "Gantt Chart:\n"
    time_points = set()
    for process in process_list:
        pid, arrival_time, burst_time = process['pid'], process['arrival_time'], process['burst_time']
        if arrival_time > completion_time:
            time_points.add(completion_time)
            completion_time = arrival_time
        time_points.add(completion_time)
        completion_time += burst_time
        time_points.add(completion_time)
        turnaround_time = completion_time - arrival_time
        waiting_time = turnaround_time - burst_time
        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time
        output_text.insert(tk.END, f"{pid}\t{arrival_time}\t{burst_time}\t{completion_time}\t{turnaround_time}\t{waiting_time}\n")
        gantt_chart += f"P{pid} |{'-' * burst_time}| "
    avg_turnaround_time = total_turnaround_time / len(process_list)
    avg_waiting_time = total_waiting_time / len(process_list)
    output_text.insert(tk.END, f"Average Turn Around Time = {avg_turnaround_time:.2f}\n")
    output_text.insert(tk.END, f"Average Waiting Time = {avg_waiting_time:.2f}\n")
    output_text.insert(tk.END, "Ended\n\n")
    output_text.insert(tk.END, gantt_chart)
    output_text.insert(tk.END, "\nTime Points: " + " ".join(str(t) for t in sorted(time_points)))

# Function to run the SRTN scheduling algorithm
def srt_n_schedule(process_list):
    processes = [{'pid': process['pid'], 'arrival_time': process['arrival_time'], 'burst_time': process['burst_time'], 'remaining_burst_time': process['burst_time']} for process in process_list]
    completed_processes = []
    current_time = 0
    gantt_chart = "Gantt Chart:\n"
    time_points = set()
    while processes:
        runnable_processes = [process for process in processes if process['arrival_time'] <= current_time]
        if not runnable_processes:
            time_points.add(current_time)
            current_time += 1
            continue
        shortest_process = min(runnable_processes, key=lambda x: x['remaining_burst_time'])
        if current_time not in time_points:
            time_points.add(current_time)
        shortest_process['remaining_burst_time'] -= 1
        gantt_chart += f"P{shortest_process['pid']} |{'-' * 1}| "
        current_time += 1
        if shortest_process['remaining_burst_time'] == 0:
            shortest_process['completion_time'] = current_time
            completed_processes.append(shortest_process)
            processes.remove(shortest_process)
    display_srt_n_results(completed_processes, gantt_chart, time_points)

# Function to display the SRTN scheduling results
def display_srt_n_results(processes, gantt_chart, time_points):
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, "SRTN Scheduling Results:\n")
    output_text.insert(tk.END, "Pid\tAT\tBT\tCT\tTAT\tWT\n")
    total_turnaround_time = 0
    total_waiting_time = 0
    for process in processes:
        turnaround_time = process['completion_time'] - process['arrival_time']
        waiting_time = turnaround_time - process['burst_time']
        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time
        output_text.insert(tk.END, f"{process['pid']}\t{process['arrival_time']}\t{process['burst_time']}\t{process['completion_time']}\t{turnaround_time}\t{waiting_time}\n")
    num_processes = len(processes)
    avg_turnaround_time = total_turnaround_time / num_processes
    avg_waiting_time = total_waiting_time / num_processes
    output_text.insert(tk.END, f"Average Turnaround Time = {avg_turnaround_time:.2f}\n")
    output_text.insert(tk.END, f"Average Waiting Time = {avg_waiting_time:.2f}\n")
    output_text.insert(tk.END, "Ended\n\n")
    output_text.insert(tk.END, gantt_chart)
    output_text.insert(tk.END, "\nTime Points: " + " ".join(str(t) for t in sorted(time_points)))


# Function to run the Round Robin scheduling algorithm
def rr_schedule(process_list):
    quantum = 2  # Define the time quantum
    time_points = set()
    current_time = 0
    remaining_time = [process['burst_time'] for process in process_list]
    gantt_chart = "Gantt Chart:\n"
    
    # Sort the processes by arrival time and process ID
    process_list.sort(key=lambda x: (x['arrival_time'], x['pid']))
    
    while any(remaining_time):
        # Check if there are any processes arriving at or before the current time
        if not any(process['arrival_time'] <= current_time for process in process_list):
            # Advance current time to the arrival time of the next process
            current_time = min(process['arrival_time'] for process in process_list if process['arrival_time'] > current_time)
            continue
        
        for i, process in enumerate(process_list):
            if remaining_time[i] > 0:
                if process['arrival_time'] <= current_time:
                    time_points.add(current_time)
                    gantt_chart += f"P{process['pid']} |"
                    if remaining_time[i] <= quantum:
                        current_time += remaining_time[i]
                        remaining_time[i] = 0
                        gantt_chart += '-' * remaining_time[i] + "| "
                    else:
                        current_time += quantum
                        remaining_time[i] -= quantum
                        gantt_chart += '-' * quantum + "| "
                    if remaining_time[i] == 0:
                        process['completion_time'] = current_time
    display_rr_results(process_list, gantt_chart, time_points)

# Function to display the Round Robin scheduling results
def display_rr_results(processes, gantt_chart, time_points):
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, "Round Robin Scheduling Results:\n")
    output_text.insert(tk.END, "Pid\tAT\tBT\tCT\tTAT\tWT\n")
    
    total_turnaround_time = 0
    total_waiting_time = 0
    
    # Sort the completed processes by their completion time
    completed_processes = sorted(processes, key=lambda x: x['completion_time'])

    for i, process in enumerate(completed_processes):
        # Calculate turnaround time
        turnaround_time = process['completion_time'] - process['arrival_time']
        total_turnaround_time += turnaround_time
        
        # Calculate waiting time
        waiting_time = max(turnaround_time - process['burst_time'], 0)  # Ensure waiting time is non-negative
        total_waiting_time += waiting_time
        
        # Output process information
        output_text.insert(tk.END, f"{process['pid']}\t{process['arrival_time']}\t{process['burst_time']}\t{process['completion_time']}\t{turnaround_time}\t{waiting_time}\n")
    
    num_processes = len(completed_processes)
    avg_turnaround_time = total_turnaround_time / num_processes
    avg_waiting_time = total_waiting_time / num_processes
    
    # Output average turnaround time and average waiting time
    output_text.insert(tk.END, f"Average Turnaround Time = {avg_turnaround_time:.2f}\n")
    output_text.insert(tk.END, f"Average Waiting Time = {avg_waiting_time:.2f}\n")
    output_text.insert(tk.END, "Ended\n\n")
    output_text.insert(tk.END, gantt_chart)
    output_text.insert(tk.END, "\nTime Points: " + " ".join(str(t) for t in sorted(time_points)))


# Create a label for algorithm selection
algorithm_label = tk.Label(window, text="Select Scheduling Algorithm:", padx='10px', pady='10px')
algorithm_label.pack()

# Create a variable to store the selected algorithm
algorithm_var = tk.StringVar(window)

# Create a dropdown menu for algorithm selection
algorithm_dropdown = tk.OptionMenu(window, algorithm_var, "FCFS", "SJF", "SRTN", "RR")
algorithm_dropdown.pack()

# Create a label and entry field for the number of processes
num_processes_label = tk.Label(window, text="Number of Processes:", padx='10px', pady='10px')
num_processes_label.pack()
num_processes_entry = tk.Entry(window)
num_processes_entry.pack()

# Create a button to run the simulation
run_button = tk.Button(window, text="Run Simulation", command=run_simulation, bg='blue', fg='white')
run_button.place(relx=.66, rely=0.164, anchor='center')

# Frame for process input fields
process_inputs_frame = tk.Frame(window, padx='10px', pady='10px')
process_inputs_frame.place(relx=.5, rely=0.4 ,  anchor='center')

# Lists to store labels and entries for process details
pid_labels = []
arrival_labels = []
burst_labels = []
pid_entries = []
arrival_entries = []
burst_entries = []

# Function to add process input fields dynamically
def add_process_fields():
    num_processes = int(num_processes_entry.get())
    if len(pid_labels) < num_processes:
        process_frame = tk.Frame(process_inputs_frame)
        process_frame.pack()
        pid_label = tk.Label(process_frame, text="PID:")
        pid_label.pack(side=tk.LEFT)
        pid_entry = tk.Entry(process_frame)
        pid_entry.pack(side=tk.LEFT)
        arrival_label = tk.Label(process_frame, text="Arrival Time:")
        arrival_label.pack(side=tk.LEFT)
        arrival_entry = tk.Entry(process_frame)
        arrival_entry.pack(side=tk.LEFT)
        burst_label = tk.Label(process_frame, text="Burst Time:")
        burst_label.pack(side=tk.LEFT)
        burst_entry = tk.Entry(process_frame)
        burst_entry.pack(side=tk.LEFT)
        # Append labels and entries to their respective lists
        pid_labels.append(pid_label)
        arrival_labels.append(arrival_label)
        burst_labels.append(burst_label)
        pid_entries.append(pid_entry)
        arrival_entries.append(arrival_entry)
        burst_entries.append(burst_entry)

# Button to add process input fields
add_fields_button = tk.Button(window, text="Add Process Fields", command=add_process_fields)
add_fields_button.place(relx=.5, rely=0.210, anchor='center')

# Text widget to display output
output_text = tk.Text(window, height=20, width=100)
output_text.place(relx=.5 ,rely=.755, anchor='center')

# Start the GUI event loop
window.mainloop()
