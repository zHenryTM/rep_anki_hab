from fpdf import FPDF


class PDF_Generator(FPDF):
    def header(self):
       self.image('./images/design/lists_pages_design.png', x=0, y=0, w=self.w, h=self.h, type='png')


    def add_my_link(self, x, y, txt, link):
        self.set_xy(x, y)
        self.set_text_color(0, 0, 0)
        self.set_font('Times', 'BI', 12)
        self.add_link()

        text_width = self.get_string_width(txt) + 6  # Soma-se 6 para adicionar uma margem de 3 em cada lado.

        # desenhar o retângulo em torno do texto
        self.set_fill_color(255, 112, 79)
        self.cell(text_width, 10, '', border=0, ln=0, fill=True, align='C', link=link)

        # adicionar o texto com o link
        self.set_xy(x, y)
        self.cell(text_width, 10, txt, border=0, ln=1, align='C', link=link)


    # Footer da página.
    def footer(self):
      if self.page_no() != 1:
        self.image("./images/design/enemaster_logo.png", x=90, y=283, h=10,type='png')
        self.set_y(0)
        self.set_font('Arial', 'BI', 8)
        self.cell(0, 8, '     '+str(self.page_no()) + '/{nb}', 0, 0, 'C')
