import tkinter as tk

class AdminDashboard:
    def __init__(self, master, albus):
        self.master = master
        self.master.title("Albus Administrator Dashboard")
        self.albus = albus

        self.label = tk.Label(master, text="Feedback Summary")
        self.label.pack()

        self.text_area = tk.Text(master, height=15, width=50)
        self.text_area.pack()

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
    # Simulating some collected feedback for demonstration purposes
    albus.record_feedback("Sample response 1", 'upvote')
    albus.record_feedback("Sample response 2", 'upvote')
    albus.record_feedback("Sample response 3", 'downvote')
    albus.record_feedback("Sample response 4", 'upvote')

    app = AdminDashboard(root, albus)
    root.mainloop()


class Albus:
    def __init__(self):
        self.responses = {}

    def record_feedback(self, response, feedback):
        if response not in self.responses:
            self.responses[response] = {'upvotes': 0, 'downvotes': 0}
        
        if feedback == 'upvote':
            self.responses[response]['upvotes'] += 1
        elif feedback == 'downvote':
            self.response
