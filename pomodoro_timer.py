# modulo pomodoro_timer
import math
import pygame

# Inicialização do pygame
pygame.mixer.init()


class PomodoroTimer:
    def __init__(self, work_min=25, short_break_min=5, long_break_min=20):
        self.work_min = work_min
        self.short_break_min = short_break_min
        self.long_break_min = long_break_min
        self.reps = 0
        self.timer = None

    def reset_timer(self, app):
        app.window.after_cancel(self.timer)
        app.update_timer("Timer", app.GREEN)
        app.update_canvas("00:00")
        self.reps = 0
        app.update_check_marks("")
        app.enable_start_button()

    def start_timer(self, app):
        self.reps += 1
        work_sec = self.work_min * 60
        short_break_sec = self.short_break_min * 60
        long_break_sec = self.long_break_min * 60
        app.disable_start_button()

        if self.reps % 8 == 0:
            app.update_timer("Break", app.RED)
            self.count_down(long_break_sec, app)
        elif self.reps % 2 == 0:
            app.update_timer("Break", app.PINK)
            self.count_down(short_break_sec, app)
        else:
            app.update_timer("Work", app.GREEN)
            self.count_down(work_sec, app)

    # No final de cada contagem, reproduza o som
    def count_down(self, count, app):
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec == 0:
            count_sec = "00"
        elif count_sec < 10:
            count_sec = f"0{count_sec}"

        app.update_canvas(f"{count_min}:{count_sec}")

        if count > 0:
            self.timer = app.window.after(1000, self.count_down, count - 1, app)
        else:
            # Reproduzir o som com pygame
            pygame.mixer.music.load("notification.wav")
            pygame.mixer.music.play()
            self.start_timer(app)
            marks = "".join("✓" for _ in range(math.floor(self.reps / 2)))
            app.update_check_marks(marks)
