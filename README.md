# Reverse-Shell

## Description

Built a reverse shell using python to simulate an event where a malicious attacker gains access to a system and attempts to exfiltrate sensitive/confidential information. The testing environment for this simulated attack was done via two computer within the same network.

## Learning outcomes
- Used python to create a server on the attackers' machine, which send requests to retrieve system information of the victim by leveraging windows commands such as: cd, ipconfig, netstat, etc..
- Used python to create a client on the victims' machine, that receives requests from the server, processes the request, and sends the result containing system information of the victim device for retrieval to the attacker via the server
- Used python to give the server file extraction privileges, allowing sensitive files to be exfiltrated from the victim's machine to the attacker

## Getting started
- [Build your own reverse shell and more!](https://thepythoncode.com/article/create-reverse-shell-python#google_vignette)

## Prerequisites

 This project will require the python library:
 ```sh
   pip3 install tqdm
