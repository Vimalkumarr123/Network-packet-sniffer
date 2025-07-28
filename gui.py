import tkinter as tk

def launch_gui():
    root = tk.Tk()
    root.title("Firewall Logs")

    text = tk.Text(root, height=30, width=100)
    text.pack()

    def refresh_logs():
        with open("firewall.log") as f:
            text.delete(1.0, tk.END)
            text.insert(tk.END, f.read())

    btn = tk.Button(root, text="Refresh Logs", command=refresh_logs)
    btn.pack()

    root.mainloop()

if __name__ == "__main__":
    launch_gui()
