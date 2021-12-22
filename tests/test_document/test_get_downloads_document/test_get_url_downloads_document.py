import pytest

from tests.conftest import ADD_DOCUMENT_ID


@pytest.mark.testrail_id(2457474)
def test_get_url_downloads_document(add_document_docx, document_api):
    """"Проверяем что возвращается адрес для скачивания документа"""
    url_downloads = document_api.get_url_downloads_document_fileservice(add_document_docx['data'])
    downloads_document = document_api.downloads_nginx(url_downloads['data'])

    ADD_DOCUMENT_ID.add(add_document_docx['data'])

    assert downloads_document.status_code == 200

