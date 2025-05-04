import tkinter as tk
from datetime import datetime, timedelta

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("300x150")  # Set the window size

        self.running = False
        self.start_time = None
        self.elapsed_time = timedelta(0)

        # Time label with color
        self.time_label = tk.Label(root, text="00:00:00.000", font=("Arial", 30), fg="white", bg="black")
        self.time_label.pack(pady=200)

        # Start button with color
        self.start_button = tk.Button(root, text="Start", command=self.start, width=10, bg="green", fg="white")
        self.start_button.pack(side=tk.LEFT, padx=5)

        # Stop button with color
        self.stop_button = tk.Button(root, text="Stop", command=self.stop, width=10, bg="red", fg="white")
        self.stop_button.pack(side=tk.LEFT, padx=5)

        # Reset button with color
        self.reset_button = tk.Button(root, text="Reset", command=self.reset, width=10, bg="blue", fg="white")
        self.reset_button.pack(side=tk.LEFT, padx=5)

        self.update_time()

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = datetime.now() - self.elapsed_time
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = timedelta(0)
        self.time_label.config(text="00:00:00.000")

    def update_time(self):
        if self.running:
            self.elapsed_time = datetime.now() - self.start_time
            time_str = str(self.elapsed_time)
            if "." not in time_str:
                time_str += ".000"  # Add milliseconds if they are missing
            time_str = time_str.split(".")[0] + "." + time_str.split(".")[1][:3]  # Format to hh:mm:ss.ms
            self.time_label.config(text=time_str)
        self.root.after(10, self.update_time)  # Update every 10ms for better accuracy

# Main application execution
if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()