import time
import winsound
import threading
import tkinter as tk
from tkinter import simpledialog

# 긴박한 느낌의 무한 알람 반복
def long_beep(stop_event):
    while not stop_event.is_set():
        # 다급한 시스템 사운드 사용
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        if stop_event.wait(0.05):  # 간격 줄여서 다급함 UP
            break

def start_timer(root, minutes, seconds):
    total_seconds = minutes * 60 + seconds
    if total_seconds <= 0:
        print("0초 타이머는 실행되지 않습니다.")
        return

    label = tk.Label(root, text="", font=("Arial", 30, "bold"), bg="#F0F0F0", fg="#000000")
    label.pack(padx=20, pady=10)

    stop_event = threading.Event()
    alarm_thread = [None]
    timer_running = [True]

    def stop_alarm():
        timer_running[0] = False
        stop_event.set()
        stop_button.config(state=tk.DISABLED)
        label.config(text="🛑 알람 종료")

    def update():
        if not timer_running[0]:
            return
        nonlocal total_seconds
        if total_seconds > 0:
            mins, secs = divmod(total_seconds, 60)
            label.config(text=f"⏳ {mins:02}:{secs:02}")
            total_seconds -= 1
            root.after(1000, update)
        else:
            label.config(text="🔔 종료!")
            start_alarm()

    def start_alarm():
        alarm_thread[0] = threading.Thread(target=long_beep, args=(stop_event,), daemon=True)
        alarm_thread[0].start()

    stop_button = tk.Button(
        root, text="정지", font=("Arial", 14, "bold"),
        bg="#333333", fg="white", activebackground="#666666", relief="flat",
        command=stop_alarm
    )
    stop_button.pack(pady=10)

    update()

def main():
    root = tk.Tk()
    root.title("Focus Timer")
    root.geometry("300x180")
    root.configure(bg="#F0F0F0")
    root.resizable(False, False)

    minutes = simpledialog.askinteger("타이머 설정", "분을 입력하세요:", minvalue=0)
    seconds = simpledialog.askinteger("타이머 설정", "초를 입력하세요:", minvalue=0)

    if minutes is None:
        minutes = 0
    if seconds is None:
        seconds = 0

    start_timer(root, minutes, seconds)
    root.mainloop()

if __name__ == '__main__':
    main()
