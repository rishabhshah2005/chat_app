from tkinter import *
import socket
import threading


FONT = ('helvetica', 15)


def clear_frame(frm):
    for widgets in frm.winfo_children():
        widgets.destroy()


def receive(server, nick, frm):
    while True:
        try:
            msg = server.recv(1024).decode('utf-8')
            msg = str(msg)
            if msg == 'NICK':
                server.send(nick.encode('utf-8'))
            else:
                Label(frm, text=msg).pack()

        except:
            print('error')
            server.close()
            break


def write(server, msg, nick):
    mes = f"{nick} >> {msg}".encode('utf-8')
    server.send(mes)



def connect(frm, ip, port, nickname):
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))
        canvas_width = event.width


    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))

        clear_frame(frm)
        # ENTRY BOX
        m = StringVar()
        m.set('')
        msg_ent = Entry(frm, width=35, font=FONT, textvariable=m).pack(side=BOTTOM, expand=1, anchor='w')
        # SEND BUTTON
        send_btn = Button(frm, text="Send", font=FONT, padx=10, pady=25, command=lambda: write(s, msg=m.get(), nick=nickname)).pack(side=BOTTOM, expand=1, anchor='se')

        canvas = Canvas(frm, height=470)
        canvas.pack(side=LEFT, expand=1, fill=BOTH)

        scrollbar = Scrollbar(frm, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.bind('<Configure>', on_configure)

        frame = Frame(canvas)
        canvas.create_window(0, 0, window=frame, anchor='w')

        t = threading.Thread(target=receive, args=(s, nickname, frame))
        t.start()

    except:
        print('ERROR')


