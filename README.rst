python-pragmatic
================

Pragmatic tools and utilities for Python projects.

Tested on Python 2.7.


Requirements
------------
Some utilities require additional libraries as:

- Pillow/PIL
- pyBarcode


Installation
------------

Using pip: pip install python-pragmatic


Usage
-----

Classes
'''''''
``get_subclasses(classes, level=0)``
    Return the list of all subclasses for given class (or list of classes).

``get_parent_classes(class)``
    Return the list of all parent classes for given class.

Dates
'''''''
``diff_month(date_from, date_to)``
    Returns number of months between dates 'date_from' and 'date_to'

``diff_days(date_from, date_to)``
    Returns number of days between dates 'date_from' and 'date_to'

``week_range(date)``
    Returns a tuple of '(start_date, end_date)' of week range by given date.

Numbers
'''''''
``round_to_n_decimal_places(value, n)``
    Returns number rounded to n decimal places.

OS
''''
``base64_to_file(content, file_path)``
    Stores base64 encoded content to file.

Strings
'''''''
``generate_hash(length=5)``
    Returns random generated string

``barcode(code, args=None)``
    Returns barcode as string encoded in base64 format.

``remove_accents(input)``
    Returns input string without accent characters.


Thirdparty
''''''''''
``class BarcodeImageWriter(ImageWriter)``
    Fixed version of barcode.writer.ImageWriter.
