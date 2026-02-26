from django.urls import reverse

from . import JuntagricoWebdavTestCase


class ViewTests(JuntagricoWebdavTestCase):
    """
    Run a webdav server before running tests. e.g.:
    pip install pywebdavserver
    pywebdavserver serve --backend local --path juntagrico_webdav/tests --username user --password password
    """

    def testMemberView(self):
        self.assertGet(reverse("webdav:list", args=[self.user_server.id]))
        self.assertGet(reverse("webdav:get-file", args=[self.user_server.id, 'test.txt']))

    def testAdminView(self):
        self.assertGet(reverse("webdav:list", args=[self.admin_server.id]), 302)
        self.assertGet(reverse("webdav:get-file", args=[self.admin_server.id, 'test.txt']), 302)

        self.assertGet(reverse("webdav:list", args=[self.admin_server.id]), member=self.admin)
        self.assertGet(reverse("webdav:get-file", args=[self.admin_server.id, 'test.txt']), member=self.admin)
