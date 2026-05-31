import socket
import threading
from contextlib import suppress
import time

BUFFER = 4096

# -------------------- Chat Functions --------------------
def receive_loop(sock, stop_event, role, peer_role, protocol="TCP", peer_addr=None):
    """Receive loop for TCP or UDP"""
    try:
        while not stop_event.is_set():
            if protocol == "TCP":
                data = sock.recv(BUFFER)
                if not data:
                    stop_event.set()
                    print(f"\n[{peer_role}] disconnected.")
                    break
            else:  # UDP
                data, _ = sock.recvfrom(BUFFER)
                if not data:
                    continue

            print(f"[{peer_role}] -> {data.decode().strip()} \n")

    except Exception:
        stop_event.set()

def send_loop(sock, stop_event, role, peer_role, protocol="TCP", peer_addr=None):
    """Send loop for TCP or UDP using input()."""
    try:
        while not stop_event.is_set():
            msg = input(f"{role} -> {peer_role}: \n")
            if msg.lower() in ("exit", "quit"):
                stop_event.set()
                if protocol == "TCP":
                    with suppress(Exception):
                        sock.shutdown(socket.SHUT_RDWR)
                break
            
            if protocol == "TCP":
                sock.sendall(msg.encode())
            else:
                sock.sendto(msg.encode(), peer_addr)

    except (KeyboardInterrupt, EOFError):
        print("\nExiting...")
        stop_event.set()
    except Exception:
        stop_event.set()

# -------------------- TCP --------------------
def tcp_host():
    """Starts a TCP server and waits for a client to connect."""
    host = input("Bind host [0.0.0.0]: ") or "0.0.0.0"
    port = int(input("Port [5000]: ") or 5000)

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((host, port))
    srv.listen(1)
    print(f"[TCP HOST] Listening on {host}:{port} ...")
    conn, addr = srv.accept()
    print(f"[TCP HOST] Connected by {addr}")

    stop_event = threading.Event()
    threading.Thread(target=receive_loop, args=(conn, stop_event, "HOST", "CLIENT", "TCP"), daemon=True).start()
    threading.Thread(target=send_loop, args=(conn, stop_event, "HOST", "CLIENT", "TCP"), daemon=True).start()
    stop_event.wait()

    conn.close()
    srv.close()
    print("[TCP HOST] Closed.")

def tcp_join():
    """Connects to a TCP server as a client."""
    host = input("Server host/IP [127.0.0.1]: ") or "127.0.0.1"
    port = int(input("Port [5000]: ") or 5000)

    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cli.connect((host, port))
        print("[TCP CLIENT] Connected!")

        stop_event = threading.Event()
        threading.Thread(target=receive_loop, args=(cli, stop_event, "CLIENT", "HOST", "TCP"), daemon=True).start()
        threading.Thread(target=send_loop, args=(cli, stop_event, "CLIENT", "HOST", "TCP"), daemon=True).start()
        stop_event.wait()
    except ConnectionRefusedError:
        print("[TCP CLIENT] Connection refused. Is host running?")
    finally:
        cli.close()
        print("[TCP CLIENT] Closed.")

# -------------------- UDP --------------------
def udp_host():
    """Starts a UDP server and waits for a client's first message."""
    host = input("Bind host [0.0.0.0]: ") or "0.0.0.0"
    port = int(input("Port [6000]: ") or 6000)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    print(f"[UDP HOST] Listening on {host}:{port} ...")

    # Wait for the first message to discover the client's address.
    # This ensures a clean start before the main loops begin.
    print("[UDP HOST] Waiting for client to send first message...")
    data, client_addr = sock.recvfrom(BUFFER)
    print(f"\n[CLIENT] -> {data.decode().strip()}")

    stop_event = threading.Event()
    threading.Thread(target=receive_loop, args=(sock, stop_event, "HOST", "CLIENT", "UDP"), daemon=True).start()
    threading.Thread(target=send_loop, args=(sock, stop_event, "HOST", "CLIENT", "UDP", client_addr), daemon=True).start()
    stop_event.wait()
    sock.close()
    print("[UDP HOST] Closed.")

def udp_join():
    """Connects to a UDP server by sending the first message."""
    host = input("Server host/IP [127.0.0.1]: ") or "127.0.0.1"
    port = int(input("Port [6000]: ") or 6000)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr = (host, port)

    print("[UDP CLIENT] Connected!")
    # Send the first message to initiate the handshake with the server.
    sock.sendto("Hiiiee".encode(), server_addr)
    
    stop_event = threading.Event()
    threading.Thread(target=receive_loop, args=(sock, stop_event, "CLIENT", "HOST", "UDP"), daemon=True).start()
    threading.Thread(target=send_loop, args=(sock, stop_event, "CLIENT", "HOST", "UDP", server_addr), daemon=True).start()
    stop_event.wait()
    sock.close()
    print("[UDP CLIENT] Closed.")

# -------------------- Main Menu --------------------
def main_menu():
    while True:
        print("\n===== CHAT MENU =====")
        print("1. TCP Chat")
        print("2. UDP Chat")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            sub = input("Host or Join? (h/j): ").strip().lower()
            if sub == "h":
                tcp_host()
            elif sub == "j":
                tcp_join()
            else:
                print("Invalid choice. Please enter 'h' or 'j'.")
        elif choice == "2":
            sub = input("Host or Join? (h/j): ").strip().lower()
            if sub == "h":
                udp_host()
            elif sub == "j":
                udp_join()
            else:
                print("Invalid choice. Please enter 'h' or 'j'.")
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Enter 1-3.")

if __name__ == "__main__":
    main_menu()
