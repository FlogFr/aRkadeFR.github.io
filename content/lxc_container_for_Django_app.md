Title: Infrastructure for 1Avis.fr: LXC container for Django web application
Date: 2014-06-24
Category: 1avis
Tags: 1Avis.fr, aRkadeFR, LXC, web server, sysadmin
Slug: 1Avis-fr-LXC-container-for-Django-app
Author: aRkadeFR
Summary: setup LXC container for dev/staging/prod with Django web framework


# 1Avis.fr, the project and infrastructure

First article of the series for 1Avis.fr, focusing on the infrastructure.

The goal of this series of article aims to keep you up to date with the project
1Avis.fr. This project is built on top of Django web framework.

After couple of months reading articles about Django, and how to scale web
application, my turn to implement a solution.

Very simple diagram to explain my view about a good infrastructure for Django
project:

![Project Infrastructure](/images/Infrastructure.png)

Some keywords about the infrastructure:

* Scalable thanks to container
* All application into container as Debian package
* Isolation of every part of the infrastructure

I wanted to use container for these reason:

* easy deployable even on laptop for development / staging
* easy scalable with a front proxy
* force the sysadmin to use Debian tools

# Setting up the LXC container

LXC provides a lightweight virtualization, and enable every one under Linux to
have the same "box" for development.

To install LXC, I referred to the very good [Debian Wikipedia.](https://wiki.Debian.org/LXC)
I installed it under a [kimsufi](https://www.kimsufi.com/fr/index.xml). You
have to upgrade the kernel. I'm using the 3.14.7 from [OVH](ftp://ftp.ovh.net/made-in-ovh/bzImage/).
The installation and setup is straightforward.

## Create the container

You'll notice that the Debian basic container that you can create is very empty.
To change this, you can go into the LXC template for adding some package to your
container (122:/usr/share/lxc/templates/lxc-Debian). Watch out of the LXC cache
into /var/cache/lxc/, you need to erase it for your changes to be taken into
account.

## Network

### Container
After starting and stopping your container to test it, you need to setup the
network.

The requirements are:

* The container needs to communicate with the outside world (we can setup a
  better firewall afterwards)
* The host and the container needs to communicate
* Containers doesn't need to see each other

A [good article](http://l3net.wordpress.com/2013/11/03/Debian-virtualization-lxc-debootstrap-filesystem/)
explains how to setup your network with a bridge between the host and the
container.

This is exactly what I want. I change the container configuration
(/var/lib/#NAME\_CONTAINER#/config) with this network setup:

	lxc.network.type = veth
	lxc.network.flags = up
	lxc.network.link = br1
	lxc.network.hwaddr = 4a:49:43:49:79:bf
	lxc.network.ipv4 = XX.XX.XX.1/24
	lxc.network.ipv4.gateway = XX.XX.XX.254
	lxc.network.ipv6 = XXXX:XXX:X:X:XXXX:XX:XX:XXXX

After restarting, the container will try to find the bridge _br1_, take the IP
XX.XX.XX.1, and have as the default gateway XX.XX.XX.254.

### Host

We need to prepare the host. I suggest to do it live, then change the
configuration to have the same setup after a reboot.

The tools you will use are:

* _brctl_ from the Debian package _bridge-utils_
* _ip_ from the Debian package _iproute_
* _iptables_ from the homonym Debian package

We create the _br1_ bridge with _brctl_. Then we address the IP XX.XX.XX.254 with _ip
address_ to the bridge.

Then we need to setup the Debian firewall. This is done with the _iptables_
command.

We tell the kernel to flush all the _iptables_ with `iptables -t nat -F && iptables -F`.
Then setup the eth0 interface as a _nat_ interface:

	iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

To forward the port 80 to the container, just add the port forwarding rule:

	iptables -t nat -A PREROUTING -p tcp -d XX.XX.XX.XX --dport 80 -j DNAT --to 10.0.0.2

Checking everything:

	root@container1:~# ip route
	default via XX.XX.XX.254 dev eth0 
	...

	root@host:~# iptables -t nat -L
	...
	Chain POSTROUTING (policy ACCEPT)
	target     prot opt source               destination         
	MASQUERADE  all  --  10.0.0.0/24          anywhere  

	root@host:~# iptables -t nat -L
	XX: br1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP 
	...
    inet XX.XX.XX.254/24 scope global br1
	...
	XX: vethSjT4bq: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master br1 state UP qlen 1000

	root@Debian1:~# ping XX.XX.XX.254
	PING XX.XX.XX.254 (XX.XX.XX.254) 56(84) bytes of data.
	64 bytes from XX.XX.XX.254: icmp_req=1 ttl=64 time=0.200 ms
	root@Debian1:~# ping 8.8.8.8
	PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
	64 bytes from 8.8.8.8: icmp_req=1 ttl=47 time=9.56 ms

We have so far a good basic setup.

