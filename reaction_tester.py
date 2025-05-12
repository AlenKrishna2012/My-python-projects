import tkinter as tk
import time
import random

class ReactionTester:
    def __init__(self, master):
        self.master = master
        self.master.title("Reaction Speed Tester")
        
        self.label = tk.Label(master, text="Get ready...", font=("Helvetica", 18))
        self.label.pack(pady=50)

        self.start_button = tk.Button(master, text="Start", font=("Helvetica", 8), command=self.start_test)
        self.start_button.pack(pady=20)

        self.reaction_time_label = tk.Label(master, text="", font=("Helvetica", 18))
        self.reaction_time_label.pack(pady=20)

        self.click_button = tk.Button(master, text="Click Me!", font=("Helvetica", 8), command=self.record_reaction)
        self.click_button.pack(pady=20)
        self.click_button.config(state=tk.DISABLED)  # Initially disabled

        self.wait_time = None
        self.start_time = None

    def start_test(self):
        self.label.config(text="Wait for the prompt...")
        self.start_button.config(state=tk.DISABLED)
        self.click_button.config(state=tk.DISABLED)  # Disable click button
        
        # Wait for a random duration before showing the prompt
        self.wait_time = random.randint(2, 5)
        self.master.after(self.wait_time * 1000, self.show_prompt)

    def show_prompt(self):
        self.label.config(text="Click the button now!")
        self.start_time = time.time()  # Record the start time
        self.click_button.config(state=tk.NORMAL)  # Enable click button

    def record_reaction(self):
        if self.start_time is not None:
            reaction_time = time.time() - self.start_time
            self.reaction_time_label.config(text=f"Your reaction time: {reaction_time:.4f} seconds")
            self.label.config(text="Get ready...")
            self.start_button.config(state=tk.NORMAL)  # Enable start button for new test
            self.click_button.config(state=tk.DISABLED)  # Disable click button again
            self.start_time = None  # Reset start time

if __name__ == "__main__":
    root = tk.Tk()
    tester = ReactionTester(root)
    root.mainloop()