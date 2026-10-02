import pyautogui
from time import sleep

# pyautogui.click -> clica
# pyautogui.write -> escreve um texto
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta um atalho (hotkey)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "pythonimpressionador@gmail.com"

pyautogui.PAUSE = 0.5


# 1ª etapa: entrar no sistema da empresa
# utilizaremos o "pyautogui.press" para abrir o navegador.

pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

# fazer uma pausa maior pro site carregar.

sleep(3)

# 2ª etapa: fazer login

pyautogui.click(713, 371)
pyautogui.write(email)

pyautogui.press("tab") # passaremos para os próximos campos utilizando tab.
pyautogui.write("teste")
pyautogui.press("tab")
pyautogui.press("enter")

# fazer uma pausa maior pro site carregar.

sleep(4)

# 3ª etapa: abrir a base de dados (importar o arquivo)
# pip install pandas openpyxl

import pandas

tabela = pandas.read_csv("csv-produtos.csv", encoding="UTF-8")

# 4ª etapa: cadastrar os produtos

for linha in tabela.index: 
    # código
    pyautogui.click(675, 250)
    t_codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(t_codigo)
    pyautogui.press("tab")

    # marca 
    t_marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(t_marca)
    pyautogui.press("tab")

    # tipo
    t_tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(t_tipo)
    pyautogui.press("tab")

    # categoria
    t_categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(t_categoria)
    pyautogui.press("tab")

    # preço

    t_preco = str(tabela.loc[linha, "preco"])
    pyautogui.write(t_preco)
    pyautogui.press("tab")

    # custo

    t_custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(t_custo)
    pyautogui.press("tab")

    # obs

    t_obs = str(tabela.loc[linha, "obs"])
    if t_obs != "nan":    
        pyautogui.write(t_obs)
    pyautogui.press("tab")
    
    # enviar
    
    pyautogui.press("enter")  
    pyautogui.scroll(2000)    # retorna ao topo da página
