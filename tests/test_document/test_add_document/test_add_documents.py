import pytest

from tests.conftest import ADD_DOCUMENT_ID


@pytest.mark.testrail_id(2456538)
def test_add_document(add_document_docx, document_api):
    """"Загрузить документ без подписи"""
    new_document = add_document_docx
    document_info = document_api.get_document_fileservice(new_document['data'])

    ADD_DOCUMENT_ID.add(add_document_docx['data'])

    assert new_document['data'] == document_info['data']['id']










