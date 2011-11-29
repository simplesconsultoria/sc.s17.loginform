# -*- coding:utf-8 -*-

from repoze.who.api import get_api

from pyramid.view import view_config

from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPForbidden
from pyramid.security import remember
from pyramid.security import forget

class LoginViews(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(renderer="templates/login.pt",
                 context=HTTPForbidden)
    @view_config(renderer="templates/login.pt", 
                 context='login:resources.Root')
    def login(self):
        request = self.request
        who_api = get_api(request.environ)
        came_from = request.params.get("came_from", request.referer or "/")
        message = ''
        login = ''
        password = ''
        if 'form.submitted' in request.params:
            creds = {}
            creds['login'] = request.params.get('username', '')
            creds['password'] = request.params.get('password', '')
            authenticated, headers = who_api.login(creds)
            if authenticated:
                return HTTPFound(location=came_from,
                                 headers=headers)
            message = 'Failed login'
        else:
            # Remove authentication
            _, headers = who_api.login({})

        if 'REMOTE_USER' in request.environ:
            del request.environ['REMOTE_USER']

        return dict(
            page_title="Login",
            message=message,
            url=request.application_url ,
            came_from=came_from,
            login=login,
            password=password,
            )

    @view_config(name="logout")
    def logout(self):
        headers = forget(self.request)
        url = self.request.resource_url(self.context, 'login')
        return HTTPFound(location=url, headers=headers)

