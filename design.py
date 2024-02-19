import tkinter as tk
from tkinter import messagebox

class AlbusGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Albus Feedback")
        
        self.albus = Albus()

        self.label = tk.Label(master, text="Albus Response:")
        self.label.pack()

        self.response_text = tk.Text(master, height=5, width=50)
        self.response_text.pack()

        self.feedback_label = tk.Label(master, text="Was this response helpful?")
        self.feedback_label.pack()

        self.upvote_button = tk.Button(master, text="Yes", command=self.upvote)
        self.upvote_button.pack(side=tk.LEFT)

        self.downvote_button = tk.Button(master, text="No", command=self.downvote)
        self.downvote_button.pack(side=tk.RIGHT)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

    def upvote(self):
        response = self.response_text.get("1.0", "end-1c")
        self.albus.record_feedback(response, 'upvote')
        self.show_message("Thank you for your feedback!")

    def downvote(self):
        response = self.response_text.get("1.0", "end-1c")
        self.albus.record_feedback(response, 'downvote')
        self.show_message("Thank you for your feedback!")

    def show_message(self, message):
        messagebox.showinfo("Feedback", message)


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


def main():
    root = tk.Tk()
    app = AlbusGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
