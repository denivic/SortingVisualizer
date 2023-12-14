# Standard modules
from platform import python_version_tuple
from logging import getLogger, setLoggerClass

# Custom modules


class SortingVisualizer():
    from modules.algorithms import SortingAlgorithms
    from modules.constants import Constants
    from modules.utilitymanager import UtilityManager
    from modules.logger import CustomLogger
    
    version = Constants.SUDOCUCHECKER_VERSION
    documentation_path = Constants.DOCUMENTATION_PATH

    _author = "dea@ufm.dk"
    _maintainer = "dea@ufm.dk"
    _version = version
    
    def __init__(self):
        setLoggerClass(self.CustomLogger)
        self.logger = getLogger('__name__')
        self.logger.propagate = False  # Prevents duplicate console logs
        
        # Initialize components
        self.algorithms = self.SortingAlgorithms()
        self.utils = self.UtilityManager()
        self.constants = self.Constants()
        
        
    def run(self, algorithm: str):
        pass

