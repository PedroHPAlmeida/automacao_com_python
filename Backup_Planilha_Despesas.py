import pyautogui
from time import sleep

pyautogui.alert('O código irá iniciar...\nNão use o computador até que o script seja totalmente executado!')
pyautogui.PAUSE = 1

#entrando no gerenciador de arquivos
pyautogui.press('winleft')
pyautogui.write('arquivo')
pyautogui.press('enter')

#digitando o endereco onde fica o backup reserva
pyautogui.moveTo(1472, 157)
pyautogui.click()
pyautogui.write('C:\\Users\\Pichau\\OneDrive\\Documentos\\Pessoal\\Financeiro\\Planilha de Gastos\\Backup')
pyautogui.press('enter')

#apagando o backup reserva
pyautogui.moveTo(348, 222)
pyautogui.click()
pyautogui.hotkey('shift', 'del')
pyautogui.moveTo(1040, 611)
pyautogui.click()

#indo para a pasta de backup imediato
pyautogui.moveTo(1472, 157)
pyautogui.click()
pyautogui.write('C:\\Users\\Pichau\\OneDrive\\Documentos\\Pessoal\\Financeiro\\Planilha de Gastos')
pyautogui.press('enter')
pyautogui.moveTo(323, 290)
pyautogui.click()
pyautogui.hotkey('ctrl', 'x') #copiando o backup imediato

#voltando para o endereco onde fica o backup reserva
pyautogui.moveTo(1472, 157)
pyautogui.click()
pyautogui.write('C:\\Users\\Pichau\\OneDrive\\Documentos\\Pessoal\\Financeiro\\Planilha de Gastos\\Backup')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'v') #colando o arquivo
sleep(1)

#entrando na pasta onde esta o arquivo Despesas Lite local
pyautogui.moveTo(1472, 157)
pyautogui.click()
pyautogui.write('C:\\Users\\Pichau\\Documents\\Pessoal\\Financeiro')
pyautogui.press('enter')
pyautogui.moveTo(307, 225)
pyautogui.click()
pyautogui.hotkey('ctrl', 'c') #copiando o arquivo

#indo para a pasta de backup imediato
pyautogui.moveTo(1472, 157)
pyautogui.click()
pyautogui.write('C:\\Users\\Pichau\\OneDrive\\Documentos\\Pessoal\\Financeiro\\Planilha de Gastos')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'v')
sleep(1)

#abrindo o one drive para sincronizar as modificacoes
pyautogui.press('winleft')
pyautogui.write('OneDrive')
pyautogui.press('enter')
sleep(2)
pyautogui.moveTo(1890, 10)
pyautogui.click()
sleep(1)
pyautogui.click()
sleep(1)
pyautogui.alert('Código executado!')
