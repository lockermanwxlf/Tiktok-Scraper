class Provision:
    def __init__(self, file, on_completed) -> None:
        self.file = file
        self.on_completed = on_completed

class Provider:
    '''
        A provider should create a file which will be written to by the download handler, and should handle the events that follow the completion of the file.
    '''
    def should_upload(directory: str, post_id: str, extension: str) -> bool:
        raise NotImplementedError()
    
    def provision(self, directory: str, filename: str) -> Provision:
        raise NotImplementedError()