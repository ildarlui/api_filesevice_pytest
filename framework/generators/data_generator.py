import random

from framework.generators.document_data_object import FileServiceDocumentDTO, FileServiceTemplateDTO
from framework.generators.fileservice_constants import FileServiceBucket, FileServiceEntityType, \
    FileServiceEntityArea, FileServiceEntityId, FileServiceExpirationDate


class DocumentDataGenerator:

    def generator_payload_document_for_fileservice(self):
        payload = self.get_random_fileservice_document().__dict__
        return payload

    def random_bucket(self):
        return random.choice([FileServiceBucket.PUBLIC.value,
                              FileServiceBucket.COMMON.value, FileServiceBucket.TEMP.value])

    def get_random_fileservice_document(self):
        file_service_document = FileServiceDocumentDTO
        file_service_document.bucket = FileServiceBucket.PUBLIC.value
        file_service_document.entityType = FileServiceEntityType.INTERNET_ACQUIRING.value
        file_service_document.entityArea = FileServiceEntityArea.SHOWCASE.value
        file_service_document.entityId = FileServiceEntityId.TEST_ID_ONE.value
        file_service_document.documentId = ''
        file_service_document.hasAttachedSign = ''
        file_service_document.signatureId = ''
        return file_service_document

    def get_attributes(self):
        attributes = {"attributes": {
            "additionalProp1": ["string1"],
            "additionalProp2": ["string2"]}}
        return attributes


class TemplateDataGenerator:

    def generator_payload_template_for_fileservice(self):
        payload = self.get_random_fileservice_template().__dict__
        return payload

    def get_random_fileservice_template(self):
        file_service_template = FileServiceTemplateDTO
        file_service_template.bucket = FileServiceBucket.TEMP.value
        file_service_template.entityType = FileServiceEntityType.BANK_GUARANTEE.value
        file_service_template.entityArea = FileServiceEntityArea.SHOWCASE.value
        return file_service_template


class FileDateGenerator:

    def get_expersion_date(self):
        expiration_date = {'expirationDate': FileServiceExpirationDate.EXPIRATION_DATE.value}
        return expiration_date
