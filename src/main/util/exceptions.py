class Error(Exception):
    """Base class for other exceptions"""
    pass

class InvalidMemberInTree(Error):
    """Raised when a member is not found in the family tree"""
    pass

class InvalidMotherForChildAddition(Error):
    """Raised when the mother of the child is male during child addition"""
    pass

class CommandLineArgumentNotAvailable(Error):
    """Raised when command line arguement is not passed"""
    pass

class InvalidFilePath(Error):
    """Raised when path is invalid"""
    pass


