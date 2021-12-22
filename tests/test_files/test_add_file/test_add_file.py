import pytest
from tests.conftest import ADD_FILE_ID


@pytest.mark.testrail_id(2457517)
def test_add_file(add_file_png, file_api):
    new_file = add_file_png
    info_new_file = file_api.get_file_fileservice(new_file['data']).json()
    ADD_FILE_ID.add(add_file_png['data'])
    assert info_new_file['data']['id'], new_file['data']
