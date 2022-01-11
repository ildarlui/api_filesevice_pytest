import pytest


from framework.generators.fileservice_constants import FileServiceEntityType
from tests.conftest import ADD_TEMPLATE_ID


@pytest.mark.testrail_id(2457538)
def test_get_templates_list(template_api, add_template_docx):

    info_template = template_api.get_template_from_fileservice(add_template_docx['data'])
    params = {'entityType': FileServiceEntityType.BANK_GUARANTEE.value, 'limit': 10, 'offset': 0}
    search_document_list = template_api.get_templates_list_fileservice(params)

    ADD_TEMPLATE_ID.add(add_template_docx['data'])

    assert info_template['data'] in search_document_list['data']
