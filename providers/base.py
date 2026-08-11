from abc import ABC, abstractmethod
from providers.models import ProviderResults
from httpx import AsyncClient

class BaseProvider(ABC):
    id = None
    name = "Undefined Provider"
    category = "undefined"
    source = "undefined"
    url = "http://127.0.0.1:8080/download/data.txt"
    

    def __init__(self, sesion: AsyncClient):
        self.session = sesion
        self.results = ProviderResults(self.name, self.category)

    
    @abstractmethod
    async def fetch(self) -> ProviderResults:
        ...
    

    

