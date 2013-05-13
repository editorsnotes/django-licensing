=========
Licensing
=========

Licensing provides an abstract base class for Django models that
contain licensable content. It provides descriptions and localizations
of Creative Commons licenses, but any license could be added.

The characters in the `symbols` fields of the provided Creative Commons
licenses are intended to be displayed with this Creative Commons icons font:
http://pfefferle.github.io/openwebicons/#cc-icons

Quick start
-----------

1. Add "licensing" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'licensing',
      )

2. Run `python manage.py syncdb` to create the licensing models.
