from pytray.utils import get_ip_address


def test_get_valid_ip_address():
  ip = get_ip_address()
  assert isinstance(ip, str)
  assert len(ip.split('.')) == 4


def test_get_local_ip_address():
  ip = get_ip_address()
  assert ip.startswith('192.168.') or ip.startswith('10.')