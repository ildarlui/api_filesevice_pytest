

class FileServiceDocumentDTO:
    def __init__(self, bucket=None, entity_type=None, entity_area=None, entity_id=None,
                 document_id=None, has_attached_sign=None, signature_id=None):
        self.bucket = bucket
        self.entityType = entity_type
        self.entityArea = entity_area
        self.entityId = entity_id
        self.documentId = document_id
        self.hasAttachedSign = has_attached_sign
        self.signatureId = signature_id


class FileServiceTemplateDTO:
    def __init__(self, bucket=None, entity_type=None, entity_area=None):
        self.bucket = bucket
        self.entityType = entity_type
        self.entityArea = entity_area
