# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
import random
from wordcloud import WordCloud

class SaveDefaultBannerImageService(IService):
    def __init__(self, core, parameters):
        super(SaveDefaultBannerImageService, self).__init__(core, parameters)

    def color(self, word, font_size, position, orientation, random_state=None,
              **kwargs):
        blue = str(random.randint(185, 210))
        luminosity = str(random.randint(30, 90))
        saturation = str(random.randint(50, 100))
        return "hsl(" + blue + ", " + saturation + "%, " + luminosity + "%)"

    def run(self):
        _id = self.parameters.get("id", None)
        _keywords = self.parameters.get("keywords", [])
        _description = self.parameters.get("description", "")
        _path = self.parameters.get("path", 'unknown/')

        filename = _id + ".png"

        content_words = str(" ".join(_keywords)) + " " + str(_description)
        content_lis = content_words.split(" ")

        if len(content_lis) <= 10:
            print "Hacemos el aleatorio del Kaiser Ainar"
            content_lis = ["hey","pepe","tomas","kluiver","rodriguez","pez","bandera","big","data","analitycs","machine","learning","K","L","R","A","J"]
            #TODO Create method with random posts and generate

        numPalabras = random.randint(10, len(set(content_lis)))
        state = random.randint(2, 45)
        print numPalabras
        print state
        widthMax = 860
        heightMax = 250
        wc = WordCloud(width=widthMax, height=heightMax, max_words=numPalabras, random_state=state, mode="RGBA",
                       background_color=None)
        wc.generate(" ".join(content_lis))
        wc.recolor(color_func=self.color)
        _path = self.core.GetMediaResources()["media_folder"] + _path

        wc.to_file(_path + filename)
        return _id
