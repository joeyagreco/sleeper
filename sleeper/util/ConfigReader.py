import configparser
import os


class ConfigReader:
    """
    Used to read from .properties files
    """
    __propertiesFileName = "app.properties"

    @classmethod
    def get(cls, section: str, name: str, asType=None) -> str:
        configParser = configparser.ConfigParser(converters={'list': lambda x: [i.strip() for i in x.split(',')]})
        propertiesFilePath = os.path.abspath(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"../{cls.__propertiesFileName}"))
        configParser.read(propertiesFilePath)
        if asType == list:
            return configParser.getlist(section, name)
        elif asType is None:
            return configParser[section][name]
        else:
            raise ValueError(f"Type conversion for '{asType}' not supported.")
