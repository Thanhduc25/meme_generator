from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .CSVImporter import CSVImporter
from .DocxImporter import DocxImporter
from .PDFImporter import PDFImporter
from .TextImporter import TextImporter
from typing import List


class Ingestor(IngestorInterface):
    """Inheirit from IngestorInterface class."""

    ingestors = [CSVImporter, DocxImporter, PDFImporter, TextImporter]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Parse method."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
