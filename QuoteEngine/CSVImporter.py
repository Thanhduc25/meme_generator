from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import pandas


class CSVImporter(IngestorInterface):
    """Helper module to read CSV file."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse CSV file and return a list of quote models."""
        quotes = []
        df = pandas.read_csv(path)
        for row in range(len(df)):
            quote = QuoteModel(df.iloc[row, 0], df.iloc[row, 1])
            quotes.append(quote)
        return quotes