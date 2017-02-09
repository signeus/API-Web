from services.interfaces.i_service import IService


class GetFileTypeService(IService):
    def __init__(self, core, parameters):
        super(GetFileTypeService, self).__init__(core, parameters)
        self.core = core
        self.parameters = parameters


    def run(self):
        #_data = self.parameters['_data_file_extension']
        _type = self.parameters['type']
        _ext = self.parameters['ext']

        imagesTypeDictionary = {
            'png': '.png',
            'jpeg': '.jpeg'
        }
        applicationTypeDictionary = {
            'ex-xml': '.xls'
        }
        typesDictionary = {
            'images': imagesTypeDictionary,
            'application': applicationTypeDictionary,
        }

        return typesDictionary[_type][_ext]