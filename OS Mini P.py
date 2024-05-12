import tkinter as tk
from tkinter import messagebox

# Define the main GUI window
window = tk.Tk()
window.title("Scheduling Simulator")

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
        roundrobin_schedule(process_list)
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
    for process in process_list:
        pid, arrival_time, burst_time = process['pid'], process['arrival_time'], process['burst_time']
        if arrival_time > completion_time:
            completion_time = arrival_time
        completion_time += burst_time
        turnaround_time = completion_time - arrival_time
        waiting_time = turnaround_time - burst_time
        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time
        output_text.insert(tk.END, f"{pid}\t{arrival_time}\t{burst_time}\t{completion_time}\t{turnaround_time}\t{waiting_time}\n")
    avg_turnaround_time = total_turnaround_time / len(process_list)
    avg_waiting_time = total_waiting_time / len(process_list)
    output_text.insert(tk.END, f"Average Turn Around Time = {avg_turnaround_time:.2f}\n")
    output_text.insert(tk.END, f"Average Waiting Time = {avg_waiting_time:.2f}\n")
    output_text.insert(tk.END, "Ended")

# Function to run the SJF scheduling algorithm
def sjf_schedule(process_list):
    process_list.sort(key=lambda x: x['burst_time'])  # Sort the processes based on burst time
    completion_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, "Pid\tAT\tBT\tCT\tTAT\tWT\n")
    for process in process_list:
        pid, arrival_time, burst_time = process['pid'], process['arrival_time'], process['burst_time']
        if arrival_time > completion_time:
            completion_time = arrival_time
        completion_time += burst_time
        turnaround_time = completion_time - arrival_time
        waiting_time = turnaround_time - burst_time
        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time
        output_text.insert(tk.END, f"{pid}\t{arrival_time}\t{burst_time}\t{completion_time}\t{turnaround_time}\t{waiting_time}\n")
    avg_turnaround_time = total_turnaround_time / len(process_list)
    avg_waiting_time = total_waiting_time / len(process_list)
    output_text.insert(tk.END, f"Average Turn Around Time = {avg_turnaround_time:.2f}\n")
    output_text.insert(tk.END, f"Average Waiting Time = {avg_waiting_time:.2f}\n")
    output_text.insert(tk.END, "Ended")

# Function to run the SRTN scheduling algorithm
def srt_n_schedule(process_list):
    processes = process_list.copy()
    completed_processes = []
    current_time = 0
    while processes:
        min_burst_time = float('inf')
        shortest_process = None
        for process in processes:
            if process['burst_time'] < min_burst_time and process['arrival_time'] <= current_time:
                min_burst_time = process['burst_time']
                shortest_process = process
        if shortest_process is None:
            current_time += 1
            continue
        shortest_process['burst_time'] -= 1
        current_time += 1
        if shortest_process['burst_time'] == 0:
            shortest_process['completion_time'] = current_time
            completed_processes.append(shortest_process)
            processes.remove(shortest_process)

    display_srt_n_results(completed_processes)

# Function to display the SRTN scheduling results
def display_srt_n_results(processes):
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
    output_text.insert(tk.END, "Ended")

def roundrobin_schedule(process_list):

# Create a label for algorithm selection
algorithm_label = tk.Label(window, text="Select Scheduling Algorithm:")
algorithm_label.pack()

# Create a variable to store the selected algorithm
algorithm_var = tk.StringVar(window)

# Create a dropdown menu for algorithm selection
algorithm_dropdown = tk.OptionMenu(window, algorithm_var, "FCFS", "SJF", "SRTN", "Round Robin")
algorithm_dropdown.pack()

# Create a label and entry field for the number of processes
num_processes_label = tk.Label(window, text="Number of Processes:")
num_processes_label.pack()
num_processes_entry = tk.Entry(window)
num_processes_entry.pack()

# Create a button to run the simulation
run_button = tk.Button(window, text="Run Simulation", command=run_simulation)
run_button.pack()

# Frame for process input fields
process_inputs_frame = tk.Frame(window)
process_inputs_frame.pack()

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
add_fields_button.pack()

# Text widget to display output
output_text = tk.Text(window, height=20, width=80)
output_text.pack()

# Start the GUI event loop
window.mainloop()
