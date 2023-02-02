import pandas as pd
from fpdf import FPDF as FP

pdf = FP(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

data = pd.read_csv("topics.csv")
for index, row in data.iterrows():
	ran1 = 21
	pdf.add_page()
	pdf.set_font(family="Helvetica", style="B", size=24)
	pdf.set_text_color(100, 100, 101)
	pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
	for line in range(10, 271, 10):
		pdf.line(10, ran1, 200, ran1)
		ran1 += 10
	pdf.ln(265)
	pdf.set_font(family="Times", style="I", size=8)
	pdf.set_text_color(180, 180, 180)
	pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
	for item in range(row["Pages"] - 1):
		ran2 = 10
		pdf.add_page()
		for line in range(10, 281, 10):
			pdf.line(10, ran2, 200, ran2)
			ran2 += 10
		pdf.ln(277)
		pdf.set_font(family="Times", style="I", size=8)
		pdf.set_text_color(180, 180, 180)
		pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output(rf"notebook.pdf")
