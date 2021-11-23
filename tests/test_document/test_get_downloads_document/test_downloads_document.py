import pytest

from tests.conftest import ADD_DOCUMENT_ID


@pytest.mark.testrail_id(2457474)
def test_downloads_document(add_document_docx, document_api):
    """"Проверяем что документ скачивается """
    downloads_document = document_api.get_downloads_document_fileservice(add_document_docx['data'])

    ADD_DOCUMENT_ID.add(add_document_docx['data'])

    assert downloads_document.status_code == 200