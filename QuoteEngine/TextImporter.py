from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextImporter(IngestorInterface):
    """Helper class to read text file."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse text file and return a list of quote models."""
        quotes = []
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                if line != "":
                    quote_model = QuoteModel(line, None)
                    quotes.append(quote_model)
        return quotes