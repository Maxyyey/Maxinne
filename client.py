import tkinter as tk
from tkinter import messagebox
import socket
import threading

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            message_listbox.insert(tk.END, message)
        except OSError:
            break

def send_message(event=None):
    message = my_message.get()
    if message:
        client_socket.send(bytes(message, 'utf-8'))
        my_message.set('')
        message_listbox.insert(tk.END, "You: " + message)  # Display the sent message locally
    else:
        messagebox.showwarning('Empty Message', 'Please enter a message.')

def on_closing(event=None):
    client_socket.close()
    root.destroy()



# Create the main window
root = tk.Tk()
root.title('CHAT APP')

# Create the message listbox
message_listbox = tk.Listbox(root, height=15, width=50, font=('Arial', 12))
message_listbox.pack(padx=10, pady=10)

# Create a scrollbar for the listbox
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
message_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=message_listbox.yview)

# Create the entry widget for user input
my_message = tk.StringVar()
entry_field = tk.Entry(root, textvariable=my_message, font=('Arial', 12))
entry_field.bind('<Return>', send_message)
entry_field.pack(padx=10, pady=10)

# Create the send button
send_button = tk.Button(root, text='Send', command=send_message, font=('Arial', 12))
send_button.pack(pady=5)

# Set up the socket connection
HOST = '192.168.100.57'
PORT = 39277

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Start a thread to receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Configure the closing event
root.protocol('WM_DELETE_WINDOW', on_closing)

# Start the Tkinter event loop
root.mainloop()
