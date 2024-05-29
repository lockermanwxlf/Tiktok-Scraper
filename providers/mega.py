import requests
import os
from .provider import Provider, Provision

class MegaProvider(Provider):
    def __init__(self, mega_path) -> None:
        self.__mega_path = mega_path
    
    def should_upload(self, directory: str, filename: str) -> bool:
        return requests.get(
            url="http://localhost:15001/exists",
            params={
                "path": os.path.join(self.__mega_path, directory, filename)
            }
            ).json()["result"]
    
    def provision(self, directory: str, filename: str) -> Provision:
        os.makedirs("tmp", exist_ok=True)
        file = open(f"tmp/{filename}", "wb+")
        def on_complete():
            requests.put(
                url="http://localhost:15001/upload",
                data={
                    "path": os.path.join(self.__mega_path, directory, filename)
                },
                files={
                    "file": open(f"tmp/{filename}", "rb")
                }
            )
            
        return Provision(file, on_complete)