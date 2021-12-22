import pytest

from tests.conftest import ADD_FILE_ID


@pytest.mark.testrail_id(2457528)
def test_add_file(add_file_png, file_api):
    new_file = add_file_png
    get_downloads = file_api.get_url_downloads_file_fileservice(new_file['data'])
    ADD_FILE_ID.add(add_file_png['data'])
    assert get_downloads.status_code == 200
