from docx import Document
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface

class DocxImporter(IngestorInterface):
    """Helper module to read Docx file."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse Docx file and return a list of quote models."""
        quotes = []
        document = Document(path)
        for paragraph in document.paragraphs:
            if paragraph.text != "":
                parsed_quote = QuoteModel(paragraph.text, None)
                quotes.append(parsed_quote)
        return quotes