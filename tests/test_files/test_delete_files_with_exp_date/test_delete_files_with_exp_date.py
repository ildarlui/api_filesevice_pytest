import json

import pytest


@pytest.mark.testrail_id(2457527)
def test_delete_files_with_exp_date(add_file_png, file_api, file_payload_generator):
    """"Проверяем что у файла поменялась expirationDate"""
    payload = file_payload_generator.get_expersion_date()
    file_api.update_expiration_date_file_fileservice(add_file_png['data'], json.dumps(payload))
    file_api.delete_expired_files_from_fileservice()
    file_info = file_api.get_file_fileservice(add_file_png['data'])
    assert file_info.status_code == 404
