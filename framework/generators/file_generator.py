

class FileGenerator:

    def get_file_document_docx(self):
        file = [('document', ('document.docx',
            open('C:/Users/ildar/PycharmProjects/github/aq-file-service-tests/framework/generators/document.docx', 'rb'),
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document'))]
        return file

    def get_file_image_png(self):
        file = [('template', ('image.png',
            open('C:/Users/ildar/PycharmProjects/github/aq-file-service-tests/framework/generators/image.png', 'rb'), 'image/png'))]
        return file

    def get_file_signature_sig(self):
        file = [('signature', ('signature.sig',
            open('C:/Users/ildar/PycharmProjects/github/aq-file-service-tests/framework/generators/signature.sig', 'rb'),
            'application/octet-stream'))]
        return file

    def get_file_document_docx_with_signature_sig(self):
        document = [('document', ('document.docx',
            open('C:/Users/ildar/PycharmProjects/github/aq-file-service-tests/framework/generators/document.docx', 'rb'),
                                  'application/vnd.openxmlformats-officedocument.wordprocessingml.document'))]
        signature = [('signature', ('ValidSign_2222995569.sig',
            open('C:/Users/ildar/PycharmProjects/github/aq-file-service-tests/framework/generators/signature.sig', 'rb'),
            'application/octet-stream'))]
        files = document + signature
        return files

    def get_file_template_docx(self):
        file = [('template', ('template.docx',
            open('C:/Users/ildar/PycharmProjects/github/aq-file-service-tests/framework/generators/template.docx', 'rb'),
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document'))]
        return file


    # @staticmethod
    # def generate_file(file_name="", file_ext="png"):
    #     # logging.getLogger(__name__).debug(f"Generate file '{file_name}.{file_ext}'")
    #
    #     image_height = 50
    #     image_width = 50
    #     red = random.randint(1, 255)
    #     green = random.randint(1, 255)
    #     blue = random.randint(1, 255)
    #
    #     file = NamedTemporaryFile(suffix=f"_{file_name}." + file_ext, delete=False)
    #     img = Image.new('RGB', (image_width, image_height), color=(red, green, blue))
    #     img.save(file.name, format=file_ext)
    #     file.flush()
    #
    #     file.close()

        # logging.getLogger(__name__).debug(f"Successful generated file '{file.name}'")
        # return file.name

    # def get_random_png(self):
    #     file_path = FileGenerator.generate_file("Апельсин", "png")
        # file = [('template', ('python-error.png', open(FileGenerator.generate_random_png(), 'rb'), 'image/png'))]
        # with open('file.png', 'w') as f:
        #     f.write(file)
        # return file_path

# with FileGenerator.generate_random_png() as f:
#     f.read()
#     print(f)

# print(type(FileGenerator.generate_random_png()))


