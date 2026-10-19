# Complete Linux Training Course

---

## Table of Contents
* [Introduction](#introduction)
* [System Access and File System](#system-access-and-file-system)
    - [Access to Linux System](#access-to-linux-system)
    - [Command Prompt](#command-prompt)
    - [What is Root?](#what-is-root)
    - [Changing Password](#changing-password)
    - [File System Structure and Description](#file-system-structure-and-description)

---

## Introduction

### What is Linux?
* Widely used in servers and cloud computing
* Free software philosophy
* Strong command line interface
* Faster processing
* Enhanced security
* Customization because of open-source nature
* There are different desktop environments like **GNOME, KDE, and XFCE**
* The file systems in use by Linux are **ext4, XFS, and Btrfs**.
* Linux **Kernel** - is NOT an operating system. It is **a small software within Linux** operating system that takes commands from users and pass them to system hardware or peripherals.

### Linux Flavors

![alt text](images/complete-linux-training/2026-10-18_14-44.png)

* **Red Hat** is paid, so if you want a a free and open-source clone, use **CentOS** (but not supported/updated anymore), or use **Rocky Linux**.

---

## System Access and File System

### Access to Linux System
* Console (local)
* Remote
    - **RDP**: Windows to Windows
    - **Sharing**: Mac to Mac
    - **Putty Client**: Windows to Linux
    - **SSH**: Windows to Linux, Mac to Linux, Linux to Linux
        - `ssh username@remote_host_ip`
        - `ssh -i ~/.ssh/my_private_key username@remote_host_ip`
        - `ssh username@remote_host_ip "df -h"` - If you want to run a quick command on the remote server without staying logged in.
    - Note: To get the IP address of the Linux Machine, run:
        - `ifconfig` (old version) or `ip a`

        ![alt text](images/complete-linux-training/2026-10-19_18-53.png)

<br>

### Command Prompt

![alt text](images/complete-linux-training/2026-10-19_19-01.png)

- `whoami`: shows the current username
- `hostname`: shows the hostname
- `ctrl + C`: to get your prompt back

<br>

### What is Root?
There are 3 types of root on Linux system:
1. **Root account**: root is an account or a username on Linux machine and it is the most powerful account which has access to all commands and files.

2. **Root as /**: the very first directory in Linux is also referred as root directory.

3. **Root home directory**: the root user account also has a directory located in /root which is called root home directory.

<br>

### Changing Password
* `passwd`: change the password of the current user. This will ask for your old password then input a new password.
* `passwd <userid>`: Only for root user, you can change other username's password. Example: `passwd jsalonga`
* `ctrl + D`: if you want to exit the passwd command.

<br>

### File System Structure and Description

![alt text](images/complete-linux-training/2026-10-19_20-03.png)

<br>