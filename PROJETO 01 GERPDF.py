import fdpf

from fpdf import FPDF
projeto = input("Digite a descricao do projeto: ")
horas_previstas = input("Digite a quantidade de horas previstas: ")
valor_hora = input("Digite valor da hora trabalhada: ")
prazo = input("Digite o prazo estimado: ")
valor_total = int(horas_previstas) * int(valor_hora)
print(valor_total)
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")

pdf.image("template.png",x=0, y=0)
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_previstas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso!")