import requests

BASE_API_URL = ''


class APITemplate:

    def add_template_for_fileservice(self, payload, file):
        url = f'{BASE_API_URL}/api/templates'
        response = requests.request("POST", url, data=payload, files=file)
        return response.json()


    def get_template_from_fileservice(self, templateId):
        url = f'{BASE_API_URL}/api/templates/{templateId}'
        response = requests.request("GET", url)
        return response.json()

    def delete_template_fileservice(self, templateId):
        url = f'{BASE_API_URL}/api/templates/{templateId}'
        response = requests.request("DELETE", url)
        return response.json()

    def get_templates_list_fileservice(self, params):
        url = f'{BASE_API_URL}/api/templates'
        response = requests.request("GET", url, params=params)
        return response.json()

    def get_downloads_template_from_fileservice(self, templateId):
        url = f'{BASE_API_URL}/api/templates/{templateId}/downloads'
        response = requests.request("GET", url)
        return response

    def get_url_downloads_template_from_fileservice(self, templateId):
        url = f'{BASE_API_URL}/api/templates/{templateId}/urls'
        response = requests.request("GET", url)
        return response

    def downloads_nginx(self, data):
        url = f"http://172.21.28.6:9000{data}"
        response = requests.request("GET", url)
        return response
