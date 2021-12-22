import json

import pytest


from framework.generators.fileservice_constants import FileServiceExpirationDate
from tests.conftest import ADD_FILE_ID


@pytest.mark.testrail_id(2457530)
def test_update_expiration_date_file(add_file_png, file_api, file_payload_generator):
    """"Проверяем что у файла поменялась expirationDate"""
    payload = file_payload_generator.get_expersion_date()
    expiration_date = FileServiceExpirationDate.EXPIRATION_DATE.value
    file_api.update_expiration_date_file_fileservice(add_file_png['data'], json.dumps(payload))
    file_info = file_api.get_file_fileservice(add_file_png['data']).json()
    ADD_FILE_ID.add(add_file_png['data'])
    assert expiration_date in file_info['data']['expirationDate']
