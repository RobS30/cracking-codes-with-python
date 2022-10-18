from ctypes import alignment
from tkinter import BOTTOM, CENTER
import PySimpleGUI as sg

def EncryptionTool():
    
    layout1 = [
        [sg.Text('')],
        [sg.Text("Enter the text to encrypt: ")],
        [sg.Text(''), sg.Multiline(key='user_input_to_encrypt',size=(80,10))],
        [sg.Text('')],
        [sg.Text("Enter Encryption Key: ")],
        [sg.Text('Encryption Key '), sg.Input('',key ='encryption_key',size=(40,30))],
        [sg.Text('')],
        [sg.Text(''), sg.Button('Start'), sg.Button('Exit')],
        [sg.Text('')]]

    layout2 = [
        [sg.Text('')],
        [sg.Text("Enter the text to decrypt ")],
        [sg.Text(''), sg.Multiline(key='user_input_to_decrypt',size=(80,10))],
        [sg.Text('')],
        [sg.Text("Enter Encryption Key: ")],
        [sg.Text('Decryption Key '), sg.Input('',key ='decryption_key',size=(40,30))],
        [sg.Text('')],
        [sg.Text(''), sg.Button('Start'), sg.Button('Exit')],
        [sg.Text('')]]

    layout3 = [
        [sg.Text('')],
        [sg.Text("Enter the encrypted text you'd like to attempt to crack: ")],
        [sg.Text("Warning: This may take a substantial amount of time depending on the length of encryption key used.")],
        [sg.Text(''), sg.Text('',key='text_to_crack')],
        [sg.Text(''), sg.Multiline(size=(80,10))],
        [sg.Text(''), sg.Button('Start'), sg.Button('Exit')]]


    main = [
        [sg.TabGroup([
            [sg.Tab('Encrypt', layout1,tooltip='Encrypt')],
            [sg.Tab('Decrypt', layout2,tooltip='Decrypt')],
            [sg.Tab('Toolkit', layout3,tooltip='Toolkit')]])],
        [sg.Text("Output "), sg.Push()],
        [sg.Output(size=(80,10))],
        [sg.Text('')]]

    window = sg.Window('Main', main, default_element_size=(30, 1),element_justification='c')

    # user input is captured in 'value' object
    # ---===--- Loop taking in user input and using it to query  --- #
    while True:
        event, value = window.read()
        if event == 'Start' or event == 'Start0' or event == 'Start1':
            print(value)               
        else:
            break
    window.close()


EncryptionTool()