free-geek
=========

Source code and documentation for the `"Code for Good"
Conference <http://codeforgood.io/>`__ (hackathon) for `Free
Geek <http://www.freegeek.org/>`__.

Getting Started
---------------

Check out `the docs <https://github.com/neex-io/free-geek/tree/master/docs>`__ where we keep a copy of the `feature
requests <https://github.com/neex-io/free-geek/tree/master/docs/Code%20For%20Good%20project.odt>`__ from Free Geek
staff.

Also, we abide by the Free Geek volunteer Code of Conduct to make sure
you review it `here <https://github.com/neex-io/free-geek/tree/master/docs/Free_Geek_General_Conduct_guidelines.pdf>`__

Installation
------------

.. code:: shell

    $ pip install geeksched

Contributing
------------

.. code:: shell

    $ git clone https://github.com/codeforgoodconf/freegeek.git
    $ mkvirtualenv freegeek
    $ pip install -e freegeek/

Documentation
-------------

The project documentation is auto-rendered from the `github
repository <https://github.com/codeforgoodconf/free-geek>`__ to `read
the docs <https://readthedocs.org/projects/free-geek/>`__.

Generating documentation
~~~~~~~~~~~~~~~~~~~~~~~~

After changes are made in markdown files run these from the level of
free-geek folder:

.. code:: bash

    $ python freegeek/convert_docs.py
    $ python freegeek/link_fix.py
    $ python setup.py docs

These commands:

1. Convert .md to .rst files
2. Fix links in README.rst
3. Build sphinx docs (read the docs)

Pandoc is required to convert the files.
`Installation <http://pandoc.org/installing.html>`__ is OS dependent.

Adding flake8 into a pre-commit hook
------------------------------------

1. Open the hidden ``.git`` folder inside free-geek folder
2. Open the ``hook`` folder.
3. You are now in ``free-geek/.git/hooks/``.
4. Create a file ``pre-commit``. No extensions.
5. Write this into the file:

.. code:: bash

    #!/bin/sh

    flake8 .

    exit 0

5. Make the file executable: ``chmod +x pre-commit``

Commits must be executed in the terminal, not GUI.

Now before every commit flake8 will run and display the output into
terminal window. It will not prevent the commit.
