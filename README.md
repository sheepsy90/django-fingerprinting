[![pypi](https://img.shields.io/pypi/v/django-spirit.svg?style=flat-square)](https://pypi.python.org/pypi/django-fingerprinting)

django_fingerprinting
=====================

Project goal
------------

Provide a first working approach to the fingerprinting of static resources. 

Reason for the project
----------------------

1. Django doesn't have a framework for this


Installation
------------

1. Install using pip:

		pip install django-fingerprinting

2. Add django_fingerprinting to your INSTALLED_APPS list.

		INSTALLED_APPS = ['django_fingerprinting',] + INSTALLED_APPS

Configuration
-------------


Fingerprinting
==============

To add a replacement of static resources simply set `FINGERPRINTING` as a dictionary 
in your settings file.

	FINGERPRINTING = {
	    'css/global.css': 'css/global-234f-2321db-74fce-34de.css'
	}

This settings option can of course be auto generated at some point.

In order to fingerprint something in your template simply include:
    
    {% load fingerprinting %}
    <head>
        <script src="{% static "js/myjavascrip.js"|fingerprinting %}"></script>
    </head>

    

