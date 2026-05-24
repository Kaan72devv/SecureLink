# SecureLink

SecureLink is a Python-based encrypted client-server communication system built with sockets and symmetric encryption.

The project was created to practice:
- socket programming
- encrypted communication
- packet-based data transfer
- multi-client architecture
- networking fundamentals
- Python backend development

SecureLink uses encrypted JSON packets between clients and the server using Fernet encryption from the `cryptography` library.

---

# Features

- Encrypted client-server communication
- JSON packet system
- Multi-client support
- Thread-based connection handling
- Real-time message transfer
- Modular project structure
- Expandable architecture

---

# Technologies Used

- Python
- Socket
- Threading
- JSON
- Cryptography (Fernet)

---

# How It Works

The client:
1. Takes user input
2. Creates a JSON packet
3. Encrypts the packet
4. Sends encrypted data to the server

The server:
1. Accepts client connections
2. Receives encrypted packets
3. Decrypts incoming data
4. Parses JSON packets
5. Displays received messages

---

# Communication Flow

```text
Client
 ↓
JSON Packet
 ↓
Encryption
 ↓
Socket Transfer
 ↓
Server
 ↓
Decryption
 ↓
Packet Parsing
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Kaan72devv/SecureLink.git
```

Move into the project directory:

```bash
cd SecureLink
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Usage

Start the server:

```bash
python server.py
```

Start the client:

```bash
python client.py
```

You can run multiple clients simultaneously.

---

# Encryption

SecureLink uses Fernet symmetric encryption provided by the `cryptography` package.

The same shared key is used by:
- the client
- the server

to encrypt and decrypt packets securely.

---

# Packet Example

Example packet before encryption:

```json
{
  "client": "client1",
  "message": "Hello"
}
```

The packet is converted into JSON format and encrypted before being sent through the socket connection.

---

# Future Improvements

Planned features for future versions:

- Authentication system
- Database integration
- GUI client
- File transfer support
- Command system
- Packet headers
- Logging system
- Web dashboard
- API integration
- RSA/AES hybrid encryption
- Docker support

---

# Educational Purpose

This project was created for educational and development purposes to improve networking and cybersecurity related programming skills.

---

# License

MIT License
