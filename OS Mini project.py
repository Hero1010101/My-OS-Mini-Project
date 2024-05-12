import tkinter as tk
import tkinter.messagebox as messagebox


class Process:
    def __init__(self, pid, at, bt):
        self.Pid = pid
        self.At = at
        self.Bt = bt
        self.Ct = 0
        self.Tat = 0
        self.Wt = 0


def fcfs(num_of_process):
    process_list = []
    for i in range(num_of_process):
        process_id = int(pid_entries[i].get())
        arrival_time = int(arrival_entries[i].get())
        burst_time = int(burst_entries[i].get())
        process_list.append(Process(process_id, arrival_time, burst_time))

    process_list.sort(key=lambda x: x.At)
    completion_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0

    result_text = "Pid\tAT\tBT\tCT\tTAT\tWT\n"
    for i in range(num_of_process):
        process = process_list[i]
        if process.At > completion_time:
            completion_time = process.At
        completion_time += process.Bt
        turnaround_time = completion_time - process.At
        waiting_time = turnaround_time - process.Bt
        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time
        result_text += f"{process.Pid}\t{process.At}\t{process.Bt}\t{completion_time}\t{turnaround_time}\t{waiting_time}\n"

    avg_turnaround_time = total_turnaround_time / num_of_process
    avg_waiting_time = total_waiting_time / num_of_process
    result_text += f"\nAverage Turn Around Time = {avg_turnaround_time:.2f}\n"
    result_text += f"Average Waiting Time = {avg_waiting_time:.2f}"

    messagebox.showinfo("FCFS Scheduling Result", result_text)


def calculate():
    try:
        num_of_process = int(num_processes_entry.get())

        if num_of_process <= 0:
            messagebox.showerror("Input Error", "Number of processes should be a positive integer.")
            return

        fcfs(num_of_process)

    except ValueError:
        messagebox.showerror("Input Error", "Invalid input. Please enter a valid number of processes.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the main window
window = tk.Tk()
window.title("FCFS Scheduling")
window.geometry("400x300")

# Number of processes input
num_processes_label = tk.Label(window, text="Number of Processes:")
num_processes_label.pack()

num_processes_entry = tk.Entry(window)
num_processes_entry.pack()

# Button to calculate FCFS
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Process inputs
process_inputs_frame = tk.Frame(window)
process_inputs_frame.pack()

pid_labels = []
arrival_labels = []
burst_labels = []

pid_entries = []
arrival_entries = []
burst_entries = []

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

        # Append the labels and entries to their respective lists
        pid_labels.append(pid_label)
        arrival_labels.append(arrival_label)
        burst_labels.append(burst_label)
        pid_entries.append(pid_entry)
        arrival_entries.append(arrival_entry)
        burst_entries.append(burst_entry)

# Add Process Fields button
add_fields_button = tk.Button(window, text="Add Process Fields", command=add_process_fields)
add_fields_button.pack()

# Run the main loop
window.mainloop()

