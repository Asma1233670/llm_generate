from fpdf import FPDF
import os

class OutputHandler():
    def __init__(self, content, output_format, output_file):
        self.content=content
        self.output_format=output_format
        self.output_file=output_file
        self.save_output()
    
    def save_output(self):
        if self.output_format=='pdf':
            self.save_as_pdf()
        elif self.output_format=='txt':
            self.save_as_txt()
        else:
            raise ValueError(f"Unsupported output format: {self.output_format}")
    
    def save_as_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_font('ArialUnicode', '', 'Arial-Unicode-Regular.ttf', uni=True) 
        pdf.set_font("ArialUnicode", size=12)
        pdf.multi_cell(0, 10, self.content)
        pdf.output(self.output_file)
    
    def save_as_txt(self):
        with open(self.output_file, 'w', encoding='utf_8') as file:
            file.write(self.content)
