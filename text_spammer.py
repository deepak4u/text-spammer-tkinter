import tkinter
import customtkinter
import pyautogui as pg
import time

# customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()   # create CTk window like you do with the Tk window
app.geometry("400x200")
app.title("Text Spammer!")


def countdown_timer(count):
    if count > 0:
        # call countdown again after 1000ms (1s)
        app.after(1000, countdown_timer, count - 1)

    if count == 0:
        spam_text = entry_spam_text.get()
        spam_text_count = int(entry_spam_text_count.get())
        for i in range(spam_text_count):
            pg.write(spam_text)
            time.sleep(0.5)
            pg.press("Enter")

    label_counter.configure(text=f"Program will start in {count} sec...")
    # print(f"Program will start in {count} sec...")


entry_spam_text = customtkinter.CTkEntry(master=app, placeholder_text="Enter text to spam")
entry_spam_text.pack(padx=10, pady=10)

entry_spam_text_count = customtkinter.CTkEntry(master=app, placeholder_text="Count")
entry_spam_text_count.pack(padx=10, pady=10)

# Todo: Validation needed for text fields
button_spam = customtkinter.CTkButton(master=app, text="Bomb It!", command=lambda: countdown_timer(6))
button_spam.pack(pady=10, anchor=tkinter.CENTER)

label_counter = customtkinter.CTkLabel(master=app, text='')
label_counter.pack(anchor=tkinter.CENTER)

app.mainloop()