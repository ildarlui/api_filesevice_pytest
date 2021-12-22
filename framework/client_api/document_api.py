import requests

BASE_API_URL = ''


class APIDocument:

    def add_document_fileservice(self, payload, files):
        url = f'{BASE_API_URL}/api/documents'
        response = requests.request("POST", url, data=payload, files=files)
        return response.json()

    def get_document_fileservice(self, document_id):
        url = f'{BASE_API_URL}/api/documents/{document_id}'
        response = requests.get(url)
        return response.json()

    def delete_document_fileservice(self, document_id):
        url = f'{BASE_API_URL}/api/documents/{document_id}'
        response = requests.request("DELETE", url)
        return response.json()

    def add_signature_for_document_fileservice(self, files, document_id):
        url = f'{BASE_API_URL}/api/documents/{document_id}/signatures'
        response = requests.request("POST", url, files=files)
        return response

    def add_signature_from_files_for_document_fileservice(self, payload, document_id):
        url = f'{BASE_API_URL}/api/documents/{document_id}/signatures'
        response = requests.request("POST", url, data=payload)
        return response

    def delete_signature_from_files_for_document_fileservice(self, document_id, signature_id):
        url = f'{BASE_API_URL}/api/documents/{document_id}/signatures/{signature_id}'
        response = requests.request("DELETE", url)
        return response

    def get_signature_info(self, document_id, signature_id):
        url = f'{BASE_API_URL}/api/documents/{document_id}/signatures/{signature_id}'
        response = requests.request("GET", url)
        return response.json()

    def search_document_list_fileservice(self, params):
        url = f'{BASE_API_URL}/api/documents'
        payload = {}
        headers = {'X-Version': '1.0'}
        response = requests.request("GET", url, params=params, headers=headers, data=payload)
        return response.json()

    def add_document_attributes_fileservice(self, document_id, payload):
        url = f'{BASE_API_URL}/api/documents/{document_id}/attributes'
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    def delete_document_attributes_fileservice(self, document_id, payload):
        url = f'{BASE_API_URL}/api/documents/{document_id}/attributes'
        headers = {'Content-Type': 'application/json'}
        response = requests.request("DELETE", url, headers=headers, data=payload)
        return response

    def get_downloads_document_fileservice(self, document_id):
        url = f'{BASE_API_URL}/api/documents/{document_id}/downloads'
        response = requests.request("GET", url)
        return response

    def get_url_downloads_document_fileservice(self, document_id):
        url = f'{BASE_API_URL}/api/documents/{document_id}/urls'
        response = requests.request("GET", url)
        return response.json()

    def downloads_nginx(self, data):
        url = f"http://172.21.28.6:9000{data}"
        response = requests.request("GET", url)
        return response