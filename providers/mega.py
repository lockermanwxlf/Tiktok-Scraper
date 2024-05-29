import requests
import os
from posixpath import join
from .provider import Provider, Provision
import re

class MegaProvider(Provider):
    def __init__(self, mega_path) -> None:
        self.__mega_path = mega_path
    
    def should_upload(self, directory: str, filename: str) -> bool:
        return requests.get(
            url="http://localhost:15001/exists",
            params={
                "path": join(self.__mega_path, directory, filename)
            }
            ).json()["result"]
        
    def filter_list(self, directory: str, post_ids: list[str]):
        existing_filenames = requests.get(
            url="http://localhost:15001/list_dir",
            params={
                "path": join(self.__mega_path, directory)
            }
        ).json()["result"]
        pattern = re.compile(r"\d+")
        matches = [
            pattern.search(filename) for filename in existing_filenames
        ]
        matches = [
            match.group(0) for match in matches if match
        ]
        matches = list(set(matches))
        return [post_id for post_id in post_ids if post_id not in matches]
    
    def provision(self, directory: str, filename: str) -> Provision:
        os.makedirs("tmp", exist_ok=True)
        file = open(f"tmp/{filename}", "wb+")
        def on_complete():
            requests.put(
                url="http://localhost:15001/upload",
                data={
                    "path": join(self.__mega_path, directory, filename)
                },
                files={
                    "file": open(f"tmp/{filename}", "rb")
                }
            )
            
        return Provision(file, on_complete)