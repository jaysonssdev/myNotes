# Practical Help Desk Course
---
## Table of Contents
* [Intro to Information Technology](#intro-to-information-technology)
* [Intro to Computing](#intro-to-computing)
* [Computer Components and Repair](#computer-components-and-repair)
* [Operating Systems](#operating-systems)
* [Virtualization](#virtualization)
* [Windows](#windows)
* [Linux](#linux)
* [Networking](#networking)

---

<br>

## Intro to Information Technology

* **Information technology (IT)** is the use of computers, software, networks, and electronic devices to create, store, process, retrieve, and exchange data.

### IT Department
* Manages and supports the technology required for the organization to function.
* **IT Department Responsibilities** can vary between orgs.
    - Infrastructure Management
    - Tech Support
    - Security
    - Data Management
    - Identity and Access Management
    - Project Management
    - Compliance and Governance
* **Sample Org Chart**

![alt text](images/practical-helpdesk/2026-10-29_19-43.png)

* **Help Desk Responsibilities:** Individual contributor responsible for providing technical support and assistance to end-users, either within an organization or to customers.
    - Front line tech Support
    - Troubleshooting
    - Password and account management
    - Customer service
    - Escalation of support
    - Fixing or installing hardware
    - Installing and configuring software
    - Maintain and create documentation

<br>

---

<br>

## Intro to Computing

### The Binary System

![alt text](images/practical-helpdesk/2026-10-30_22-17.png)

### Bits and Bytes
* 4 bits = nibble
* 8 bits = 1 byte

![alt text](images/practical-helpdesk/2026-10-30_22-26.png)

### Encoding

![alt text](images/practical-helpdesk/2026-10-30_22-34.png)

* **ASCII**: American Standard Code for Information Interchange

![alt text](images/practical-helpdesk/2026-10-30_22-40.png)

* **UTF**: Unicode Transformation Format -- an extension of ASCII, so we can add emojis, etc.

### How a Computer Computes

#### Logic Gates
* By stacking them together we can have the logic gates perform basic computations.

![alt text](images/practical-helpdesk/2026-10-30_23-03.png)

* Each processor has what's called an instruction set. We can then store these instructions in some sort of external memory and have our processor run through them.

![alt text](images/practical-helpdesk/2026-10-30_23-22.png)

<br>

---

<br>

## Computer Components and Repair
* **Electro Static Discharge (ESD)**
    - just a small shock to humans but can be damaging to hardwares (computers). To prevent it is to use an **ESD mat** (made of rubber), or ground yourself by touching a large metallic surface.

* **Central Processing Unit (CPU)**
    - In desktop computers you're generally going to see one of two CPU manufacturers, it's either going to be **Intel or AMD**.
    - A **CPU core** is a physical hardware processing unit on a computer chip, while a **CPU thread** is a virtual or logical sequence of instructions that a core handles.

* **Random Access Memory (RAM)**
    - is the **temporary** memory that's used in the computer.
    - make sure that you put the right **DDR** that is compatible to your motherboard.

* **Drives**
    - An **HDD (Hard Disk Drive)** uses spinning magnetic platters and a mechanical arm to read and write data, like a tiny record player. An **SSD (Solid State Drive)** uses flash memory chips with no moving parts, working much like a giant USB thumb drive.

* **Power Supply Unit (PSU)**
    - **Wattage** measures the total power the PSU can deliver.
    - an **80 Plus Gold or Bronze rating** is usually the sweet spot for price and performance.

* **Graphical Processing Unit (GPU)**
    - VRAM (Video RAM): This is the GPU's dedicated memory.
    - 12GB to 16GB of VRAM is highly recommended for modern gaming.

* **Motherboard (MOBO)** 
    - it connects all your components and determines how much you can expand or upgrade your system in the future.
    - it is important to know the compatibilities of your components.
    - Form Factor (Size):

    ![alt text](images/practical-helpdesk/2026-10-31_14-42.png)

* **POSTing and the BIOS**
    - **POST (Power On Self Test)** - it's essentially a set of tests that the **BIOS (Basic Input Output System)**, or the firmware for the motherboard, runs when it powers on to make sure that everything in the computer is okay.

<br>

---

<br>

## Operating Systems
* **Abstraction**: The OS hides the complex, messy details of physical hardware and presents clean, simplified logical interfaces to applications and users.
* **Arbitration**: The OS manages, coordinates, and controls how finite hardware resources are shared among multiple competing programs, users, or devices.

![alt text](images/practical-helpdesk/2026-10-31_21-50.png)

### File Systems
* is a set of data structures, rules, and methods that an operating system uses to organize, store, name, and retrieve data on a **persistent storage** device (such as an HDD, SSD, or flash drive).

#### Common File System Types
* **NTFS:** The standard default file system for Microsoft Windows.
* **APFS:** The primary file system used by Apple macOS devices.
* **ext4:** The common default file system for Linux distributions.
* **exFAT:** A cross-platform file system ideal for flash drives and external drives shared between Windows and macOS.

### File Types / Extensions
- is a short suffix (usually 2 to 4 letters) at the end of a computer file name—separated by a period—that identifies the file's format and tells the operating system which program to use to open it.

<br>

---

<br>

## Virtualization
We will virtualize an entire computer, which are often referred to as **virtual machines (VM)**.

### Hypervisor
Its responsibility is to partition up and allocate out the resources to the virtual machines.

- **Type 1**: is directly installed on the bare metal. It is more efficient than Type 2 because we're **not wasting any resources to run a base OS**.

    ![alt text](images/practical-helpdesk/2026-10-31_22-49.png)

- **Type 2**: is for personal use only. It is installed on top of a base OS.

    ![alt text](images/practical-helpdesk/2026-10-31_22-41.png)

### Containers
The main difference between a container and a virtual machine is that **a virtual machine is intended to virtualize an entire computer**, where a **container is intended to virtualize just a single application**. And inside of that container, we only contain the things that are needed to actually run that application.

<br>

---

<br>

## Windows

### Local and Domain Accounts

#### Local Accounts
* exists and is managed on a single, specific machine.

#### Domain Accounts
* is stored centrally on a network server (such as Active Directory) and works across multiple computers joined to that domain.

![alt text](images/practical-helpdesk/2026-11-01_14-28.png)

<br>

### Administering Local User Accounts

* Go to **Settings -> Accounts** 
* or **Control Panel -> User Accounts -> User Accounts**
* or **run -> lusrmgr.msc**

#### Users

![alt text](images/practical-helpdesk/2026-11-01_15-02.png)

- **Administrator:** by default, this account actually gets disabled after Windows installs itself
- **andrew:** Windows actually sets the user account that we create first as an administrative account (in this example it was andrew)
- **Properties**: Double-clicking these users shows their **Properties**
    - General tab: You can do some password related options here.
    - MemberOf tab: You can see and add the group/s where this user belongs to.
- **New User**: you can right-click here and choose a **New User**

#### Groups

![alt text](images/practical-helpdesk/2026-11-01_15-34.png)

* There are groups here that have certain sets of permissions for specific tasks, and then just add our users to those groups.

<br>

### Local File Permissions

#### Folder Permission

* Note: In Windows by default when we create folders they're going to inherit the properties of their parent (ex. C: drive) and same with if we add any files to those folders. To disable this, click the **Advanced** button to **Disable Inheritance** -> **Remove all inherited permissions from this object.** -> **Apply**

1. Right-click the folder -> Properties.
2. Go to Security tab.
3. To change the permissions on a group, click **Edit**.

![alt text](images/practical-helpdesk/2026-11-01_19-52.png)

4. Or add or remove users/groups for this folder.

<br>

### Windows Logs and Event Viewer
* Start Menu -> then type `Event Viewer`
* **Critical** and **Error** are going to be probably the most important ones that we will want to take a look at.
    - Click the `+` then double-click the event to see more details about it.

    ![alt text](images/practical-helpdesk/2026-11-02_13-48.png)

* **Windows Logs**
    - You can filter these logs if you're looking for something in particular.

    ![alt text](images/practical-helpdesk/2026-11-02_14-24.png)

<br>

### Device Manager
* Start Menu -> then type `Device Manager`
* Example task: Add a printer that is accessible from the network:
    - In Device Manager -> Action tab -> **Devices and Printers**
    - Click the **Add a printer** (located beside the 'Add a device')
    - Double-click the detected printer that you want to add. 

<br>

### Windows Services
* We access it thru Task Manager -> Services tab -> `Open Services`
* or Start Menu -> then type `Services`
* **Windows Services** is a program that runs in the background and it operates without any user interaction or having a user interface.
* Sometimes developers will want certain processes or applications to just automatically run that don't need user interaction to take care of their task.
* Can set a task to run automatically, or manually, or start or stop it, etc.

<br>

### Windows Registry
* Start Menu -> Registry Editor
* The **registry** is actually just **a database that stores configuration settings for the operating system and applications that are installed**.
* A lot of settings in Windows and applications actually have user interfaces that allow us to easily make changes to the configuration of the application.
* It is organized by **KEYS** (that has subkeys) and **VALUES**.

<br>

### Windows Cmd Prompt
* Start Menu -> `cmd`
* **Batch scripting**: is the scripting language that Windows cmd uses.
* Some common commands:
    - `dir`: lists the content of the current directory
    - `cls`: clear screen
    - `cd`: change directory
    - `ipconfig`: shows your network configuration
    - `/?`: shows the help menu of a command. Example: `ipconfig /?`
    - `/` or `-`: adds options to a command. Eaxmple: `ipconfig /all`, `ping -n 12 8.8.8.8`
    - `ctrl + C`: halts an operation or a command
* If you open cmd as a standard user only you won't be able to access some files/directories due to permissions, even if your current user has admin priviledges. **Run as administrator** so that you'll have admin priviledges in cmd.

<br>

### Windows Task Scheduler
* Start Menu -> `Task Scheduler`

![alt text](images/practical-helpdesk/2026-11-02_19-20.png)

* On the right side panel you can see the **Actions** that you can do, like **Create Task...**
* You can add new tasks to automate like Disk Clean Up, etc.

<br>

---

<br>

## Linux

### GNU/Linux and Distros
* **Kernel** is responsible for **interfacing between the hardware and the applications** and software that actually run on top of it.

* **Full operating system** need the things like the applications, the software, the file system, and some sort of desktop user interface **that runs on top of the kernel**.

* **Linux** is only the kernel of the operating system. The **GNU** accounts for the other parts of the OS, like the applications and file system that **run on top of the kernel** to make it a complete OS.

* **Distros** are different variations of Linux. A Linux distro is generally made up of:
    - **Linux kernel**
    - **Packages** which are the software or application that run on top of it
    - **Package Manager** which is used to install, update, or otherwise manage the packages
    - **Desktop UI** so that users can interact with it.
        - Gnome


<br>

### Linux Filesystem Hierarchy

![alt text](images/practical-helpdesk/2026-11-03_11-56.png)

* **bin**: short for *binaries*, this folder contains the majority of the binaries or as they're sometimes referred
to **executables commands**.

* **sbin**: short for *system binaries*, these are binaries that are only expected **to be used by the root or super user**.

* **lib**; short for *libraries*, this contains all of the libraries that those binaries are going to make use of (these are the dependencies or external code that those binaries require)

* **usr**: these are user files or executables that are not required for the operation of the operating system itself but are to be used by the end user.

* **etc**: short for *editable text configuration*, this conatin files to configure the various binaries and even things in the operating system.

* **home**: this has the users' home directories, which contains the user's config files, etc.

* **dev**: this contain files that represent devices.

* **boot**: this contain all the required files of linux to boot up.

* **opt**: this is designed to be a folder where we could install optional softwares

* **tmp**: this is where both the OS or user can write temporary files, which does not persist after a reboot.

* **var**: short for *variables*,this folder is going to store variables that the operating system needs while it's in use.

* **proc**: short for *process*, what it is for is actually for the OS to keep track of all of the processes that are running so that's why you'll see a bunch of numbers.

<br>

### Linux File Permissions

![alt text](images/practical-helpdesk/2026-10-20_12-36.png)

![alt text](images/practical-helpdesk/2026-10-20_14-13.png)

![alt text](images/practical-helpdesk/2026-11-03_14-20.png)

### Common Commands

#### `adduser`
- to add a new user
- Example: `sudo adduser jayson`

#### `addgroup`
- to create a new group
- Example: `sudo addgroup confidential`

#### `usermod`
- to add a user to a group
- Example: `sudo usermod -a -G confidential jayson`

#### `passwd`
- to change or expire the password
- Example: `sudo passwd --expire jayson` to make jayson's password expire and will require him to give a new one

#### `chmod`
* to change file permission 
* Example: `sudo chmod 700 test.txt` means that the **owner** will have all the permissions on the file (read, write, execute) (4 + 2 + 1), while the **group** and **world** has none (0 + 0 + 0), resulting to `-rwx------`

#### `chown`
* to change the owner of the file
* Example: `sudo chown root test.txt`

#### `chgrp`
* to change the group of the file
* Example: `sudo chgrp root test.txt`

#### Note: Directories are generally executable

![alt text](images/practical-helpdesk/2026-11-03_14-38.png)

<br>

### Scheduling Tasks with Cronjobs
* `crontab -l`: to list all the cronjobs of the current user 
* `crontab -e`: to edit the cron config file of the current user

![alt text](images/practical-helpdesk/2026-11-03_19-13.png)

#### Cron Syntax

![alt text](images/practical-helpdesk/2026-11-03_19-24.png)

#### Cron Characters

![alt text](images/practical-helpdesk/2026-11-03_19-25.png)

#### Cron examples:

![alt text](images/practical-helpdesk/2026-11-03_19-26_1.png)

![alt text](images/practical-helpdesk/2026-11-03_19-26.png)

![alt text](images/practical-helpdesk/2026-11-03_19-27_1.png)

![alt text](images/practical-helpdesk/2026-11-03_19-27_2.png)

![alt text](images/practical-helpdesk/2026-11-03_19-27.png)

![alt text](images/practical-helpdesk/2026-11-03_19-28_1.png)

![alt text](images/practical-helpdesk/2026-11-03_19-28.png)

#### Run a cronjob as root for another user
* while logged in on your target user, run: `sudo crontab -u root -e`

![alt text](images/practical-helpdesk/2026-11-03_19-36.png)

<br>

### Upgrading and Installing Packages (also known as softwares)

* `sudo apt update`
    - **apt** is the package manager for debian and debian-based distros 
    - **dnf** is the standard package manager for Fedora, Red Hat Enterprise Linux (RHEL), Rocky Linux, and AlmaLinux
    - does not install or upgrade any software. It only refreshes your computer's local list of available packages and versions from the internet.

* `sudo apt upgrade`
    - installs the newer versions of the software you already have installed, based on that refreshed catalog. If an update requires removing something else, it skips it.

* `sudo apt full-upgrade`
    - performs a complete system upgrade. Like a standard upgrade, it installs new versions, but **it is smart enough to handle complex changes**.

* `sudo apt install <software name>`
    - used to install a new software that should be available from that package.

* `sudo apt remove <software name>`
    - used to uninstall a software.

<br>

---

<br>

## Networking

### Intro to Networking

![alt text](images/practical-helpdesk/2026-11-04_13-29.png)

* `ipconfig`: a Windows command to view all IP addresses and interfaces.
* `ip a` or `ifconfig`: a Linux command to view all IP addresses and interfaces.

#### Private IP Addresses
* 10.0.0.0 - 10.255.255.255 - usually used on commercial local networks
* 172.16.0.0 - 172.31.255.255
* 192.168.0.0 - 192.168.255.255 - usually used on home networks

#### DNS Look Up
* `nslookup`: a linux/windows command to see the public ip address/es of a domain name. Example: `nslookup www.google.com`

<br>

### The OSI Model 
* OSI stands for **Open Systems Interconnection**
* Not a protocol itself, more of a guide
* Useful for communication between IT professionals and
troubleshooting (shared understanding of complex system)

![alt text](images/practical-helpdesk/2026-11-04_14-49.png)

#### Layer 1: Physical
* Refers to the **actual signals** being used to transmit the data
* Voltage (bits on the wire), Light, Radio Frequency (RF)
* Layer 1 issues include **unplugged/damaged cable** or connectors or **weak wireless signal**


![alt text](images/practical-helpdesk/2026-11-04_15-02.png)

#### Layer 2: Data Link
* Transmit data directly **between two devices**
* Sometimes referred to as the **switching layer**
* Data Unit: **Frame**
* This layer is responsible for getting frames (the data) between two devices
* **Performs collision detection and prevention**
* Uses **MAC addresses** to communicate
* Networking Eguipment: **NIC** and **Switch**

#### Layer 3: Network
* Responsible for **getting data throughout a network(s)** from one destination to another
* Networking layer addresses **segments of data with IP addresses to create a packet**
* Responsible for **actual routing of data** through the network
* Determining **best path** (routing) for data.
* Data Unit: **packet**
* Uses **IP addresses**.
* Networking eguipment: **Router** and **NIC**

#### Layer 4: Transport
* Responsible for **breaking data streams down into segments** that can be transmitted
* Handles **flow control** so data is not sent too fast (or too slow)
* Performs **error checking via a checksum to receiver** can verify segment integrity
* Data unit: **Segment**
* Uses **UDP** or **TCP**
    - UDP (User Datagram Protocol): 
        - Connectionless protocol that **doesn't use acknowledgements**
        - Sends traffic out and doesn't care if receiver gets it (**faster**)
        - **Good for time-sensitive applications like gaming or streaming**
    - TCP (Transmission Control Protocol):
        - Connection based protocol that **checks data if received**
        - Uses a **3-way handshake** to acknowledge data is received correctly
        - Is **slower** than UDP but **better suited when integrity is important**, like **downloading a file**

#### Layer 5: Session
* Responsible for **creating and managing separate communication channels between devices aka sessions**
* When communicating with a server **multiple sessions may be opened** to receive files in parallel
* Can be used to **resume interrupted communication**
* Handled by the **web browser**

#### Layer 6: Presentation
* Responsible for **translating data between human readable formats and computer readable**
* Performs **compression**
* Responsible for **encryption of data**
* Also handled by **web browser** 

#### Layer 7: Application
* Comprised of the protocols that we interact with or the **“applications” we use interact with HTTP, POP3, SSH, Telnet**
* If you're interacting with it or see it on your screen it's most likely layer 7
* Also handled by the **web browser**

<br>

### Network Addresses and Subnet Masks
* We can have addresses in the range of anything **from 0.0.0.0** all the way up **to 255.255.255.255**  -- there are sets of IP addresses inside of this range that are reserved for specific things:
    - **Network Address**: the first IP address. Example: **192.168.50.0**
    - **Default Gateway**: the IP address of the Router. Example: **192.168.50.1**
    - **Broadcast Address**: the last IP address. Example: **192.168.50.255**
    - **Subnet Mask**: tells us which portion of the IP address is actually for the network address and then which portion of that IP address are free to be used for the host address.
    
    ![alt text](images/practical-helpdesk/2026-11-04_19-11.png)

    ![alt text](images/practical-helpdesk/2026-11-04_19-39.png)

<br>

### CIDR Notation
* CIDR = **Classless Interdomain Routing**
* CIDR Notation = Shorthand to write out IP and Subnet Mask
* Examples:

![alt text](images/practical-helpdesk/2026-11-04_19-55.png)

![alt text](images/practical-helpdesk/2026-11-04_19-59.png)

**Note:** A valid Subnet Mask should have 0s all the way to the end (contiguous)

![alt text](images/practical-helpdesk/2026-11-04_20-03.png)

<br>

### Hubs, Switches and ARP

#### Hubs
* Hubs are obsolete because when a hub receives a data packet on one port, it blindly broadcasts that data out to every other port and connected device.

![alt text](images/practical-helpdesk/2026-11-04_20-50.png)

#### Crossover Cable
* For connecting just 2 devices.

![alt text](images/practical-helpdesk/2026-11-04_20-39.png)

#### Switch

![alt text](images/practical-helpdesk/2026-11-04_20-58.png)

* **Unamanaged Swicth**: All ports are identical.

![alt text](images/practical-helpdesk/2026-11-04_20-07.png)

* **Managed Switch**: Allows us to perform some **configuration like VLAN**. You'll also be able to set things like **mirroring ports**.

![alt text](images/practical-helpdesk/2026-11-04_20-10.png)



#### ARP
* ARP (Address Resolution Protocol) is the digital translator that **connects an IP address to a MAC address** (physical device)
* `arp -a`: is a linux/windows command to see the **arp table**

<br>

### Routers
* **Switches** are used to create networks and **routers** are used to connect networks together.

![alt text](images/practical-helpdesk/2026-11-04_21-51.png)

<br>

### Ports
*  A **port** is a **virtual slot** used by an operating system **to direct network traffic to specific applications or services**.
* **Firewalls** use ports to block or allow data, securing your device from unwanted access.
* Common Examples:

![alt text](images/practical-helpdesk/2026-11-04_22-16.png)

- **Note:** For web servers, they usually open port 443 to listen for incoming requests from the user.

- **Note:** We can have ports for both TCP and UDP and those are separate ports apart from each other.

![alt text](images/practical-helpdesk/2026-11-04_22-32.png)

- **Notes:**
    - `netstat -tulpna`: a linux command to see the open ports in your machine.
    - `127.0.0.*` - local host (loop back addresses), which doesn't listen from extenal connections.
    - `0.0.0.0` - means that we're listening on all IPv4 addresses
    - `192.168.50.7:68` - this is an example of an ESTABLISHED coonection to the router (192.168.50.1:67) - and these ports **67 and 68 are associated with DHCP** - the basics of this protocol is that it is what allows us to get an IP address from the router.

<br>

### VPN (Virtual Private Networks)
* Used to create an encrypted channel (usually) over the internet between a client and server
* Multiple use cases
* Connect to another LAN through the internet
* Additional security for traffic over the internet
* Increased anonymity on the internet

#### Remote LAN Connection
* Used to allow a remote computer to tunnel into a LAN through the VPN server
* Frequently used to allow remote workers to access an office LAN and internal resources
* VPN client device will receive a LAN IP of the remote network
* For the most part the client can communicate as if it were physically on the LAN
* Traffic still encrypted over the internet, even if LAN

![alt text](images/practical-helpdesk/2026-11-04_23-01.png)

<br>

### OpenVPN Client (Plus how to connect to TCM Exam Platform)

#### Windows Setup
1. Go to https //openvpn.net/client/
2. Click **Download OpenVPN Connect for Windows**
3. Install.
4. Download the `.ovpn` file from https //exams.tcmsecurity.com

![alt text](images/practical-helpdesk/2026-11-04_23-22.png)

5. Upload file on OpenVPN app.

#### Linux CLI
1. Download the `.ovpn` file from https //exams.tcmsecurity.com
2. Go to the folder where you downloaded the file.
3. `sudo openvpn --config <ovpn file>`

<br>

### Network Troubleshooting Commands (Windows)

* Start Menu -> Command Prompt (Run as Administrator)

* `ping <ip address or url>`: to check if you have a connection to the specified ip address. Good for checking **layer 3** network connections. Example: `ping 192.168.50.1`, or `ping www.google.com`
    - Note: One thing to keep in mind is that some devices actually will be configured to not respond to ping messages by default for security issues.

* `ipconfig`: to see both our IP address, the subnet mask and the default gateway.
    - `ipconfig /all`: to see more details like the mac address, etc.
    - `ipconfig /release`: sometimes releasing your current ip address and getting a new one can fix some networking issues on our network. Then run `ipconfig /renew` to have a new ip address.
    - `ipconfig /displaydns`: to get a bunch of details back for the various DNS records we have.
    - `ipconfig /flushdns`: to flush the DNS Resolver Cache. Then run `ipconfig /registerdns` to get a fresh register of DNS.
    - `ipconfig --help`: to see more ipconfig options

<br>

---