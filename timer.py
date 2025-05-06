import tkinter as tk
from tkinter import messagebox
from datetime import timedelta

class Timer:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer")
        self.root.geometry("400x200")  # Adjusted for better layout
        self.root.configure(bg="lightblue")  # Set lightblue background

        self.running = False
        self.time_left = timedelta(0)  # Time remaining as a timedelta object

        # Input field for timer duration
        self.input_label = tk.Label(root, text="Set Timer (D:HH:MM:SS):", font=("Arial", 14), bg="lightblue")
        self.input_label.pack(pady=10)

        self.time_entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.time_entry.insert(0, "0:00:00:00")  # Default format
        self.time_entry.pack(pady=5)

        # Display the countdown
        self.timer_label = tk.Label(root, text="0:00:00:00.000", font=("Arial", 27), fg="blue", bg="lightblue")
        self.timer_label.pack(pady=20)

        # Start button
        self.start_button = tk.Button(root, text="Start", command=self.start_timer, width=9, bg="green", fg="white")
        self.start_button.pack(side=tk.LEFT, padx=6)

        # Pause button
        self.stop_button = tk.Button(root, text="Pause", command=self.pause_timer, width=10, bg="orange", fg="white")
        self.stop_button.pack(side=tk.LEFT, padx=5)

        # Reset button
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer, width=9, bg="red", fg="white")
        self.reset_button.pack(side=tk.LEFT, padx=5)

    def start_timer(self):
        if not self.running:
            self.running = True
            try:
                if self.time_left == timedelta(0):  # Parse time only if the timer hasn't started
                    time_parts = self.time_entry.get().split(":")
                    if len(time_parts) != 4:
                        raise ValueError("Invalid format")
                    days, hours, minutes, seconds = map(int, time_parts)
                    self.time_left = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
                self.update_timer()
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter time in D:HH:MM:SS format.")

    def pause_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.time_left = timedelta(0)
        self.timer_label.config(text="0:00:00:00.000")
        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(0, "0:00:00:00")

    def update_timer(self):
        if self.running and self.time_left > timedelta(0):
            self.time_left -= timedelta(milliseconds=10)  # Subtract 10 ms
            days = self.time_left.days
            hours, remainder = divmod(self.time_left.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            milliseconds = self.time_left.microseconds // 1000
            self.timer_label.config(text=f"{days}:{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}")
            self.root.after(10, self.update_timer)
        elif self.time_left <= timedelta(0) and self.running:
            self.running = False
            self.timer_label.config(text="0:00:00:00.000")
            messagebox.showinfo("Timer Ended", "Time's up!")

# Main application execution
if __name__ == "__main__":
    root = tk.Tk()
    timer = Timer(root)
    root.mainloop()