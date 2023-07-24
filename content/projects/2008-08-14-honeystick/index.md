---
title: "Honeystick"
date: "2008-08-14"
---

Honeystick is a bootable Honeynet from a USB device. It includes both the Honeywall and honeypots from a single, portable device. Developed and maintained by the UK Honeynet Project.

Homepage is available here: [http://www.ukhoneynet.org/research/honeystick-howto/](http://www.ukhoneynet.org/research/honeystick-howto/)

 

## **What is a HoneyStick then?**

* * *

A HoneyStick is a portable honeynet demonstration and incident response tool – an complete OS platform, GenIII honeywall and one or more honeypots on a single bootable USB stick.

 

## **Why is a HoneyStick useful?**

* * *

If you have ever wanted to quickly demo a honeynet system to someone but didn\`t have a full set of demo kit handy, or they didn\`t want to sacrifice one or more of their physical systems, or VMWare was just too much time to justify it (and they didn\`t have media, patches, disk space handy, etc, then a HoneyStick will be very useful.

Also, if you have ever been involved in incident response and really wanted to quickly spin up a honeypot in a potentially compromised environment, HoneySticks also come in handy too.

 

## **So where can I download HoneyStick?**

* * *

Not quite so straight forward – we can’t distribute an entire downloadable HoneyStick image as some software needs licensing. We can however make full build instructions available here…

 

## **What do I need to get started building my own HoneyStick?**

* * *

Three mains things are required:

- A Debian system (ideally Sarge) with Internet access
- A bootable 2GB USB keyfob
- 30 minutes
- basic UNIX skills and some experience of the Honeynet Project’s tools

 

## **Can you recommend a cheap 2GB USB stick?**

* * *

We use EasyDisk USB2.0 2GB devices from Dabs in the UK:

[http://www.dabs.com/productview.aspx?Quicklinx=3KQG&CategorySelectedId=11152&PageMode=1&NavigationKey=11152](http://www.dabs.com/productview.aspx?Quicklinx=3KQG&CategorySelectedId=11152&PageMode=1&NavigationKey=11152 "http://www.dabs.com/productview.aspx?Quicklinx=3KQG&CategorySelectedId=11152&PageMode=1&NavigationKey=11152")

 

## HowTo

* * *

### Initial Preparations

1. Check your USB device is definitely bootable, and that your PC/laptop supports booting from it (USB-ZIP or USB-HDD usually need enabling in the BIOS as the initial boot device.
2. Check that your Debian system has the following packages installed (and add them using apt-get if it doesn\`t):
    - debootstrap
    - reiserfsprogs
    - grub-install
    - cramfs support
3. Check that you have working Internet access (or a local Debian repository), as you will need to download a number of .deb packages.

### Building your own HoneyStick

**Step #1**

Create a single partition and Reiser file system on your USB device and mount it:

mkdir /mnt/usb /mnt/initrd /tmp/cramfs
fdisk /dev/sda1
mkfs -t reiserfs /dev/sda1
mount /dev/sda1 /mnt/usb

ReiserFS is good because it is journaled and doesn\`t make uncessary writes to your USB device (reducing operating life).

**Step #2**

Set up an initial Debian Sarge environment on the HoneyStick:

debootstrap sarge /mnt/usb

**Step #3**

Install a boot loaded on the HoneyStick:

grub-install --root-directory=/mnt/usb /dev/sda

Use the “–recheck” option, if required.

**Step #4**

Set up apt sources:

cp /etc/apt/sources.list /mnt/usb/etc/apt

**Step #5**

Chroot into the new HoneyStick environment and begin configuration work by updating and patching using apt:

chroot /mnt/usb
mount -t proc /proc proc
apt-get update
apt-get upgrade

**Step #6**

You already have a very minimal Debian Sarge environment, but some additional software packages are required for HoneyStick operation. Add them using apt:

apt-get install mdetect read-edid hotplug nmap tcpdump mozilla-browser vim gcc make x-window-system-core xdm xterm fluxbox localepurge deborphan debfoster kernel-headers-2.6.8-2-386 kernel-image-2.6.8-2-386

Select “n” to not stop on init warning.

**Step #7**

Set up the environment:

vi /etc/hostname
passwd root

Suggested initial values are:

Hostname = honeystick Password = honey

**Step #8**

Clean up after yourself:

deborphan
apt-get clean
rm -f /var/lib/apt/lists/\*debian\*
umount /proc
exit

If storage space is an issue for you, you could also try running the “debfoster” command to further reduce your OS footprint.

**Step #9**

Customise your HoneyStick’s Debian initrd file system to make it USB device aware. If you don\`t do this the device will not be able to boot as USB devices are not part of the standard Debian initrd configuration.

The initrd file is actually a compress RAM filesystem image (cramfs) which can\`t be edited directly, so we\`ll mount it ready only and make a copy before overwriting it with the revised version.

First phase is to set up the cramfs device:

mount -o loop,ro -t cramfs /boot/initrd.img-2.6.8-2-386 /mnt/initrd
cp -a /mnt/initrd/\* /tmp/cramfs
cd /tmp/cramfs
mkdir devfs keyscripts mnt proc sys tmp var

**Step #10**

Now add the necessary USB device drivers into the modules tree of the initrd file. All modules are sourced from your local running Debian system, so make sure that your running kernel and modules match the version that you are installing onto the HoneyStick!

cd lib/modules/2.6.8-2-386/kernel/drivers
mkdir usb
mkdir usb/core
mkdir usb/storage
mkdir usb/host
cp /lib/modules/2.6.8-2-386/kernel/drivers/usb/core/usbcore.ko usb/core
cp /lib/modules/2.6.8-2-386/kernel/drivers/usb/storage/usb-storage.ko usb/storage
cp /lib/modules/2.6.8-2-386/kernel/drivers/usb/host/\*hcd\* usb/host
cp /bin/sleep /tmp/cramfs/bin

**Step #11**

Instruct the kernel to load these additional modules on boot. The sleep command is necessary to ensure that the boot process waits long enough for slow USB devices to be detected and their drivers loaded. You might not need this, but play it safe for now.

Update /tmp/cramfs/loadmodules before the “ide-generic” section:

modprobe -k  usbcore > /dev/null 2>&1
modprobe -k  scsi\_mod > /dev/null 2>&1
modprobe -k  sd\_mod > /dev/null 2>&1
modprobe -k  sr\_mod > /dev/null 2>&1
modprobe -k  usb-storage > /dev/null 2>&1
modprobe -k  uhci-hcd > /dev/null 2>&1
modprobe -k  ohci-hcd > /dev/null 2>&1
/bin/sleep 5

**Step #12**

Update the “/tmp/cramfs/script” to use a USB device as the root filesystem:

ROOT=/dev/sda1

This was probably /dev/hda1 or similar, depending upon your own configuration. If you use SCSI disks, it was probably already to /dev/sda1 correctly (as the 2.6 Debian kernel treats USB devices as SCSI disks).

**Step #13**

Overwrite the old initrd file on the HoneyStick with your new customised cramfs:

umount /mnt/initrd
cd /tmp
mkcramfs cramfs /mnt/usb/boot/initrd.img-2.6.8-2-386

**Step #14**

Configure the Grub boot loader to boot the correct kernel and initrd image:

cp /boot/grub/menu.lst /mnt/usb/boot/grub

Update “/mnt/usb/boot/grub/menu.lst” to only have the following boot options:

title           Debian GNU/Linux, kernel 2.6.8-2-386
root            (hd0,0)
kernel          /boot/vmlinuz-2.6.8-2-386 root=/dev/sda1 ro
initrd          /boot/initrd.img-2.6.8-2-386
savedefault
boot

**Step #15**

Set up initial networking using DHCP. This means that your HoneyStick will attempt to automatically assign itself an IP address on the first local ethernet address on boot up. If you don\`t want this, simply set up networking as per the normal Debian process.

Update “/mnt/usb/etc/network/interfaces”:

\# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
auto eth0
iface eth0 inet dhcp

**Step #16**

Ensure that the correct filesystems are mounted after bootup.

Update “/mnt/usb/etc/fstab”:

\# /etc/fstab: static file system information.
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
proc            /proc           proc    defaults        0       0
/dev/sda1       /               reiserfs    defaults    0       0
usbdevfs        /proc/bus/usb   usbdevfs        defaults        0       0

**Step #17**

Although we have not actually installed it yet, we will set vmware to start automatically in root’s .xsession by updating “/mnt/usb/root/.xession”:

fluxbox & wpmid=$!
vmware &
wait $wmpid

chmod 600 /mnt/usb/root/.xsession

**Step #18**

Secure the HoneyStick by setting up iptables and ensure that it is automatically restarted on bootup by creating “/mnt/usb/etc/init.d/iptables”:

#!/bin/sh

IPTABLES=/sbin/iptables

case "$1" in
start)
        echo -n "Starting iptables"
        #echo "1" > /proc/sys/net/ipv4/ip\_forward
        #echo "1" > /proc/sys/net/ipv4/tcp\_syncookies

        # Clear old rules
        $IPTABLES -X
        $IPTABLES -F
        $IPTABLES -Z

        # INPUT Rules - Add to this section the ports you wish to explicitly allow connections on

        $IPTABLES -A INPUT -i eth0 -m state --state ESTABLISHED,RELATED -j ACCEPT       #Allows connections you start

        #$IPTABLES -A INPUT -i eth0 -p tcp --dport 22 -j ACCEPT  #SSH Connections
        #$IPTABLES -A INPUT -i eth0 -p icmp -j ACCEPT # Ping

        # Drop the rest
        $IPTABLES -A INPUT -i eth0 -j DROP

        echo "done."
        ;;
stop)
        echo -n "Stopping IP Firewall and NAT..."
        $IPTABLES -X
        $IPTABLES -F
        $IPTABLES -Z

        # Input Rules
        $IPTABLES -A INPUT -i eth0 -m state --state ESTABLISHED,related -j ACCEPT
        $IPTABLES -A INPUT -i eth0 -j REJECT
        echo "done."
        ;;

restart)
        echo -n "Restarting iptables"
        $0 stop > /dev/null
        sleep 1
        $0 start > /dev/null
        ;;

\*)
        echo "Usage: $0 {start|stop|restart}"
        ;;
esac

chmod 755 /mnt/usb/etc/init.d/iptables
cd /mnt/usb/etc/rc2.d
ln -s ../init.d/iptables S01iptables

**Step #18**

Reboot and check there is a graphical root login to the HoneyStick.

**Step #19**

If so, download and install VMWare from .tgz file.

**Step #20**

Reboot the HoneyStick and check that VMWare is automatically started on root login.

**Step #21**

Download the current Roo Honeywall ISO image and save it to /root of the HoneyStick:

[https://www.honeynet.org/tools/cdrom](https://www.honeynet.org/tools/cdrom "https://www.honeynet.org/tools/cdrom")

**Step #21**

We need a small honeypot (to save disk space), so download the current Damn Small Linux ISO image which is about 50 Mbytes and offers a number of Unix services by default:

[http://www.damnsmalllinux.org/download.html](http://www.damnsmalllinux.org/download.html "http://www.damnsmalllinux.org/download.html")

**Step #22**

Customise your working environment. I\`d suggest the following steps within the fluxbox X desktop:

- Install VMWare license
- Maximise VMWare application
- Select Autofit VMWare guest in View menu

**Step #23**

You can harden and obfuscate your VMWare workstation installation by installing Kostya’s .c patch from the French Honeynet Project:

[http://www.frenchhoneynet.org](http://www.frenchhoneynet.org/ "http://www.frenchhoneynet.org")

**Step #24**

Set up your Roo GenIII honeywall virtual host.

Create a new Linux virtual host named “honeywall” and set defaults except:

1. Boot from downloaded Roo ISO image in /root (bridged networking)
2. Disable floppy device
3. Add NIC #2 vmnet 2 (custom)
4. Add NIC #3 vmnet 1 (host only)

Power up and check it boots.

**Step #25**

Set up your DSL honeypot virtual host.

Create a new Linux virtual host named “honeypot” and set defaults except:

1. Boot from downloaded DSL ISO image in /root (vmnet2 – custom networking)
2. Disable floppy device

Power up with the kernel options “dsl 2 ssh ldp ftp nfs syslog monkey” and check it boots into a non-X configuration with these services running.

**Step #25**

Configure your HoneyStick’s virtual honeywall and honeypot. See the Honeynet Project’s KYE on building a VMWare Honeynet:

[https://www.honeynet.org/papers](https://www.honeynet.org/papers "https://www.honeynet.org/papers")

### Shrinking your HoneyStick

By default your HoneyStick should have around 450 MBytes of disk space available, which is plenty for a demo honeynet.

For incident response usage, prolonged operation or to create a smaller HoneyStick device, the following steps can be taken:

Clean up after your initial install:

1. Remove /root/vmware-distrib (VMWare installer packages)
2. Remove /root/roo.iso
3. deborphan
4. apt-get clean
5. rm -f /var/lib/apt/lists/\*debian\*

Remove further unnecessary or non-essential Debian packages:

debfoster

Remove the largest installed packages manually using “dpkg -r packagename”:

dpkg-query -W –showformat=’${Installed-Size} ${Package} ${Status}\\n’ | grep -v

deinstall | sort -n | awk ‘{ print $1 ” ” $2 }’

We hope you enjoyed this quick HoneyStick HOWTO and will find the device useful. If you have any questions, please contact David Watson [(mailto:david@honeynet.org.uk)](mailto:david@honeynet.org.uk%29 "mailto:david@honeynet.org.uk)").
