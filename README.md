# free-geek

Source code and documentation for the ["Code for Good" Conference](http://codeforgood.io/) (hackathon) for [Free Geek](http://www.freegeek.org/).

## Getting Started

Check out [the docs](/docs) where we keep a copy of the [feature requests](/docs/Code%20For%20Good%20project.odt) from Free Geek staff.

Also, we abide by the Free Geek volunteer Code of Conduct to make sure you review it [here](/docs/Free_Geek_General_Conduct_guidelines.pdf)


## Installation

```shell
$ pip install geeksched
```

## Contributing

```shell
$ git clone https://github.com/codeforgoodconf/freegeek.git
$ mkvirtualenv freegeek
$ pip install -e freegeek/
```

## Documentation

The project documentation is auto-rendered from the [github repository](https://github.com/codeforgoodconf/free-geek) to [read the docs](https://readthedocs.org/projects/free-geek/).

### Generating documentation
After changes are made in markdown files run these from the level of free-geek folder:

```bash
$ python freegeek/convert_docs.py
$ python freegeek/link_fix.py
$ python manage.py docs
```
These commands:

1. Convert .md to .rst files 
2. Fix links in README.rst
3. Build sphinx docs (read the docs)

Pandoc is required to convert the files. [Installation](http://pandoc.org/installing.html) is OS dependent.

## Adding pre-commit hook for running flake8

1. Open the hidden `.git` folder inside free-geek folder
2. Open the `hook` folder.
3. You are now in `free-geek/.git/hooks/`.
4. Create a file `pre-commit`. No extensions.
5. Write this into the file:
```bash
#!/bin/sh

flake8 .

exit 0
```
5. Make the file executable: `chmod +x pre-commit`

Now before every commit it is going to fun flake8 and display the output while run in terminal.

