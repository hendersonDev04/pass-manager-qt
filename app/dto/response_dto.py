# from pydantic import BaseModel

class ResponseDto():

    def __init__(self, id_response : int, message : str):
        self.id_response : int = id_response
        self.message : str = message