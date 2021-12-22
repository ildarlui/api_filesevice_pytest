import pytest

from tests.conftest import ADD_TEMPLATE_ID


@pytest.mark.testrail_id(2457539)
def test_get_url_downloads_template(template_api, add_template_docx):
    new_template = add_template_docx
    download_url = template_api.get_url_downloads_template_from_fileservice((new_template['data']))
    ADD_TEMPLATE_ID.add(add_template_docx['data'])
    assert download_url.status_code == 200