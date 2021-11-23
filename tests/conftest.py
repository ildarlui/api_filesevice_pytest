import pytest

from framework.client_api.document_api import APIDocument
from framework.client_api.file_api import APIFile
from framework.client_api.template_api import APITemplate
from framework.generators.DTO import FileServiceDocumentDTO
from framework.generators.data_generator import DocumentDataGenerator, Constants_FS
from framework.generators.file_generator import FileGenerator


@pytest.fixture(scope="module", name="file_generator")
def file_generator_fixture():
    return FileGenerator()


@pytest.fixture(scope="module", name="payload_generator")
def payload_generator_fixture():
    return DocumentDataGenerator()


@pytest.fixture(scope="module", name="document_api")
def document_api_fixture():
    return APIDocument()


@pytest.fixture(scope="module", name="file_api")
def file_api_fixture():
    return APIFile()


@pytest.fixture(scope="function", name="template_api")
def template_api_fixture():
    return APITemplate()


@pytest.fixture(scope="function", name="dto_document")
def DTO_document_fixture():
    return FileServiceDocumentDTO()


@pytest.fixture(scope="function", name="constants_api")
def constants_fixture():
    return Constants_FS()

#фикстуры для документов

@pytest.fixture(scope="module", name="add_document_docx")
def add_document_docx(file_generator, payload_generator, document_api):
    files = file_generator.get_file_document_docx()
    payload = payload_generator.generator_payload_document_for_fileservice()
    document_docx = document_api.add_document_fileservice(payload, files)
    return document_docx


@pytest.fixture(scope="module", name="add_signature")
def add_signature(file_generator, payload_generator, document_api):
    files = file_generator.get_file_signature_sig()
    payload = payload_generator.generator_payload_document_for_fileservice()
    signature = document_api.add_document_fileservice(payload, files)
    return signature


@pytest.fixture(scope="module", name="add_document_with_signature")
def add_document_with_signature(file_generator, payload_generator, document_api):
    files = file_generator.get_file_document_docx_with_signature_sig()
    payload = payload_generator.generator_payload_document_for_fileservice()
    document_with_signature = document_api.add_document_fileservice(payload, files)
    return document_with_signature


#фикстуры для удаления документов

ADD_DOCUMENT_ID = set()

@pytest.fixture(autouse=True)
def delete_all_created_entity(document_api, request):

    def delete_document_fileservice():
        if ADD_DOCUMENT_ID is not None:
            for i in ADD_DOCUMENT_ID:
                document_api.delete_document_fileservice(i)

    ADD_DOCUMENT_ID.clear()
    request.addfinalizer(delete_document_fileservice)