from tkinter import *
import pyAesCrypt
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "foopassword"
#ENTER VALUE IN DATAFILE
def textEntry(entry):
	value = entry
	with open('data.txt', 'w') as f:
		f.write(value)
		f.close()
# encrypt
def EncryptFunc():
	pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password, bufferSize)
# decrypt
def DecryptFunc():
	pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", password, bufferSize)

#read the data from dataout file
def readEntry():
	with open('dataout.txt', 'r') as f:
		value = f.read()
		f.close()
	output.delete(0.0,END)
	output.insert(END, value)

window = Tk()

window.title("AES algo")
window.configure(background="black")
Label(window,text="Enter the text in data.txt file for encryption",bg="black",fg="white",font="none 12 bold").grid(row=0,column=0,stick='w')
textentry = Entry(window, width=20, bg='white')
textentry.grid(row=2, column=0, sticky='w')
Button(window,text="SUBMIT", width=12,command=lambda: textEntry(textentry.get())).grid(row=5,column=3,sticky='w')
Button(window,text="Encrypt", width=12,command=lambda: EncryptFunc()).grid(row=8,column=0,sticky='w')
Label(window,text="\nOutput is saved inside the data.txt.aes file it is encrypted",bg="black",fg="white",font="none 12 bold").grid(row=12,column=0,stick='w')

#_________________________for decrypted_________________#
Button(window,text="Decrypt", width=6,command=lambda: DecryptFunc()).grid(row=15,column=3,sticky='e')
Label(window,text="\nOutput is saved inside the dataout.txt",bg="black",fg="white",font="none 12 bold").grid(row=19,column=0,stick='w')
Button(window,text="OUTPUT", width=6,command=lambda: readEntry()).grid(row=17,column=3,sticky='e')
output = Text(window, width=75, height=6, wrap=WORD, background="White")
output.grid(row=20,column=0, columnspan=2, stick='w')
window.mainloop()
