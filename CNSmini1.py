from tkinter import *
import pyAesCrypt
import io
#import tkinter as tk
#import requests


bufferSize = 64 * 1024
password = "foopassword"

global fCiph,fDec
# initialize ciphertext binary stream
fCiph = io.BytesIO()

# initialize decrypted binary stream
fDec = io.BytesIO()

# encrypt stream
def EncryptFunc(entry):
	output1.delete(0.0,END)
	pbdata = bytes(entry,encoding= 'utf-8')
	fIn = io.BytesIO(pbdata)
	pyAesCrypt.encryptStream(fIn, fCiph, password, bufferSize)
	# print encrypted data
	print("This is the ciphertext:\n" + str(fCiph.getvalue()))
	output_of_Cipher = str(fCiph.getvalue())
	#label['text'] = output_of_Cipher
	with open('CipherText.txt', 'w') as f:
		f.write(output_of_Cipher)
		f.close()
	output1.insert(END, output_of_Cipher)
#calling the encryption function do this inside tkinter button
#EncryptFunc(entry)

def DecryptFunc():
	output.delete(0.0, END)
	fDec = io.BytesIO()
	# get ciphertext length
	ctlen = len(fCiph.getvalue())
	print(ctlen)
	# go back to the start of the ciphertext stream
	fCiph.seek(0)

	# decrypt stream
	pyAesCrypt.decryptStream(fCiph, fDec, password, bufferSize, ctlen)

	# print decrypted data
	output_of_Decipher = str(fDec.getvalue(),'utf-8')
	print("Decrypted data:\n" + str(fDec.getvalue(),'utf-8'))
	output.insert(END, output_of_Decipher)




#calling DecryptFunc function do this inside tkinter button
#DecryptFunc()

#_____________________GUI_______________________
window = Tk()

window.title("AES algo")
window.configure(background="black")
Label(window,text="Enter the text",bg="black",fg="white",font="none 12 bold").grid(row=0,column=0,stick='w')
textentry = Entry(window, width=20, bg='white')
textentry.grid(row=2, column=0, sticky='w')
Button(window,text="Encrypt", width=6,command=lambda: EncryptFunc(textentry.get())).grid(row=2,column=3,sticky='e')
Label(window,text="\nOutput",bg="black",fg="white",font="none 12 bold").grid(row=4,column=0,stick='w')
output1 = Text(window, width=75, height=6, wrap=WORD, background="White")
output1.grid(row=5,column=0, columnspan=2, stick='w')
#_________________________for decrypted_________________#
Button(window,text="Decrypt", width=6,command=lambda: DecryptFunc()).grid(row=8,column=3,sticky='e')
Label(window,text="\nOutput",bg="black",fg="white",font="none 12 bold").grid(row=11,column=0,stick='w')
output = Text(window, width=75, height=6, wrap=WORD, background="White")
output.grid(row=14,column=0, columnspan=2, stick='w')
window.mainloop()
