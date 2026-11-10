from unittest.mock import patch

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


class ViewErrorHandlingTests(JuntagricoWebdavTestCase):
    """Test that the list view handles WebDAV server errors gracefully."""

    @patch('juntagrico_webdav.views.requests.Session')
    def test_propfind_non_xml_response(self, mock_session_class):
        """If the server returns non-XML content, show an error message on the page."""
        mock_session = mock_session_class.return_value
        mock_response = mock_session.request.return_value
        mock_response.status_code = 200
        mock_response.content = b'Not XML content at all'
        response = self.assertGet(reverse("webdav:list", args=[self.user_server.id]), 200)
        assert 'ungültige Antwort'.encode() in response.content

    @patch('juntagrico_webdav.views.requests.Session')
    def test_propfind_error_status(self, mock_session_class):
        """If the server returns a non-2xx status, show an error message on the page."""
        mock_session = mock_session_class.return_value
        mock_response = mock_session.request.return_value
        mock_response.status_code = 500
        mock_response.content = b'<html><body>Internal Server Error</body></html>'
        response = self.assertGet(reverse("webdav:list", args=[self.user_server.id]), 200)
        assert b'500' in response.content

    @patch('juntagrico_webdav.views.requests.Session')
    def test_propfind_401_status(self, mock_session_class):
        """If the server returns 401 (Unauthorized), show an error message on the page."""
        mock_session = mock_session_class.return_value
        mock_response = mock_session.request.return_value
        mock_response.status_code = 401
        mock_response.content = b'Unauthorized'
        response = self.assertGet(reverse("webdav:list", args=[self.user_server.id]), 200)
        assert b'401' in response.content
