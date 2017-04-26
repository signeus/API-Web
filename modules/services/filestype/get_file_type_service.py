from services.interfaces.i_service import IService


class GetFileTypeService(IService):
    def __init__(self, core, parameters):
        super(GetFileTypeService, self).__init__(core, parameters)
        self.core = core
        self.parameters = parameters


    def run(self):
        _type = self.parameters['type']
        _ext = self.parameters['ext']

        imagesTypeDictionary = {
            'png': '.png',
            'jpeg': '.jpeg',
        }

        videoTypeDictionary = {
            'mp4': '.mp4'
        }
        audioTypeDictionary = {
            'mp3': '.mp3'
        }

        applicationTypeDictionary = {
            'ex-xml': '.xls'
        }
        typesDictionary = {
            'images': imagesTypeDictionary,
            'application': applicationTypeDictionary,
            'video': videoTypeDictionary,
            "audio": audioTypeDictionary,
        }

        return typesDictionary[_type][_ext]