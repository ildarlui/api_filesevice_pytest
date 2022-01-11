import os


class FileGenerator:

    def get_file_document_docx(self):
        current_path = os.path.dirname(__file__)
        path = os.path.join(current_path, "../../", "document.docx")
        file = [('document', ('document.docx', open(path, 'rb'),
                              'application/vnd.openxmlformats-officedocument.wordprocessingml.document'))]
        return file

    def get_file_image_png(self):
        current_path = os.path.dirname(__file__)
        path = os.path.join(current_path, "../../", "image.png")
        file = [('template', ('image.png', open(path, 'rb'),
                              'application/vnd.openxmlformats-officedocument.wordprocessingml.image'))]
        return file

    def get_file_signature_sig(self):
        current_path = os.path.dirname(__file__)
        path = os.path.join(current_path, "../../", "signature.sig")
        file = [('signature', ('signature.sig', open(path, 'rb'),
                               'application/vnd.openxmlformats-officedocument.wordprocessingml.signature'))]
        return file

    def get_file_document_docx_with_signature_sig(self):
        current_path = os.path.dirname(__file__)
        path_doc = os.path.join(current_path, "../../", "document.docx")
        document = [('document', ('document.docx', open(path_doc, 'rb'),
                                  'application/vnd.openxmlformats-officedocument.wordprocessingml.document'))]
        path_sig = os.path.join(current_path, "../../", "signature.sig")
        signature = [('signature', ('signature.sig', open(path_sig, 'rb'),
                                    'application/vnd.openxmlformats-officedocument.wordprocessingml.signature'))]
        files = document + signature
        return files

    def get_file_template_docx(self):
        current_path = os.path.dirname(__file__)
        path = os.path.join(current_path, "../../", "template.docx")
        file = [('template', ('template.docx', open(path, 'rb'),
                              'application/vnd.openxmlformats-officedocument.wordprocessingml.image'))]
        return file
