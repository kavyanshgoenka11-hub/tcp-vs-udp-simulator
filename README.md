# 🌐 TCP vs UDP Network Simulator

An interactive networking project that visually demonstrates the differences between **TCP (Transmission Control Protocol)** and **UDP (User Datagram Protocol)** through a modern web-based simulator and Python socket programming implementation.

This project helps students, educators, and networking enthusiasts understand how data packets travel across a network, how TCP ensures reliable delivery using acknowledgments, and how UDP prioritizes speed over reliability.

---

## 🚀 Deploy URL: 
https://tcp-vs-udp-chat-simulator.vercel.app/

---

## 🚀 Features

### 🎨 Frontend Simulation
- Interactive TCP/UDP protocol switch
- Real-time packet transmission animations
- TCP acknowledgment (ACK) visualization
- UDP packet loss simulation
- UDP packet reordering simulation
- Network event logging system
- Chat-based communication interface
- Responsive modern UI built using Tailwind CSS

### 🐍 Backend Socket Programming
- TCP Server and Client implementation
- UDP Server and Client implementation
- Multi-threaded communication
- Real-time message exchange
- Host/Join functionality
- Command-line based networking demonstration
- Uses Python Socket Programming concepts

---

## 📸 Project Preview

### TCP Communication
✅ Reliable Transmission  
✅ Packet Ordering  
✅ Acknowledgment Mechanism  
✅ Guaranteed Delivery

```
Client → Packet 1 → Server
Client ← ACK 1 ← Server

Client → Packet 2 → Server
Client ← ACK 2 ← Server

...
```

### UDP Communication

⚡ Faster Transmission  
❌ No Acknowledgments  
❌ Possible Packet Loss  
❌ Possible Packet Reordering

```
Packet 1 ✓
Packet 2 ✗ Lost
Packet 3 ✓
Packet 4 ✓

Received Message:
H L O
instead of
HELLO
```

---

## 🏗️ Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript (ES6)
- Tailwind CSS

### Backend

- Python 3
- Socket Programming
- Multithreading
- TCP/IP Networking

---

## 📂 Project Structure

```text
tcp-vs-udp-network-simulator/
│
├── index.html
|
|── tcp_udp_chat.py
│
├── README.md

```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/tcp-vs-udp-network-simulator.git

cd tcp-vs-udp-network-simulator
```

---

## 🌐 Running Frontend Simulator

Simply open:

```bash
index.html
```

or

Run using VS Code Live Server.

---

## 🐍 Running Python Backend

### Start Program

```bash
python tcp_udp_chat.py
```

### Menu

```text
===== CHAT MENU =====

1. TCP Chat
2. UDP Chat
3. Exit
```

### TCP Example

#### Machine 1

```text
TCP Chat
Host
```

#### Machine 2

```text
TCP Chat
Join
```

### UDP Example

#### Machine 1

```text
UDP Chat
Host
```

#### Machine 2

```text
UDP Chat
Join
```

---

## 🧠 Networking Concepts Demonstrated

### TCP

- Connection-Oriented Protocol
- Three-Way Handshake
- Reliable Data Transfer
- Flow Control
- Error Checking
- Packet Sequencing
- Acknowledgments (ACK)

### UDP

- Connectionless Protocol
- Faster Communication
- No Delivery Guarantee
- No Packet Ordering
- Lower Overhead
- Suitable for Real-Time Applications

---

## 📊 TCP vs UDP Comparison

| Feature | TCP | UDP |
|----------|------|------|
| Connection | Required | Not Required |
| Reliability | High | Low |
| Ordering | Guaranteed | Not Guaranteed |
| Acknowledgments | Yes | No |
| Speed | Slower | Faster |
| Overhead | Higher | Lower |
| Packet Loss Handling | Retransmission | No Retransmission |

---

## 🎯 Educational Purpose

This project was developed to provide a practical understanding of:

- Computer Networks
- Transport Layer Protocols
- Socket Programming
- TCP/IP Model
- Network Reliability
- Packet Transmission Concepts

It can be used as:

- Academic Mini Project
- Computer Networks Lab Project
- Networking Demonstration Tool
- Learning Resource for Students

---

## 🔮 Future Improvements

- Integrate Python backend with web frontend
- WebSocket-based real-time communication
- Multi-user chat rooms
- Packet latency simulation
- Congestion control visualization
- Three-way handshake animation
- Network topology visualization
- Deployment using Flask/FastAPI backend

---

## 👨‍💻 Author

**Kavyansh Goenka**

Computer Science Student | Networking Enthusiast

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

📢 Share it with others learning Computer Networks

---

## Development Notes

This project was developed with the assistance of AI coding tools for code generation, debugging, and UI design suggestions. All architecture decisions, feature selection, testing, and project integration were performed by the author
