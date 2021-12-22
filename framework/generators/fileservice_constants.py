from enum import Enum


class FileServiceBucket(Enum):
    PUBLIC = 'Public'
    COMMON = 'Common'
    TEMP = 'Temp'


class FileServiceEntityType(Enum):
    INTERNET_ACQUIRING = 'InternetAcquiring'
    BANK_GUARANTEE = 'BankGuarantee'
    MERCHANT_ACQUIRING = 'MerchantAcquiring'


class FileServiceEntityArea(Enum):
    SHOWCASE = 'Showcase'
    SHOWCASE_TEST = 'ShowcaseTest'


class FileServiceEntityId(Enum):
   TEST_ID_ONE = '9103bb2b-226b-9c6e-9649-0cd39a0d6d9a'


class FileServiceExpirationDate(Enum):
   EXPIRATION_DATE = '2021-10-08T07:47:33.09'

