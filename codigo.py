import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(3)

pyautogui.click(x=883, y=375)
pyautogui.write('diogokglms@hotmail.com')
pyautogui.press('tab')
pyautogui.write('Ra06ra02')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(3)

tabela = pd.read_csv('produtos.csv')

for linha in tabela.index:

    pyautogui.click(x=934, y=258)   
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press('tab')
    obs = (str(tabela.loc[linha, "obs"]))
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(5)
          
