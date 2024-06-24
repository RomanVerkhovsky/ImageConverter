from src.core.converter import AppConverter


class GUI:

    def __init__(self):

        self.converter = AppConverter()

    def run(self):
        print("IMAGE CONVERTER___   ")

        path = input("Input path to image and enter to convert >> ")\

        img_format = ""

        while img_format not in self.converter.get_formats():

            print("Доступны следующие форматы для конвертации:")
            print("-", ("\n- ".join(self.converter.get_formats())), "\n")

            img_format = input("Введите нужный формат >> ")

        self.converter.convert_image(path)

        input(f"Image was converted to {self.converter.get_converter_format()}!\n Enter to exit...")
