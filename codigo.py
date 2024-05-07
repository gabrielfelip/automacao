import pyautogui
import time

pyautogui.PAUSE = 0.8

#apertar tecla windowns
pyautogui.press("win")
#procurar chrome
pyautogui.write("chrome")
#apertar enter
pyautogui.press("enter")
#digitar link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
#pressionar enter
pyautogui.press("enter")
#aguardar 2 segundos
time.sleep(2)
#clicar na posição em que o mouse está
pyautogui.click(x=523, y=380)
#digitar email
pyautogui.write("gabriel_felype@hotmail.com")
#pressinao tab
pyautogui.press("tab")
#digitar senha
pyautogui.write("gabriel")
#pressionar tab
pyautogui.press("tab")
#pressionar enter
pyautogui.press("enter")

#abrir/importar a base de dados de produtos para cadastras
# pip install pandas numpy openpyxl

import pandas

tabela = pandas.read_csv("produtos.csv")
#variavel do codigo de um produto

for linha in tabela.index:
    codigo = str (tabela.loc[linha, "codigo"])
    #clicar no campo codigo do produto
    pyautogui.click(x=538, y=253)
    #escrever codigo
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #condição para observação ser preenchida ou não
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

    

