## The Honeynet Project Website

This repository houses the source code for https://honeynet.org/.

### Run site locally

1. Clone this repository.
2. Get the latest version of Hugo extended from https://github.com/gohugoio/hugo/releases/. [^hugo-install]  
   **You need the _Hugo extended_ binaries**, which are typically hidden behind _"Show all ... assets"_.
3. Run `hugo server` in the root directory of this repository.
4. Point your browser to <http://localhost:1313>.

[^hugo-install]: See https://gohugo.io/installation/ for more detailed installation instructions.

### Adding content

To add a new blog post, either copy an existing post
or run the following command in the root directory of this repository:

```
hugo new blog/YYYY/MM/DD/some-title/index.md
```

You can then edit the newly created file with your favorite text editor, and add images/resources next to it.

### Adding an author profile

To add an author profile, either copy an existing profile
or run the following command in the root directory of this repository:

```
hugo new authors/john-doe/_index.md
```

You can then edit the newly created file with your favorite text editor, and add images/resources next to it.

### Adding a GitHub project

To add an GitHub project, either copy an existing project
or run the following command in the root directory of this repository:

```
hugo new projects/foo.md
```

You can then edit the newly created file with your favorite text editor.
