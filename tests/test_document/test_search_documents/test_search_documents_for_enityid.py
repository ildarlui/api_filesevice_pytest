import json

import pytest


from framework.generators.fileservice_constants import FileServiceEntityId
from tests.conftest import ADD_DOCUMENT_ID


@pytest.mark.testrail_id(2457506)
def test_search_documents_for_enityid(document_api, add_document_docx):

    info_document = document_api.get_document_fileservice(add_document_docx['data'])
    params = {'entityId': FileServiceEntityId.TEST_ID_ONE.value, 'limit': 10, 'offset': 0}
    print(params)
    search_document_list = document_api.search_document_list_fileservice(params)

    ADD_DOCUMENT_ID.add(add_document_docx['data'])

    assert info_document['data'] in search_document_list['data']