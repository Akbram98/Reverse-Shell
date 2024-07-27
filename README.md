# Reverse-Shell

## Description

Developed a reverse shell using Python to simulate a scenario in which a malicious attacker gains access to a system and attempts to exfiltrate sensitive information. The testing environment for this simulated attack consisted of two computers within the same network.

## Learning outcomes
- Developed a Python-based server on the attacker's machine to send commands and retrieve system information from the victim's device using Windows commands like **`cd`**, **`ipconfig`**, and **`netstat`**.
- Created a Python client on the victim's machine to receive and execute commands from the server, processing the requests and sending back the system information to the attacker.
- Implemented file extraction capabilities in the Python server, enabling the exfiltration of sensitive files from the victim's machine to the attacker's machine.

## Getting started
- [Build your own reverse shell and more!](https://thepythoncode.com/article/create-reverse-shell-python#google_vignette)

## Prerequisites

 This project will require the python library:
 ```sh
   pip3 install tqdm
