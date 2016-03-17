=========
Licensing
=========

Licensing provides some utilities needed in order to save and
show licensable content. As default it provides descriptions and localizations
of Creative Commons licenses, but any license could be added.

The characters in the ``symbols`` fields of the provided Creative Commons
licenses are intended to be displayed with this Creative Commons icons font:
http://pfefferle.github.io/openwebicons/#cc-icons

Supported Django versions
-------------------------
Licensing is tested against Django versions 1.8 and 1.9.

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

5. Where is needed to show the symbol associated with the license you can use the tag ``show_license``:
it uses the openweb font to render it; it's simple as

.. code-block:: html

    {% load licensing_tags %}

    {% block head %}

    {% licensing_style %}

    {% endblock %}
    {% block foobar %}
        {% show_license license %}
    {% endblock %}

where ``license`` is an instance of the ``License`` model.

The ``licensing_style`` tag simply renders a ``<style>`` block with all the necessary
to use the correct font, like the code below:

.. code-block:: css

    /* http://pfefferle.github.io/openwebicons/usage/ */
    @import url("http://weloveiconfonts.com/api/?family=openwebicons");

    /* openwebicons */
    i.openwebicons {
      font-family: 'OpenWeb Icons', sans-serif;
      font-style: normal;
    }

It's possible to customize the css class and template used in these tags, read the source
code for more details.

Tests
-----

If you want to modify this app, there are available several tests that you can launch to check
that nothing is broken::

    $ python runtests.py

It's also available a ``tox`` configuration file to test it on multiple Django versions.
