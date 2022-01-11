import pytest


pytest_plugins = (
    "pytest_plugins.fileservice_plugins.plugin"
)

ADD_DOCUMENT_ID = set()
ADD_FILE_ID = set()
ADD_TEMPLATE_ID = set()


@pytest.fixture(autouse=True)
def delete_all_created_documents(document_api, file_api, template_api, request):

    def delete_document_fileservice():
        if ADD_DOCUMENT_ID is not None:
            for i in ADD_DOCUMENT_ID:
                document_api.delete_document_fileservice(i)

    ADD_DOCUMENT_ID.clear()
    request.addfinalizer(delete_document_fileservice)

    def delete_file_fileservice():
        if ADD_FILE_ID is not None:
            for i in ADD_FILE_ID:
                file_api.delete_file_fileservice(i)

    ADD_FILE_ID.clear()
    request.addfinalizer(delete_file_fileservice)

    def delete_template_fileservice():
        if ADD_TEMPLATE_ID is not None:
            for i in ADD_TEMPLATE_ID:
                template_api.delete_template_fileservice(i)

    ADD_TEMPLATE_ID.clear()
    request.addfinalizer(delete_template_fileservice)
