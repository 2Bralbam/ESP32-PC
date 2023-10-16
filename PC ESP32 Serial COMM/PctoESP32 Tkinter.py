import serial
import time
import tkinter as tk
from tkinter import messagebox
import serial.tools.list_ports
import threading

MAX_BUFF_LEN = 255
SETUP = False
port = None
running = True
prev = time.time()

def connect():
    global port, SETUP
    com_value = com_listbox.get(com_listbox.curselection())
    try:
        port = serial.Serial(com_value, 115200, timeout=1)
        SETUP = True
        connection_status.itemconfig(connection_indicator, fill="green")
        connection_label.config(text="ESP32 conectado")
        
    except:
        messagebox.showerror("Error", "No se pudo conectar al puerto " + com_value)

def read_ser(num_char = 1):
    string = port.read(num_char)
    return string.decode()

def write_ser(cmd):
    cmd = cmd + '\n'
    port.write(cmd.encode())

def send_command():
    cmd = entry.get()
    if cmd:
        write_ser(cmd)

def update_received_messages():
    while running:
        if SETUP:
            message = read_ser(MAX_BUFF_LEN)
            if len(message) > 0:
                received_messages.insert(tk.END, message)
                
        time.sleep(1)  # Check for new messages every second

def stop():
    global running
    running = False
    if SETUP:
        port.close()
    root.quit()

root = tk.Tk()
root.title("Control Serial esp32")
root.geometry("500x600")

label2 = tk.Label(text="Elija puerto")
com_listbox = tk.Listbox(root)
com_listbox.pack()
com_ports = serial.tools.list_ports.comports()
for com_port in com_ports:
    com_listbox.insert(tk.END, com_port.device)

connect_button = tk.Button(root, text="Conectar", command=connect)
connect_button.pack()

received_messages = tk.Listbox(root)
received_messages.pack()

connection_status = tk.Canvas(root, width=50, height=50)
connection_status.pack()
connection_indicator = connection_status.create_oval(10, 10, 40, 40, fill="red")

connection_label = tk.Label(root, text="ESP32 desconectado")
connection_label.pack()

label = tk.Label(text="Inserte comando")
label.pack()
entry = tk.Entry(root)
entry.pack()
send_button = tk.Button(root, text="Enviar", command=send_command)
send_button.pack()

stop_button = tk.Button(root, text="Cerrar todo", command=stop)
stop_button.pack()

threading.Thread(target=update_received_messages).start()  # Start checking for new messages in a separate thread

root.mainloop()
