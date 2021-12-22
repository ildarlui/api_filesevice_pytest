import json

import pytest


from tests.conftest import ADD_DOCUMENT_ID


@pytest.mark.testrail_id(2457507)
def test_search_documents_for_attributes_from_fileservice(document_payload_generator,
                                                                      document_api, add_document_docx):
    payload = document_payload_generator.get_attributes()
    document_api.add_document_attributes_fileservice(add_document_docx['data'], json.dumps(payload))
    info_document = document_api.get_document_fileservice(add_document_docx['data'])
    params = {'entityId': '', 'attributes.additionalProp1': 'string1', 'attributes.additionalProp2': 'string2', 'limit': 10, 'offset': 0}
    search_document_list = document_api.search_document_list_fileservice(params)

    ADD_DOCUMENT_ID.add(add_document_docx['data'])

    assert info_document['data'] in search_document_list['data']