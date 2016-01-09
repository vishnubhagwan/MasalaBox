# -*- coding: utf-8 -*-

from os import path

db.define_table('carousel',
    Field('is_enabled', 'boolean', readable=True, writable=True, default=True, label=T('Is Enabled')),
    Field('name', 'string',length=256, notnull=True, label=T('Name')),
    Field('alt', 'string', length=256, label=T('Alt')),
    Field('description', 'string', length=512, label=T('Description')),
    Field('image_file', 'upload', uploadfolder=path.join(
        request.folder,'static','images','carousel'
        ), autodelete=True, label=T('Image File')),
    Field('created_on','datetime',default=request.now,
            writable=False,readable=True, label=T('Created on')),format='%(name)s')

db.define_table('ground',
    Field('name','string',length=256,notnull=True,label=T('Name')),
    Field('image_file','upload',uploadfolder=path.join(
        request.folder,'static','images','ground'
        ),autodelete=True,label=T('Image File')),
    Field('created_on','datetime',default=request.now,
            writable=False,readable=True,label=T('Created on')),format='%(name)s')

db.define_table('blend',
    Field('name','string',length=256,notnull=True,label=T('Name')),
    Field('image_file','upload',uploadfolder=path.join(
        request.folder,'static','images','blend'
        ),autodelete=True,label=T('Image File')),
    Field('created_on','datetime',default=request.now,
            writable=False,readable=True,label=T('Created on')),format='%(name)s')

db.define_table('recipe',
    Field('name','string',length=256,notnull=True,label=T('Name')),
    Field('image_file','upload',uploadfolder=path.join(
        request.folder,'static','images','recipe'
        ),autodelete=True,label=T('Image File')),
    Field('created_on','datetime',default=request.now,
            writable=False,readable=True,label=T('Created on')),format='%(name)s')
