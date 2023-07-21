import pytest
from pdf_parser.parser import PDFParser


@pytest.fixture(scope='function')
def setup():
    pdf_file_path = 'pdf_file/test_task.pdf'
    pdf_parser = PDFParser(pdf_file_path)
    yield pdf_parser
