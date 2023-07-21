import pytest
from pdf_parser.parser import PDFParser


@pytest.fixture(scope='function')
def setup():
    pdf_file_path = 'https://github.com/Uroboric/pdf_parser_task/blob/9d9d06bccad9b4efa5423ea9185525d4a8358883/pdf_file/test_task.pdf'
    pdf_parser = PDFParser(pdf_file_path)
    yield pdf_parser
