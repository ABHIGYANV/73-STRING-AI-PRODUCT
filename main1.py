import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

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

        # Styling
        style = ttk.Style()
        style.theme_use('clam')  # Set theme to 'clam'
        style.configure("TFrame", background="#333")
        style.configure("TLabel", background="#333", foreground="white")

        # Frame to hold widgets
        self.frame = ttk.Frame(master)
        self.frame.pack(padx=20, pady=20)

        # Albus response label and text area
        ttk.Label(self.frame, text="Albus Response:", background="#333", foreground="white").grid(row=0, column=0, pady=5)
        self.response_text = tk.Text(self.frame, height=5, width=50, background="#444", foreground="white")
        self.response_text.grid(row=1, column=0, padx=5, pady=5)

        # Thumbs up and thumbs down icons
        self.thumbs_up_img = ImageTk.PhotoImage(Image.open("thumbs_up.png").resize((32, 32)))
        self.thumbs_down_img = ImageTk.PhotoImage(Image.open("thumbs_down.png").resize((32, 32)))

        # Feedback buttons
        self.upvote_button = ttk.Button(self.frame, image=self.thumbs_up_img, command=self.upvote)
        self.upvote_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        self.downvote_button = ttk.Button(self.frame, image=self.thumbs_down_img, command=self.downvote)
        self.downvote_button.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

        # Quit button
        self.quit_button = ttk.Button(self.frame, text="Quit", command=master.quit)
        self.quit_button.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

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

        # Styling
        style = ttk.Style()
        style.theme_use('clam')  # Set theme to 'clam'
        style.configure("TFrame", background="#333")
        style.configure("TLabel", background="#333", foreground="white")

        # Frame to hold widgets
        self.frame = ttk.Frame(master)
        self.frame.pack(padx=20, pady=20)

        # Feedback summary label and text area
        ttk.Label(self.frame, text="Feedback Summary", font=("Helvetica", 14), background="#333", foreground="white").grid(row=0, column=0, columnspan=2, pady=5)
        self.text_area = tk.Text(self.frame, height=15, width=50, background="#444", foreground="white")
        self.text_area.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Update button to refresh feedback summary
        self.update_button = ttk.Button(self.frame, text="Update Summary", command=self.update_summary)
        self.update_button.grid(row=2, column=0, columnspan=2, pady=5, sticky="ew")

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
