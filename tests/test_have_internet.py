from pytray.utils import have_internet
from pytest_mock import mocker


def test_have_internet(mocker):
  mocker.patch("http.client.HTTPSConnection")
  assert have_internet() == True


def test_have_internet_no_connection(mocker):
  mock_conn = mocker.MagicMock()
  mock_conn.request.side_effect = Exception
  mocker.patch("http.client.HTTPSConnection", return_value=mock_conn)
  assert have_internet() == False


def test_have_internet_request_called(mocker):
  mock_conn = mocker.MagicMock()
  mocker.patch("http.client.HTTPSConnection", return_value=mock_conn)
  have_internet()
  mock_conn.request.assert_called_with("HEAD", "/")


def test_have_internet_close_connection(mocker):
  mock_conn = mocker.MagicMock()
  mocker.patch("http.client.HTTPSConnection", return_value=mock_conn)
  have_internet()
  mock_conn.close.assert_called()
