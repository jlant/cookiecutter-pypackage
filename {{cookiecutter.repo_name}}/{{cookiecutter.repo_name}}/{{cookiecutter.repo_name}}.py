# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.repo_name }}.{{ cookiecutter.repo_name }}
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A short description.

    :copyright: {{ cookiecutter.year }} by {{ cookiecutter.full_name }}, see AUTHORS.rst
    :license: The MIT License (MIT), see LICENSE file for more details
"""

def hello(msg="World"):
    """Function that prints a message.

    :param msg: message to say
    :type msg: string
    :returns: string
    :raises: something

    .. note::
       You can note something here.

    .. warning::
       You can warn about something here.

    >>> hello()
    Hello World!
    >>> hello(msg="there")
    Hello there!
    """
    return "Hello {}!".format(msg)
