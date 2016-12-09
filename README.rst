==========
``gistey``
==========

Installation:
-------------

- Using pip

  ``pip install gistey``

  On linux systems you might require to use `sudo` 

Usage:
------

1. To create a public gist with description for a bunch of files

   .. code:: bash

     $ gistey --description "This would be the description" --files somefile.ext someotherfile
     URL of the gist created:  https://gist.github.com/<id> # output


2. To create a secret gist, just add ``--secret`` option

   .. code:: bash

     $ gistey --description "This would be the description" --files somefile.ext someotherfile --secret
     URL of the gist created:  https://gist.github.com/<id> # output


3. To create a gist without description

   .. code:: bash

     $ gistey --files somefile.ext someotherfile
     URL of the gist created:  https://gist.github.com/<id> # output
