# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    response.flash = T("The Taste of India")
    message = T('Welcome to Shri Nimad Spices')
    MAX_IMAGES=10
    q=(db.carousel.is_enabled==True)
    images = db(q).select(orderby=~db.carousel.created_on,limitby=(0,MAX_IMAGES))
    MAX_IMAGES=db(q).count()
    return dict(message=message,enum_images=enumerate(images),MAX_IMAGES=MAX_IMAGES)


def about():
    return locals()


def products():
    return locals()


def contact():
    return locals()


def ground_spices():
    images = db(db.ground).select(orderby=~db.ground.created_on)
    return locals()


def blend_spices():
    images = db(db.blend).select(orderby=~db.blend.created_on)
    return locals()

def recepies():
    images = db(db.recipe).select(orderby=~db.recipe.created_on)
    return locals()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
