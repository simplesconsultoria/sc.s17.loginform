import unittest

from pyramid import testing

class LoginViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def _makeOne(self, request):
        from sc.s17.loginform.views import LoginViews
        context = testing.DummyResource()
        inst = LoginViews(context, request)
        return inst

    def tearDown(self):
        testing.tearDown()

    def test_login(self):
        request = testing.DummyRequest()
        inst = self._makeOne(request)
        result = inst.login()
        self.assertEqual(result['page_title'], 'login')


class LoginViewFunctionalTests(unittest.TestCase):
    def setUp(self):
        from sc.s17.loginforms import main

        app = main()
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_it(self):
        res = self.testapp.get('/', status=200)
        self.failUnless('Username' in res.body)


