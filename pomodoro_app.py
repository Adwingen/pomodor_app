# modulo pomodoro_app
from tkinter import *


class PomodoroApp:
    def __init__(self, timer):
        # Constants
        self.PINK = "#e2979c"
        self.RED = "#e7305b"
        self.GREEN = "#9bdeac"
        self.YELLOW = "#f7f5dd"
        self.FONT_NAME = "Courier"

        # Reference to timer logic
        self.timer_logic = timer

        # UI Setup
        self.window = Tk()
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=50, bg=self.YELLOW)
        self.window.resizable(False, False)

        # Canvas
        self.canvas = Canvas(width=200, height=224, bg=self.YELLOW, highlightthickness=0)
        self.tomato_img = PhotoImage(file="tomato.png")
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white",
                                                  font=(self.FONT_NAME, 35, "bold"))
        self.canvas.grid(column=2, row=1)

        # Labels
        self.label_timer = Label(text="Timer", foreground=self.GREEN, font=(self.FONT_NAME, 45, "bold"), bg=self.YELLOW)
        self.label_timer.grid(column=2, row=0)

        # Buttons
        self.button_start = Button(text="Start", command=lambda: self.timer_logic.start_timer(self))
        self.button_start.grid(column=1, row=2)
        self.button_reset = Button(text="Reset", command=lambda: self.timer_logic.reset_timer(self))
        self.button_reset.grid(column=3, row=2)

        # Check Mark Label
        self.label_check_mark = Label(bg=self.YELLOW, fg=self.GREEN, font=(self.FONT_NAME, 15, "bold"))
        self.label_check_mark.grid(column=2, row=3)

        # Start the main loop
        self.window.mainloop()

    # UI Update Methods
    def update_timer(self, text, color):
        self.label_timer.config(text=text, fg=color)

    def update_canvas(self, time_text):
        self.canvas.itemconfig(self.timer_text, text=time_text)

    def update_check_marks(self, marks):
        self.label_check_mark.config(text=marks)

    def enable_start_button(self):
        self.button_start.config(state="normal")

    def disable_start_button(self):
        self.button_start.config(state="disabled")
