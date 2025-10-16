import configparser
class ConfigReader:
    def __init__(self,config:configparser.ConfigParser):
        self.config = config
    def ReadByKey(self,section:str,key:str):
        if self.config[section][key]!="":
            if self.config[section][key] in ["true","false"]:
                return self.config[section].getboolean(key)
            elif self.config[section][key].isdigit():
                return self.config[section].getint(key)
            elif self.config[section][key].replace('.','',1).isdigit() and self.config[section][key].count('.') < 2:
                return self.config[section].getfloat(key)
            else:
                return self.config[section][key]