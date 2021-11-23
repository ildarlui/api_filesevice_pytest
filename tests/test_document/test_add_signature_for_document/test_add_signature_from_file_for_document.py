import pytest
from tests.conftest import ADD_DOCUMENT_ID


@pytest.mark.testrail_id(2457473)
def test_add_signature_from_file_for_document(add_document_docx, file_api, document_api, file_generator):
    file = file_generator.get_file_signature_sig()
    file_id = file_api.add_file_fileservice(file)['data']
    payload = {'signatureFileId': f'{file_id}'}
    document_id = add_document_docx['data']
    add_signature = document_api.add_signature_from_files_for_document_fileservice(payload, document_id)
    signature_id = add_signature.json()['data']
    document_info = document_api.get_document_fileservice(add_document_docx['data'])

    ADD_DOCUMENT_ID.add(add_document_docx['data'])

    assert document_info['data']['id'], document_id
    assert signature_id, document_info['data']['signatureIds']