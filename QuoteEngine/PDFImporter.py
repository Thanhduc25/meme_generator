from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import subprocess
import random
import os


class PDFImporter(IngestorInterface):
    """Helper module to read PDF file."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse PDF file and return a list of quote models."""
        quotes = []
        temp_txt_file = f"temp_{random.randint(1, 1000000)}.txt"
        try:
            subprocess.call(["pdftotext", path, temp_txt_file])
            with open(temp_txt_file, 'r') as file:
                for line in file:
                    if line.strip() != "":
                        lines_separate = line.split("-")
                        if len(lines_separate) < 2:
                            continue
                        quote, author = lines_separate[0], lines_separate[1]
                        quote = quote.strip()
                        author = author.strip()
                        quote_model = QuoteModel(quote, author)
                        quotes.append(quote_model)
        finally:
            os.remove(temp_txt_file)
        return quotes