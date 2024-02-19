import tkinter as tk
from tkinter import messagebox

class Albus:
    def __init__(self):
        self.responses = {}

    def record_feedback(self, response, feedback):
        if response not in self.responses:
            self.responses[response] = {'upvotes': 0, 'downvotes': 0}
        
        if feedback == 'upvote':
            self.responses[response]['upvotes'] += 1
        elif feedback == 'downvote':
            self.responses[response]['downvotes'] += 1


class AlbusGUI:
    def __init__(self, master, albus):
        self.master = master
        self.master.title("Albus Feedback")

        self.albus = albus

        # Label and Text area to display Albus's response
        self.label = tk.Label(master, text="Albus Response:")
        self.label.pack()

        self.response_text = tk.Text(master, height=5, width=50)
        self.response_text.pack()

        # Buttons for feedback
        self.feedback_label = tk.Label(master, text="Was this response helpful?")
        self.feedback_label.pack()

        self.upvote_button = tk.Button(master, text="Yes", command=self.upvote)
        self.upvote_button.pack(side=tk.LEFT)

        self.downvote_button = tk.Button(master, text="No", command=self.downvote)
        self.downvote_button.pack(side=tk.RIGHT)

        # Quit Button
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

    def upvote(self):
        response = self.response_text.get("1.0", "end-1c")
        self.albus.record_feedback(response, 'upvote')
        self.show_message("Thank you for your positive feedback!")

    def downvote(self):
        response = self.response_text.get("1.0", "end-1c")
        self.albus.record_feedback(response, 'downvote')
        self.show_message("Thank you for your feedback! We'll improve.")

    def show_message(self, message):
        messagebox.showinfo("Feedback", message)


class AdminDashboard:
    def __init__(self, master, albus):
        self.master = master
        self.master.title("Albus Administrator Dashboard")

        self.albus = albus

        # Label and Text area to display feedback summary
        self.label = tk.Label(master, text="Feedback Summary")
        self.label.pack()

        self.text_area = tk.Text(master, height=15, width=50)
        self.text_area.pack()

        # Update button to refresh feedback summary
        self.update_button = tk.Button(master, text="Update Summary", command=self.update_summary)
        self.update_button.pack()

        # Initial update of feedback summary
        self.update_summary()

    def update_summary(self):
        summary = ""
        for response, feedback in self.albus.responses.items():
            summary += f"Response: {response}\n"
            summary += f"Upvotes: {feedback['upvotes']}\n"
            summary += f"Downvotes: {feedback['downvotes']}\n\n"
        self.text_area.delete('1.0', tk.END)
        self.text_area.insert(tk.END, summary)


def main():
    root = tk.Tk()

    albus = Albus()
    user_app = AlbusGUI(root, albus)
    admin_app = AdminDashboard(tk.Toplevel(root), albus)

    root.mainloop()


if __name__ == "__main__":
    main()
