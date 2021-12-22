import json

import pytest

from tests.conftest import ADD_DOCUMENT_ID


@pytest.mark.testrail_id(2457476)
def test_add_attributes_for_document(document_payload_generator, document_api, add_document_docx):
    """"Проверяем что появляются атрибуты """
    payload = document_payload_generator.get_attributes()
    document_api.add_document_attributes_fileservice(add_document_docx['data'], json.dumps(payload))
    document_with_attributes = document_api.get_document_fileservice(add_document_docx['data'])

    ADD_DOCUMENT_ID.add(add_document_docx['data'])

    assert document_with_attributes['data']['attributes'] == payload['attributes']