import json
import pytest

from tests.conftest import ADD_DOCUMENT_ID


@pytest.mark.testrail_id(2457503)
def test_delete_attributes_from_document(document_payload_generator, document_api, add_document_docx):
    """"Проверяем что удаляются атрибуты """
    payload = document_payload_generator.get_attributes()
    document_api.add_document_attributes_fileservice(add_document_docx['data'], json.dumps(payload))
    document_api.delete_document_attributes_fileservice(add_document_docx['data'], json.dumps(payload))
    document_no_attributes = document_api.get_document_fileservice(add_document_docx['data'])

    ADD_DOCUMENT_ID.add(add_document_docx['data'])

    assert 'attributes' not in document_no_attributes['data']
