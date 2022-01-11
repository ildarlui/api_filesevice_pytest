import pytest

from tests.conftest import ADD_DOCUMENT_ID


@pytest.mark.testrail_id(2457463)
def test_add_signature_for_document(add_document_docx, document_api, file_generator):
    """"Проверяем что загруженная подпись прикрепляется к документу"""
    files = file_generator.get_file_signature_sig()
    add_signature = document_api.add_signature_for_document_fileservice(files, add_document_docx['data'])
    signature_id = add_signature.json()['data']
    signature_info = document_api.get_signature_info(add_document_docx['data'], signature_id)

    ADD_DOCUMENT_ID.add(add_document_docx['data'])

    assert signature_info['data']['id'] == signature_id
    assert signature_info['data']['documentId'] == add_document_docx['data']
