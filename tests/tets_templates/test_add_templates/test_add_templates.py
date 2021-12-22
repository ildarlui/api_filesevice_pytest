import pytest

from tests.conftest import ADD_TEMPLATE_ID


@pytest.mark.testrail_id(2457541)
def test_add_document(add_template_docx, template_api):
    """"Загрузить шаблон"""
    new_template = add_template_docx
    template_info = template_api.get_template_from_fileservice(new_template['data'])

    ADD_TEMPLATE_ID.add(add_template_docx['data'])

    assert new_template['data'] == template_info['data']['id']