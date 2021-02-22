## Nicole Terry
02/20/21

## Executive Summary 
We will look at network components and different types of network layouts. We will also learn LucidChart to help with visualizing those layouts.
We will explore some encryption technologies and have an intro to cybersecurity.  



## Lucidchart
I have made company org charts before using microsoft word or excel, this is by far much easier. I like this software, it’s intuitive, and I’ll definitely keep it in my repertoire. 

## Introduction to Networking

### Data Transmission
#### Packet: A packet is a unit of data transmitted through the internet.  Packets are made of a header and a payload. The Header information directs the packet to its destination, where the payload is then used by the application.
#### Packet-Switching: Packet switching allows for the router to choose the optimal route and sometimes priority for the packets to get to where they need to go.
#### IP Address: Every device on the internet has a unique IP address. With the implementation of the IPv6, there are 3.4×1038 possible addresses.
#### DNS: DNS stands for Domain Name Server, DNS translates hostnames like www.google.com to an IP address like 216.239.32.0, giving us near instantaneous access to the website.
#### Protocol: The set of rules that govern how communications take place on a network is called Protocol. File Transfer Protocol (FTP) and TCP/IP (transmission-control protocol/Internet protocol) are two well known protocols.

### Networking Hardware
A hub will only detect devices that are connected to it, and incoming data is transmitted to all other devices on the hub. This creates a lot of unnecessary traffic on the network. A switch, on the other hand, is intelligent and can store the MAC addresses of different devices on the network. It will send data to only the intended recipients. 
A router is the gateway of the network, and will forward data from one network to another, based on their IP addresses. 

### Network Topologies
#### Single point of Failure
In a star topology, all machines on the network connect to one switch or hub. This has the advantage that if one wire breaks, it only affects that computer. However if the switch or hub breaks, the entire network goes down. This is called a single point of failure.

#### Infrastructure vs. Wireless Mesh
With Infrastructure Topology, you have the internet connection coming from a modem, then to a router, in this example there are 2 computers that are hardlined to the router. Then from the router, another connection is made to a wireless access point, for all of the wireless devices in the home. This is a fairly standard setup for a home network.
With a Wireless Mesh multiple wireless access points are interconnected with each other to create a seamless internet connection for devices to connect to. 

### Network Design
In my design, the 2 computers and the printer are communicating through the wireless router. This allows either computer to send something to print, via the router. It does have a single point of failure with either the ethernet connection coming in, or the router itself failing. Many home networks are set up this way, and it should work just fine for non-strenuous use.

### NSA/CSS
The Central Security Service is a partnership with the NSA (National Security Agency), branches of the military, and civilian leaders to develop national policy and guidance regarding cybersecurity. 

## Cybersecurity and Encryption

### Information Systems Security

#### Security Triad
Confidentiality - The actual securing of the data. Confidentiality covers a wide range of access controls and procedures that protect your information from unauthorized access. 
Integrity -  The accuracy and completeness of data. For example, in a data breach that compromises integrity, a hacker may seize data and modify it before sending it on to the intended recipient.
Availability -  Availability refers to reliability and system uptime. HAving offsite backups, redundancies, proper monitoring of data are all things that can ensure your data is available for authorized users.

#### Authentication
Three daily tasks that require authentication: 
Logging on to your email
Unlocking/driving your vehicle
Entering your workplace
You can use multifactor authentication to make these all more secure. You can log in to your email using a password as well as an authentication code from something like Google Authenticator. A car could have a proximity key from your phone as well as the physical car key. When entering your workplace building, you could have both a RFID card as well as a biometrics scanner. 

#### ACL and RBAC
ACL stands for Access Control List and RBAC stands for Role-Based Access Control.
ACL’s are easy to maintain, but have the drawback that each resource is maintained separately. This is feasible for a small number of users, or a small number of resources. Adding or removing a user’s permissions for a large number of resources is quite time consuming.
An RBAC allows permissions to be assigned to roles (such as reader, editor, administrator, etc.) instead of individuals. 

#### Ciphertext, Public Key and Private Key

 If a company needs to send encrypted data, they can use Public Key Encryption. To send an encrypted message, you obtain the public key, encode the message, and send it. If the data is intercepted, unless that person also has the private key, they will only be able to see the ciphertext. Once the recipient receives the data, they use their private key to decode it. 

#### Public Key Cryptography
A Public Key allows anyone to encrypt a message, but that encrypted message can only be decrypted with the receiver's private key. This ensures that only the intended recipient can access the data, because they would have the correct private key.

### Cryptography
#### Encryption
"cryptography is a growing field" turns into “etvqitcrja ku c itqykpi hkgnf” with the Caesar cipher.
The Caesar cipher takes the letters in a message, and moves them a pre-agreed on number of spaces up or down to replace the letters with new ones, making the letter look like indecipherable gibberish.

#### Frequency Fingerprint
Frequency fingerprint tracks the usage of different letters in a particular language, and will move the matching “fingerprint” accordingly, hopefully breaking the cipher. Anytime there is a difference in letter frequencies, information is able to be gathered that can help break the code.
#### Polyalphabetic Cipher
A polyalphabetic cipher is any cipher based on substitution, using multiple substitution alphabets. 

#### Polyalphabetic Example
If we map the A to the o, we get something like this:
Plain text: My name is Nicole Terry
Encrypted: YK ZMYQ UE ZUOAXQ FQQDK

#### Brute-Force
A brute-force attack tries every possible decryption key for a cipher. If the person trying to decode the message can tell what kind of cypher is used, they can try all combinations until one makes sense. 

## Conclusion
We learned to use LucidChart, which helped us visualize network layouts. We also learned of various kinds of networks, as well as the need for cybersecurity. We learned about encryption and a few of the methods that are used to secure data.


