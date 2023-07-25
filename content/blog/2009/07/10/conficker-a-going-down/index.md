---
title: "Conficker.A going down?"
date: "2009-07-10"
tags: 
  - "conficker-d40"
---

[Conficker](/papers/conficker) contains a piece of code that has been object of speculation: It does not infect boxes located in the Ukraine. Before sending an exploit, it performs a lookup against Maxmind's GeoIP database, which is freely available, and skips the host if the returned country code is UA. While the B variant comes with a copy of the database embedded, the A variant downloads the file from Maxmind's server. A couple of days ago Felix had the idea to deliver a specially crafted database that maps every IP address to the Ukrain. The database format is actually quite simple, and he managed to create a valid database that places the whole Internet around Kiev.

Maxmind had already changed the link for their database file, probably to mitigate load problems caused by Conficker. The file wasn't accessible from its old URL anyway, so we asked them if they could redirect HTTP requests for the original path to our server where we placed the special database. They did it, and now Conficker.A is being provided with our little gift.

We were very excited to see if this trick would be noticeable in the number of infections. According to the [statistics](http://www.confickerworkinggroup.org/wiki/pmwiki.php/ANY/InfectionTracking#toc4) provided by the Conficker Working Group, the numbers haven't changed yet. This makes sense, the database trick does not necessarily have an impact on the absolute number of infections. However, it should prevent new infections. So we took a look at the number of download attempts for our database file - and saw a clear decrease, depicted in the chart below.

![](images/drupal_image_462.png)

We measured the number of unique IP addresses per hour and came to the graph above. There were almost 15000 hosts attempting to download the file right after we put it online. Current numbers are less than 1000. We are not really sure if this means that Conficker.A cannot infect systems on the Internet anymore at this point in time, but we certainly think that the decreasing download numbers are a good sign - one way or the other.

Tillmann
