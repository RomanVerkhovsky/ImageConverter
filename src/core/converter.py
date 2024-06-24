from __future__ import annotations
from abc import ABC, abstractmethod
from PIL import Image
import os


class IConverterCreator(ABC):

    @abstractmethod
    def _create_converter(self, image_out_format: str) -> IImageConverter:
        pass


class IImageConverter(ABC):

    @abstractmethod
    def get_format(self) -> str: pass
    @abstractmethod
    def convert(self, path_in: str) -> None: pass


class PNGConverter(IImageConverter):

    image_format = "png"

    def __init__(self):
        self._image_format = self.image_format

    def get_format(self) -> str:

        return self._image_format

    def convert(self, path_in: str) -> None:

        assert isinstance(path_in, str), "Error: path is not string"
        assert os.path.isfile(path_in), "Error, file not found"

        image = Image.open(path_in)

        name = os.path.splitext(path_in)[0] + f".{self.image_format}"
        image.save(name, format=self.image_format)


class JPEGConverter(IImageConverter):

    image_format = "jpg"

    def __init__(self):

        self._image_format = self.image_format

    def get_format(self) -> str:

        return self._image_format

    def convert(self, path_in: str) -> None:

        assert isinstance(path_in, str), "Error: path is not string"
        assert os.path.isfile(path_in), "Error, file not found"

        image = Image.open(path_in)

        name = os.path.splitext(path_in)[0] + f".{self.image_format}"
        image.save(name, format=self.image_format)


class AppConverter(IConverterCreator):

    converter: IImageConverter

    def __init__(self) -> None:

        self.formats = {
            "jpg": JPEGConverter(),
            "png": PNGConverter()
        }

        self.converter = self.formats["png"]

    def _create_converter(self, image_out_format: str) -> IImageConverter:

        assert isinstance(image_out_format, str), "Error, type not string"
        assert image_out_format in list(self.formats.keys()), "Error, format is not supported"

        return self.formats[image_out_format]

    def set_converter(self, image_out_format: str) -> None:

        self.converter = self._create_converter(image_out_format)

    def get_formats(self) -> list:

        return [key for key in self.formats]

    def get_converter_format(self) -> str:

        return self.converter.get_format()

    def convert_image(self, path_in: str):

        self.converter.convert(path_in)
