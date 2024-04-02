from sqlalchemy import Column, LargeBinary, Integer, String, Text
from app.configurations.DataBase import DB
import json as js

class Presente(DB.Model):
    id = Column(Integer, primary_key=True, nullable=False)
    p_titulo = Column(String(100))
    p_imagem = Column(Text)
    p_nome = Column(Text)
    p_mimeType = Column(Text)
    p_links = Column(LargeBinary)


    def __init__(self, titulo: str, imagem: str, nome: str, mimType: str, links: dict) -> None:
        self.p_titulo = titulo
        self.p_imagem = imagem
        self.p_nome = nome
        self.p_mimeType = mimType
        self.p_links = links

    
    def converteBytesLinks(self) -> bytes:
        jsondata = js.dumps(self.p_links)

        self.p_links = bytes(jsondata, encoding='utf-8')
    

    def converterDictLinks(self) -> None:
        jsonData = self.p_links.decode("utf-8")
        jsonData = js.loads(jsonData)

        self.p_links = jsonData