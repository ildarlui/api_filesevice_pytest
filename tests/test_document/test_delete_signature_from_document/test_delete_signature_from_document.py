import pytest

from tests.conftest import ADD_DOCUMENT_ID


@pytest.mark.testrail_id(2457464)
def test_delete_signature_from_document(add_document_docx, file_api, document_api, file_generator):
    """"Проверяем что подпись удаляется из документа"""
    file = file_generator.get_file_signature_sig()
    file_id = file_api.add_file_fileservice(file)['data']
    payload = {'signatureFileId': f'{file_id}'}
    document_id = add_document_docx['data']
    signature_id = document_api.add_signature_from_files_for_document_fileservice(payload, document_id).json()['data']
    document_api.delete_signature_from_files_for_document_fileservice(document_id, signature_id)
    document_info = document_api.get_document_fileservice(document_id)

    ADD_DOCUMENT_ID.add(add_document_docx['data'])

    assert 'signatureIds' not in document_info['data']