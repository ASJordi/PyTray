from pytray.utils import display_usage
from pytest_mock import mocker
import psutil


def test_display_usage(mocker):
  mock_cpu_percent = mocker.patch("psutil.cpu_percent", return_value=42.0)
  mock_virtual_memory = mocker.MagicMock()
  mock_virtual_memory.percent = 84.0
  mocker.patch("psutil.virtual_memory", return_value=mock_virtual_memory)
  assert display_usage() == (42.0, 84.0)


def test_display_usage_calls(mocker):
  mocker.patch("psutil.cpu_percent", return_value=42.0)
  mock_virtual_memory = mocker.MagicMock()
  mock_virtual_memory.percent = 84.0
  mocker.patch("psutil.virtual_memory", return_value=mock_virtual_memory)
  display_usage()
  psutil.cpu_percent.assert_called_with()
  psutil.virtual_memory.assert_called_with()
