from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Verify if the file type is compatible with the ingestor class."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Check path is applicable for each ingestor class or not."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Nothing to pass here."""
        pass