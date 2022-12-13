
from tkinter import Tk, Frame, Scrollbar, Label, END, Entry, Text, VERTICAL, Button, messagebox #Tkinter Python Module for GUI
import socket #Sockets for network connection
import threading # for multiple proccess
import caesar_cipher, monoalphabetic_cipher,polyalphabetic_cipher, hill_cipher, playfair_cipher,otp ,rail_fence_cipher,columnar_cipher,hashing_for_integrity #importing all the ciphers
from tkinter import *

class GUI:
    client_socket = None
    last_received_message = None
    def __init__(self, master):
        self.root = master
        self.chat_transcript_area = None
        self.name_widget = None
        self.enter_text_widget = None
        self.join_button = None
        self.key_widget = None
        self.cipher_widget = None
        self.decrypt_label = None
        self.initialize_socket()
        self.initialize_gui()
        self.listen_for_incoming_messages_in_a_thread()

    def initialize_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # initialazing socket with TCP and IPv4
        remote_ip = '127.0.0.1' # IP address
        remote_port = 10319 #TCP port
        self.client_socket.connect((remote_ip, remote_port)) #connect to the remote server

    def initialize_gui(self): # GUI initializer
        self.root.title("Socket Chat")
        self.root.resizable(0, 0)
        self.display_chat_box()
        self.display_name_section()
        self.display_cipher_section()
        self.display_key_section()
        self.display_chat_entry_box()
        self.display_decrypt_section()
        self.display_decrypt_text()

    def display_cipher_section(self):
        options = [
            "Caesar Cipher",
            "Monoalphabetic Cipher",
            "Polyalphabetic Cipher",
            "Hill Cipher",
            "Playfair Cipher",
            "One Time Pad",
            "Rail Fence Cipher",
            "Columnar Cipher",
            "Hashing for integrity",
        ]
        def show():
            self.cipher_widget = clicked.get()
        # datatype of menu text
        clicked = StringVar()

        # initial menu text
        clicked.set( "Select Cipher" )

        # Create Dropdown menu
        drop = OptionMenu( root , clicked , *options )
        drop.pack()

        # Create button, it will change label text
        button = Button( root , text = "Set This" , command = show ).pack()


    def listen_for_incoming_messages_in_a_thread(self):
        thread = threading.Thread(target=self.receive_message_from_server, args=(self.client_socket,)) # Create a thread for the send and receive in same time
        thread.start()
    #function to recieve msg
    def receive_message_from_server(self, so):
        while True:
            buffer = so.recv(256)
            if not buffer:
                break
            message = buffer.decode('utf-8')

            if "joined" in message:
                user = message.split(":")[1]
                message = user + " has joined"
                self.chat_transcript_area.insert('end', message + '\n')
                self.chat_transcript_area.yview(END)
            else:
                self.chat_transcript_area.insert('end', message + '\n')
                self.chat_transcript_area.yview(END)

        so.close()

    def display_name_section(self):
        frame = Frame()
        Label(frame, text='Enter your name:', font=("Helvetica", 16)).pack(side='left', padx=10)
        self.name_widget = Entry(frame, width=50, borderwidth=2)
        self.name_widget.pack(side='left', anchor='e')
        self.join_button = Button(frame, text="Join", width=10, command=self.on_join).pack(side='left')
        frame.pack(side='top', anchor='nw')

    def display_key_section(self):
        frame = Frame()
        Label(frame, text='Enter your Key:', font=("Helvetica", 16)).pack(side='left', padx=10)
        self.key_widget = Entry(frame, width=50, borderwidth=2)
        self.key_widget.pack(side='left', anchor='e')
        self.join_button = Button(frame, text="SET KEY", width=10, command=self.on_join).pack(side='left')
        frame.pack(side='top', anchor='nw')

    def display_chat_box(self):
        frame = Frame()
        Label(frame, text='Chat Box:', font=("Serif", 12)).pack(side='top', anchor='w')
        self.chat_transcript_area = Text(frame, width=60, height=10, font=("Serif", 12))
        scrollbar = Scrollbar(frame, command=self.chat_transcript_area.yview, orient=VERTICAL)
        self.chat_transcript_area.config(yscrollcommand=scrollbar.set)
        self.chat_transcript_area.bind('<KeyPress>', lambda e: 'break')
        self.chat_transcript_area.pack(side='left', padx=10)
        scrollbar.pack(side='right', fill='y')
        frame.pack(side='top')

    def display_chat_entry_box(self):
        frame = Frame()
        Label(frame, text='Enter message:', font=("Serif", 12)).pack(side='top', anchor='w')
        self.enter_text_widget = Text(frame, width=60, height=3, font=("Serif", 12))
        self.enter_text_widget.pack(side='left', pady=15)
        self.enter_text_widget.bind('<Return>', self.on_enter_key_pressed)
        frame.pack(side='top')

    def display_decrypt_section(self):
        frame = Frame()
        Label(frame, text='Enter message to decrypt:', font=("Helvetica", 16)).pack(side='left', padx=10)
        self.decrypt_widget = Entry(frame, width=50, borderwidth=2)
        self.decrypt_widget.pack(side='left', anchor='e')
        self.decrypt_button = Button(frame, text="Decrypt", width=10, command=self.decrypt).pack(side='left')
        frame.pack(side='top', anchor='nw')




    def display_decrypt_text(self):
            frame = Frame()
            self.decrypt_label =Label(frame, text=self.decrypt_label, font=("Serif", 12)).pack(side='top', anchor='w')
            frame.pack(side='top', anchor='nw')

    def decrypt(self):
        key = self.key_widget.get()
        data = self.decrypt_widget.get()
        print(self.cipher_widget)
        # decrypt the data here
        if self.cipher_widget == "Caesar Cipher":
            data = caesar_cipher.decrypt(data, key)
        elif self.cipher_widget == "Monoalphabetic Cipher":
            data = monoalphabetic_cipher.decrypt(data, key)
        elif self.cipher_widget == "Polyalphabetic Cipher":
            data = polyalphabetic_cipher.decrypt(data, key)
        elif self.cipher_widget == "Playfair Cipher":
            data = playfair_cipher.decrypt(data, key)
        elif self.cipher_widget == "One Time Pad":
            data = otp.decrypt(data, key)
        elif self.cipher_widget == "Rail Fence Cipher":
            data = rail_fence_cipher.decrypt(data, key)
        elif self.cipher_widget == "Columnar Cipher":
            data = columnar_cipher.decrypt(data, key)
        elif self.cipher_widget == "Hashing for integrity":
            data = hashing_for_integrity.decrypt(data)
        elif self.cipher_widget == "Hill Cipher":
            data = hill_cipher.decrypt(data,key)
        

        self.decrypt_widget.delete(0, "end")
        self.decrypt_widget.insert(0, data)


    def on_join(self):
        if len(self.name_widget.get()) == 0:
            messagebox.showerror(
                "Enter your name", "Enter your name to send a message")
            return
        self.name_widget.config(state='disabled')
        self.client_socket.send(("joined:" + self.name_widget.get()).encode('utf-8'))

    def on_enter_key_pressed(self, event):
        if len(self.name_widget.get()) == 0:
            messagebox.showerror("Enter your name", "Enter your name to send a message")
            return
        self.send_chat()
        self.clear_text()

    def on_enter_key_added(self, event):
        if len(self.name_widget.get()) == 0:
            messagebox.showerror("Enter your key", "Enter your key to send a message")
            return
        self.send_key()
        self.clear_text()

    def clear_text(self):
        self.enter_text_widget.delete(1.0, 'end')

    def send_chat(self):
        senders_name = self.name_widget.get().strip() + ": "
        data = self.enter_text_widget.get(1.0, 'end').strip()
        key = self.key_widget.get()

        # Encrypt with all ciphers here
        if self.cipher_widget == "Caesar Cipher":
            data = caesar_cipher.encrypt(data, key)
        elif self.cipher_widget == "Monoalphabetic Cipher":
            data = monoalphabetic_cipher.encrypt(data, key)
        elif self.cipher_widget == "Polyaplhabetic Cipher":
            data = polyalphabetic_cipher.encrypt(data, key)
        elif self.cipher_widget == "Playfair Cipher":
            data = playfair_cipher.encrypt(data, key)
        elif self.cipher_widget == "One Time Pad":
            data = otp.encrypt(data, key)
        elif self.cipher_widget == "Rail Fence Cipher":
            data = rail_fence_cipher.encrypt(data, key)
        elif self.cipher_widget == "Columnar Cipher":
            data = columnar_cipher.encrypt(data, key)
        elif self.cipher_widget == "Hashing for integrity":
            data = hashing_for_integrity.encrypt(data,key)
        elif self.cipher_widget == "Hill Cipher":
            data = hill_cipher.encrypt(data,key)
        # default to caesar cipher
        else:
            data = caesar_cipher.encrypt(data, 15)
        # Check which cipher we need and call it
        message = (senders_name + data).encode('utf-8')
        self.chat_transcript_area.insert('end', message.decode('utf-8') + '\n')
        self.chat_transcript_area.yview(END)
        self.client_socket.send(message)
        self.enter_text_widget.delete(1.0, 'end')
        return 'break'

    def on_close_window(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            self.client_socket.close()
            exit(0)

#the mail function
if __name__ == '__main__':
    root = Tk()
    gui = GUI(root)
    root.protocol("WM_DELETE_WINDOW", gui.on_close_window)
    root.mainloop()
