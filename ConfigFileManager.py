import pandas as pd

class ConfigFileManager:
    configFileName = 'blackjack.conf'
    def __init(self):
        pass
    def _readConfigFile(self):
        """
        Reads the config file and returns the config data as a pandas.DataFrame
        :return: the config file data
        :rtype pandas.DataFrame:
        """
        configDF = pd.read_csv(self.configFileName, index_col='index')
        return configDF
    @property
    def gameNumber(self):
        """
        Get the gameNumber from the config file.
        :return: the game number stored in the config file
        :rtype int:
        """
        configDF = self._readConfigFile()
        value = int(configDF['gameNumber'][0])
        return value
    @gameNumber.setter
    def gameNumber(self, value):
        """
        Save the gameNumber to the config files
        :param value: the value to set gameNumber to
        :type value: int
        :return: none
        :rtype None:
        """
        if not isinstance(value, int):
            raise TypeError("gameNumber can only be set to an integer value")

        # save gameNumber to the config file
        configDF = self._readConfigFile()
        configDF.iloc[0]['gameNumber'] = value
        configDF.to_csv(self.configFileName, sep=',', header=True, index=True)
