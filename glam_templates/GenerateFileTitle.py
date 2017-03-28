__author__ = 'djff'

class GenerateFileTitle:
    def __init__(self, file_id, extension, filename='', description='', glam_name='', collection=''):
        self.file_id = file_id
        # self.collection = collection
        self.extension = extension
        self.filename = filename
        self.description = description
        self.glam_name = glam_name

        self.file_title = None
        self.__set_filename()

    def test_title(self):
        pass

    def __set_filename(self):
        """
        sets name of a single image
        :return:
        """
        title = ''
        seperator = '_'

        # title += seperator + self.collection

        if self.filename:
            title += seperator + self.filename

        elif self.description:
            title += seperator + self.description

        if self.glam_name:
            title += seperator + self.glam_name

        if self.file_id:
            title +=  seperator + self.file_id

        self.file_title = title + self.extension

    def get_filename(self):
        """
        returns created name of image file.
        :return:
        """
        return self.file_title
