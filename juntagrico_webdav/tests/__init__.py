from django.contrib.auth.models import Permission

from juntagrico.tests import JuntagricoTestCase

from juntagrico_webdav.models import WebdavServer


class JuntagricoWebdavTestCase(JuntagricoTestCase):

    @classmethod
    def setUpTestData(cls):
        # load from fixtures
        cls.load_members()
        cls.default_member = cls.member2
        cls.set_up_server()

    @classmethod
    def set_up_server(cls):
        cls.user_server = WebdavServer.objects.create(
            name="server1",
            url="http://localhost:8080/",
            path="webdav",
            username="user",
            password="password",
            menu_title="server1",
            sortby=WebdavServer.SortOrder.BY_NAME_ASC,
            type=WebdavServer.USER_SERVER,
        )
        cls.admin_server = WebdavServer.objects.create(
            name="server2",
            url="http://localhost:8080/",
            path="webdav",
            username="user",
            password="password",
            menu_title="server2",
            sortby=WebdavServer.SortOrder.BY_NAME_ASC,
            type=WebdavServer.ADMIN_SERVER,
        )
