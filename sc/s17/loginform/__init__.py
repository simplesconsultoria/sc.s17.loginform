# -*- coding:utf-8 -*-
from pyramid.config import Configurator
from sc.s17.loginform.resources import Root
from pyramid.i18n import TranslationStringFactory

MessageFactory = TranslationStringFactory("sc.s17.loginform")

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.scan("sc.s17.loginform.views")
    config.add_static_view('static', 'sc.s17.loginform:static',
                           cache_max_age=3600)
    return config.make_wsgi_app()
