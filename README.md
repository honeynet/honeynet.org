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

### Migrating content

- To keep old URLs working, we can specify `url: ...` in the page's front matter: https://gohugo.io/content-management/urls/#url
- If you want to add particular styling/structure to static pages, we're using Bootstrap 5.3: https://getbootstrap.com/

### Adding content

To add a new blog post, run the following command in the root directory of this repository:

```
hugo new blog/YYYY/MM/DD/some-title/index.md
```

You can then edit the newly created file with your favorite text editor, and
add images/resources next to it.
