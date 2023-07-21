import pdfplumber
from pyzbar import pyzbar
from PIL import Image
import tempfile


class PDFParser:
    pdf_file_path = 'pdf_file/test_task.pdf'

    def __init__(self, file_path):
        self.file_path = file_path

    @staticmethod
    def insert_line_breaks(text, fields):
        for field in fields:
            text = text.replace(field, "\n" + field)
        return text.strip()

    @staticmethod
    def parse_pdf_info(text, fields) -> dict:
        pdf_info = {}
        all_lines = text.split('\n')
        for i, current_line in enumerate(all_lines):
            current_line = current_line.strip()
            if current_line.startswith(tuple(fields)):
                key, value = current_line.split(':', 1)
                key = key.strip()
                value = value.strip()
                if key == "NOTES" and i + 1 < len(all_lines):
                    value = all_lines[i + 1].strip()
                pdf_info[key] = value

        return pdf_info

    def read_pdf(self) -> dict:
        with pdfplumber.open(self.file_path) as pdf:
            first_page = pdf.pages[0]
            text = first_page.extract_text()

            fields = [
                "PN", "SN", "LOCATION", "CONDITION", "RECEIVER#", "UOM", "EXP DATE",
                "PO", "REC.DATE", "MFG", "BATCH#", "DOM", "REMARK", "LOT# ", "TAGGED BY",
                "NOTES", "Qty"
            ]

            formatted_text = self.insert_line_breaks(text, fields)
            pdf_info = self.parse_pdf_info(formatted_text, fields)

            return pdf_info

    @staticmethod
    def save_page_as_image(page, resolution=150):
        image = page.to_image(resolution=resolution)
        temp_filename = tempfile.NamedTemporaryFile(suffix=".png").name
        image.save(temp_filename)
        return temp_filename

    @staticmethod
    def decode_barcodes_from_image(image_path):
        with open(image_path, 'rb') as temp_file:
            pil_image = Image.open(temp_file).convert("L")
            return pyzbar.decode(pil_image)

    def extract_barcodes_from_pdf(self) -> list:
        all_barcodes = []

        with pdfplumber.open(self.file_path) as pdf:
            for page in pdf.pages:
                image_path = self.save_page_as_image(page)
                decoded_barcodes = self.decode_barcodes_from_image(image_path)
                all_barcodes.extend(decoded_barcodes)

        return all_barcodes

    def extract_and_add_barcodes_to_pdf_info(self, pdf_info):
        extracted_barcodes = self.extract_barcodes_from_pdf()
        barcode_data = [barcode.data.decode("utf-8") for barcode in extracted_barcodes]
        pdf_info["BARCODES"] = barcode_data

    def main(self):
        extracted_info = self.read_pdf()
        self.extract_and_add_barcodes_to_pdf_info(extracted_info)

        print("PDF Info:", extracted_info)

        if "BARCODES" in extracted_info:
            print("Распознанные штрихкоды:")
            for barcode in extracted_info["BARCODES"]:
                print(barcode)
        else:
            print("Штрихкоды не найдены")


if __name__ == "__main__":
    use_file_path = PDFParser.pdf_file_path
    parser = PDFParser(use_file_path)
    parser.main()
