=========
Licensing
=========

Licensing provides some utilities needed in order to save and
show licensable content. As default it provides descriptions and localizations
of Creative Commons licenses, but any license could be added.

The characters in the ``symbols`` fields of the provided Creative Commons
licenses are intended to be displayed with this Creative Commons icons font:
http://pfefferle.github.io/openwebicons/#cc-icons

Quick start
-----------

1. Install it using pip

    $ pip install django-licensing

2. Add "licensing" to your ``INSTALLED_APPS`` setting like this::

      INSTALLED_APPS = (
          ...
          'licensing',
      )

3. Create a model that subclass ``Licensed`` (an abstract base class)

.. code-block:: python

    from licensing.models import Licensed

    class Whatever(Licensed):
        pass

The model ``Whatever`` will contain a ``ForeignKey`` field named ``license``.

4. Run ``python manage.py migrate`` to create the licensing models.

5. Show the symbols associated with the license using the openweb font:
at the beginning of the project CSS file you have to add the font

.. code-block:: css

    /* http://pfefferle.github.io/openwebicons/usage/ */
    @import url("http://weloveiconfonts.com/api/?family=openwebicons");

    /* openwebicons */
    i.openwebicons {
      font-family: 'OpenWeb Icons', sans-serif;
      font-style: normal;
    }

and in order of use them you can do something like this

.. code-block::html

    <i class="openwebicons">{{ whatever.license.symbols }}</i>

Tests
-----

If you want to modify this app, there are available several tests that you can launch to check
that nothing is broken::

    $ python runtests.py