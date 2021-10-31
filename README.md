# R3-SoftwareTask2-BekhbatDavaatseren
 The project first takes the input from keyboard which was taken from https://pynput.readthedocs.io/en/latest/keyboard.html#monitoring-the-keyboard. 
 The second part is involving the sending and the recieving of the data which was implemented as the key data turned into bytes via (bytes(format(key.char), 'utf-8')). The main reciever and client program was taken from https://wiki.python.org/moin/TcpCommunication#TCP_Communication
 It was placed under the def on_press(key) statement
A character is pressed then sent to the reciever as bytes.
The data then is in a infinite loop of recording, there are if statements where pressing 5 leads to max speed and only then will the rest of the if statements of going foward is w, d,a,s the standard control they each were set to consider both capital and lowercase letters. 
The actual input is b'5' due to the string to bytes transformation  
PROBLEM: socket problem where only 1 input can be put anymore leads to the program crashing.  