import pytest

from framework.client_api.document_api import APIDocument
from framework.client_api.file_api import APIFile
from framework.client_api.template_api import APITemplate
from framework.generators.document_data_object import FileServiceDocumentDTO
from framework.generators.data_generator import DocumentDataGenerator, FileDateGenerator, \
    TemplateDataGenerator
from framework.generators.file_generator import FileGenerator




@pytest.fixture(scope="module", name="file_generator")
def file_generator_fixture():
    return FileGenerator()


@pytest.fixture(scope="module", name="document_payload_generator")
def document_payload_generator_fixture():
    return DocumentDataGenerator()


@pytest.fixture(scope="module", name="document_api")
def document_api_fixture():
    return APIDocument()


@pytest.fixture(scope="module", name="file_api")
def file_api_fixture():
    return APIFile()


@pytest.fixture(scope="module", name="file_payload_generator")
def file_payload_generator_fixture():
    return FileDateGenerator()


@pytest.fixture(scope="module", name="template_api")
def template_api_fixture():
    return APITemplate()


@pytest.fixture(scope="module", name="template_payload_generator")
def template_payload_generator_fixture():
    return TemplateDataGenerator()


@pytest.fixture(scope="module", name="add_document_docx")
def add_document_docx(file_generator, document_payload_generator, document_api):
    files = file_generator.get_file_document_docx()
    payload = document_payload_generator.generator_payload_document_for_fileservice()
    document_docx = document_api.add_document_fileservice(payload, files)
    return document_docx


@pytest.fixture(scope="module", name="add_document_with_signature")
def add_document_with_signature(file_generator, document_payload_generator, document_api):
    files = file_generator.get_file_document_docx_with_signature_sig()
    payload = document_payload_generator.generator_payload_document_for_fileservice()
    document_with_signature = document_api.add_document_fileservice(payload, files)
    return document_with_signature


@pytest.fixture(scope="module", name="add_signature")
def add_signature(file_generator, document_payload_generator, document_api):
    files = file_generator.get_file_signature_sig()
    payload = document_payload_generator.generator_payload_document_for_fileservice()
    signature = document_api.add_document_fileservice(payload, files)
    return signature


@pytest.fixture(scope="module", name="add_file_png")
def add_file(file_generator, file_api):
    file = file_generator.get_file_image_png()
    new_file = file_api.add_file_fileservice(file)
    return new_file


@pytest.fixture(scope="module", name="add_template_docx")
def add_template(file_generator, template_payload_generator, template_api):
    file = file_generator.get_file_template_docx()
    payload = template_payload_generator.generator_payload_template_for_fileservice()
    template_docx = template_api.add_template_for_fileservice(payload, file)
    return template_docx

