# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Govind Shukla <govindshukla17may@gmail.com>'
response.meta.description = 'Nimad Spices'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('About Us'), False, URL('default', 'about'), []),
    (T('Products'), False, URL('default', 'products'), [
        (T('Ground Spices'), False, URL('default', 'ground_spices'), []),
        (T('Blend Spices'), False, URL('default', 'blend_spices'), []),
        (T('Other Products'), False, URL('default', 'other_prducts'), []),
        (T('Recipies'), False, URL('default', 'recepies'), []),
    ]),
    (T('Contact Us'), False, URL('default', 'contact'), [])
]

if "auth" in locals(): auth.wikimenu()
