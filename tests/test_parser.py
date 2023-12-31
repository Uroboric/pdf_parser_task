import pytest
from pdf_parser.parser import PDFParser


@pytest.mark.usefixtures('setup')
class TestParser:
    @pytest.mark.parametrize("input_text, fields, expected_output", [
        ("this text can be replased", ["this", "text", "can", "be", "replased"], "this \ntext \ncan \nbe \nreplased"),
    ])
    def test_insert_line_breaks(self, input_text, fields, expected_output):
        result = PDFParser.insert_line_breaks(input_text, fields).strip()
        assert result == expected_output

    @pytest.mark.parametrize("input_text, fields, expected_output", [
        ("PN: Product1\nSN: SN123\nMFG: Manufacturer1", ["PN", "SN", "MFG"],
         {"PN": "Product1", "SN": "SN123", "MFG": "Manufacturer1"}),
    ])
    def test_parse_pdf_info(self, input_text, fields, expected_output):
        result = PDFParser.parse_pdf_info(input_text, fields)
        assert result == expected_output

    def test_read_pdf(self, setup):
        result = setup.read_pdf()
        assert isinstance(result, dict)
        assert "PN" in result
        assert "SN" in result
        assert "MFG" in result

    def test_extract_barcodes_from_pdf(self, setup):
        result = setup.extract_barcodes_from_pdf()
        assert isinstance(result, list)
        assert len(result) == 2  # Assuming there should be at least 2 barcodes in the test PDF.

    def test_extract_and_add_barcodes_to_pdf_info(self, setup):
        pdf_info = {"PN": "Product1", "SN": "SN123"}
        setup.extract_and_add_barcodes_to_pdf_info(pdf_info)
        assert "BARCODES" in pdf_info
        assert isinstance(pdf_info["BARCODES"], list)
        assert len(pdf_info["BARCODES"]) == 2  # Assuming there should be at least 2 barcodes in the test PDF.
