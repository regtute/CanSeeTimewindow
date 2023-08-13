import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# 创建Tkinter窗口
window = tk.Tk()

# 设置窗口标题
window.title("Countdown")

# 创建文本标签
label = tk.Label(window, text="",font=("Arial", 24))
label.pack()

# 创建进度条
progress_bar = ttk.Progressbar(window, orient='horizontal', mode='determinate')
progress_bar.pack()

# 定义递归函数来更新文本标签和进度条的内容
def update_countdown(count):
    # 在这里更新文本标签和进度条的内容
    if count == 0:
        label.config(text="时间到")
        messagebox.showerror(title="到喽！！", message="时间到")
        progress_bar['value'] = 0
        return
    label.config(text=str(count))
    progress_bar['value'] = count

    # 更新倒计时
    count -= 1

    if count >= 0:
        # 在指定的毫秒数后调用递归函数
        window.after(1000*60, update_countdown, count)

# 获取用户输入的倒计时时间
def start_countdown():
    input_text = entry.get()
    
    try:
        count = int(input_text)
    except ValueError:
        count = 0

    # 设置进度条的最大值
    progress_bar['maximum'] = count

    # 第一次调用递归函数开始倒计时
    update_countdown(count)

# 创建输入框和按钮
entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="开始倒计时", command=start_countdown)
button.pack()

# 开始事件循环
window.mainloop()