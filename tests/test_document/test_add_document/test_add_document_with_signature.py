import pytest

from tests.conftest import ADD_DOCUMENT_ID


@pytest.mark.testrail_id(2456539)
def test_add_document_with_signature(add_document_with_signature, document_api):
    """Загрузить документ c подписью"""
    new_document = add_document_with_signature
    document_info = document_api.get_document_fileservice(new_document['data'])

    ADD_DOCUMENT_ID.add(add_document_with_signature['data'])

    assert new_document['data'] == document_info['data']['id']
    assert document_info['data']['signatureIds'] is not None


