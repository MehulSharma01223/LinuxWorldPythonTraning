import socket
import os

print("1. Send File")
print("2. Receive File")
choice = input("Choose option (1/2): ")

# ======================= RECEIVER =======================
if choice == "2":
    HOST = "0.0.0.0"
    PORT = 5001

    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(1)

    print(f"\n[+] Waiting for connection on port {PORT}...")
    conn, addr = s.accept()
    print(f"[+] Connected with {addr}")

    filename = conn.recv(1024).decode()
    print(f"[+] Receiving file: {filename}")

    with open(filename, 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

    print("[+] File received successfully.")
    conn.close()
    s.close()

# ======================= SENDER =========================
elif choice == "1":
    HOST = input("Enter receiver IP: ")
    PORT = 5001

    filename = input("Enter file name to send: ")

    if not os.path.exists(filename):
        print("File does not exist!")
        exit()

    s = socket.socket()
    s.connect((HOST, PORT))

    s.send(filename.encode())

    with open(filename, 'rb') as f:
        data = f.read(1024)
        while data:
            s.send(data)
            data = f.read(1024)

    print("[+] File sent successfully.")
    s.close()

else:
    print("Invalid choice!")
