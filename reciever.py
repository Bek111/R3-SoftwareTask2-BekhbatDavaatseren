import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    print("received data on  the re:", data)
    if data in [b'5']:
        print("Speed has been set to max")
        if data in [b'w', b'W']:    # for going forward
            print("[f255][f255][f255][f255]")
        if data in [b'd', b'D']:    # turning right
            print("[f255][f255][r255][r255]")
        if data in [b'a', b'A']:    # turning left
            print("[r255][r255][f255][f255]")
        if data in [b's', b'S']:    # turning left
            print("[r255][r255][r255][r255]")
    else:
        print("Speed has not been set to max")
    conn.send(data)
conn.close()
