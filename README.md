## The Honeynet Project Website

This repository houses the next version of https://honeynet.org/. 
The main objective is to migrate from Wordpress to a static site generator (Hugo) and to make the site more maintainable.

### Run site locally

1. Clone this repository.
2. Get the latest version of Hugo extended from https://github.com/gohugoio/hugo/releases/. [^hugo-install]  
   **You need the _Hugo extended_ binaries**, which are typically hidden behind _"Show all ... assets"_.
3. Run `hugo server` in the root directory of this repository.
4. Point your browser to <http://localhost:1313>. 

[^hugo-install]: See https://gohugo.io/installation/ for more detailed installation instructions.

### Contributing

Contributions are super welcome! A lot of stuff can be done by pretty much anyone, it just needs to get done!

#### TODO (necessary for replacing the existing website)

 - [x] Setup Hugo scaffolding. (@mhils)
 - [x] Write a new template from scratch to get rid of the existing cruft. (@mhils)
 - [x] Setup CI to automatically build the site to https://honeynet.github.io/. (@mhils)
 - [ ] Add docs for how to add a blog post. [#4](https://github.com/honeynet/honeynet.github.io/issues/4)
 - [ ] Migrate existing content
   - [ ] Front page (remove hot topics + active projects for now?)
   - [ ] About Us
     - [ ] About Us
     - [ ] CoC
     - [ ] Funding (needs minor updates)
     - [ ] Papers
   - [ ] News (what can we do with auto-migration here?)
   - [ ] GSoC
   - [ ] Projects
   - [ ] FAQ
   - [ ] Workshops (need to add Taiwan 2018 and https://austria2019.honeynet.org/)
   - [ ] Challenges (partially broken on the current website, update with a pointer to https://github.com/honeynet/forensic_challenges)
 - [ ] Fix social icons in the footer. Simply embedding SVGs from https://icons.getbootstrap.com/ is the way to go.

#### TODO (stretch goals)

 - Replicate the fancy front page animation with CSS.
 - Can we do something smart about "active projects"? Scrape activity stats from GitHub maybe?
 - Write new blog entries.