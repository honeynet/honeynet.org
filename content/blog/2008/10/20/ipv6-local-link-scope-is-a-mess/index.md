---
title: "ipv6 local-link scope is a mess"
authors: ["Markus Koetter"]
date: "2008-10-20"
tags: 
  - "ipv6-d51"
  - "link-local"
---
{{<figure src="images/banner.png" alt="Banner" width="50%">}}

I've been looking on [ipv6](http://en.wikipedia.org/wiki/IPv6) lately, and even though I got a global /64 for free from he.net, I'm not that amused about ipv6 yet.

  

  
- **ipv6 link-local scope** : if you have multiple interfaces with ipv6 link-local addresses, the operating system does not know which interface to use, so you have to append the interface to the hostname/ip when connecting hosts in link-local scope. If you do not use getaddrinfo, this information has to be passed to the bind/connect using  
    `struct sockaddr_in6.sin6_scope_id = if_nametoindex(devicename);`  
    This sounds weird, and it actually is:  
    `nc6 -6 -vv fe80::21f:d0ff:fe23:9b77%eth1 80`  
    may work for some people, but encoding the interface in url renders the whole url-idea useless  
    `http://[fe80::21f:d0ff:fe23:9b77%eth1]`
  
- **getaddrinfo()** is meant to resolve a domain for a service to its A&AAAA records, report the required family etc.   
    
      
    - **problem**: some cheap home routers drop AAAA requests, so the getaddrinfo() call -as well as the application/user- has to wait for a timeout
      
    
      
    **solutions**  
    
      
    - check for AF\_INET6 support, if ipv6 is supported, resolve AAAA   
        
          
        - **problem:** loading a module does not mean you really use ipv6, your nics always get the ipv6 link-local addresses assigned
          
        
          
        
      
    - if hint AI\_ADDRCONFIG is provided, check if we have a ipv6 address with site or global scope, if there is none, report only A/ipv4   
        
          
        - **problem**: all programm using getaddrinfo() do no work for local-link scope any longer, including simple things like netcat6
          
        
          
        
      
    
      
    
  

  

Ubuntu, has chosen to [disable getaddrinfo() for ipv6 if only link-local scope addresses are availible](https://bugs.launchpad.net/ubuntu/+source/netcfg/+bug/24828), breaking ipv6 support for all major applications, but improving the user experience for people with b0rked routers. **netcat6** on Ubuntu hardy:  
`nc6 -6 -vv -l -p 4711  
nc6: forward host lookup failed for local endpoint [unspecified] (4711): Name or service not known  
`  
Debian [had the same patch applied](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=435646), but removed it due to regression. Summing up the problems with ipv6 link-local scope, it is a mess. I'll have to provide site/global ipv6 for my network to circumvent these problems, rendering link-local completely useless.
