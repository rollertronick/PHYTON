import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

ticker = ""

ticker = input ("digite o codigo da acao desejada: ") 
dados = yfinance.Ticker(ticker).history(start="2020-01-01", end="2020-12-31") 
dados.Close
fechamento = dados.Close

maxima = round (fechamento.max(), 2) 
minima = round (fechamento.min(), 2)
valor_medio = round (fechamento.mean(), 2)

destinatario = "taniavavriv1@gmail.com"
assunto = "analise do projeto 2024"
mensagem = f"""
Prezado gestor,
Seguem as analises solicitadas da acao {ticker}:
cotacao maxima: R$ {maxima}:
cotacao minima : R$ {minima}:
valor medio: R$ {valor_medio}:

Qualquer duvida estou a disposicao!

Atenciosamente.
"""
webbrowser.open("www.gmail.com")
time.sleep(3)
pyautogui.PAUSE = 3
pyautogui.click(x=115, y=234)
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.click(x=1113, y=997)
pyautogui.click("ctrl", "f4")
print ("e-mail enviado com sucesso")