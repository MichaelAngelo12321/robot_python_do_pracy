from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv


# plik csv
lokalizacje = []
nośniki = []
uwagi = []
#pobieranie pliku excel
with open('blok.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter = ";")

    for line in reader:
        lokalizacja = line[4]
        uwaga = line[7]
        nośnik = line[2]

        lokalizacje.append(lokalizacja)
        nośniki.append(nośnik)
        uwagi.append(uwaga)

#koniec pliku csv









# Skrypt do odpalenia storny
driver = webdriver.Chrome("C:\chromedriver.exe")
driver.implicitly_wait(2)
driver.get("http://192.168.2.12:82/Tiger4.WebRole/Modules/StockItemByLocalization")
driver.minimize_window()

# Zmienne do logowania
print('logowanie')
login = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/section/form/div/fieldset/div[1]/div/input")
haslo = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/section/form/div/fieldset/div[2]/div/input")
logowanie = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/section/form/div/div/div/input")

# logowanie
a = input('wpisz login: ')
b = input('wpisz hasło: ')
login.send_keys(a)
haslo.send_keys(b)
logowanie.send_keys(Keys.ENTER)
print('użytkownik zalogowany')
# zmienna lokalizacji
#z = input('Jaka lokalizacja: ')

# wybieranie lokalizacji
search = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/input")
search.click()
search.send_keys(lokalizacje[1])
search.send_keys(Keys.ENTER)
time.sleep(2)
try:
    przycisk = driver.find_element(By.PARTIAL_LINK_TEXT, "Pokaż")
    przycisk.click()
except:
    print('Niepoprawna lokalizacja, sprawdź tą loklizację w pliku csv i odpal program jeszcze raz')
    wylogowywanie = driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/button")
    wylogowywanie2 = driver.find_element(By.XPATH, "/html/body/header/nav/div[2]/ul[2]/li[2]/a")
    wylogowanie3 = driver.find_element(By.XPATH, "/html/body/header/nav/div[2]/ul[2]/li[2]/ul/li[4]/a")

    # wylogowywanie
    time.sleep(10)
    wylogowywanie.click()
    wylogowywanie2.click()
    wylogowanie3.click()

    # zamykanie skryptu
    driver.close()

else:
    # zmienne do pętli
    y = input('Ile palet chcesz zablokować/odblokować: ')
    paleta = 0
    i = 1
    # pętla
    while paleta < int(y):
        guzik = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/section/div/div/div[2]/div[1]/h4/a")
        guzik.click()
        search2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/section/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/input")
        search2.clear()
        search2.click()
        search2.send_keys(nośniki[i])
        search2.send_keys(Keys.ENTER)
        time.sleep(3)
        try:
            przycisk = driver.find_element(By.PARTIAL_LINK_TEXT, "Pokaż")
            przycisk
        except:
            print('Nie ma tego nośnika w tej lokalizacji, program przechodzi do następnego nośnika sprawdź ten nośnik, którego nie ma')
            search2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/section/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/input")
            search2.clear()
            search2.click()
            paleta += 1
            i += 1
            search2.send_keys(nośniki[i])
            time.sleep(3)
            search2.send_keys(Keys.ENTER)
            przycisk = driver.find_element(By.PARTIAL_LINK_TEXT, "Pokaż")
            przycisk.click()
            guzik3 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[2]/button")
            guzik3.click()

            try:
                wpis = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/section/form/div[1]/div[2]/div/textarea")
                wpis
            except:
                print('paleta zablokowana, teraz ją odblokuje')
                guzik4 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[5]/button")
                guzik4.click()
                print('paleta odblokowana')
            else:
                wpis.send_keys(uwagi[i])
                guzik = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/section/form/div[2]/div/div/input[1]")
                guzik.click()
                guzik4 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[5]/button")
                guzik4.click()
                print('paleta zablokowana')
        else:
            przycisk = driver.find_element(By.PARTIAL_LINK_TEXT, "Pokaż")
            przycisk.click()
            guzik3 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[2]/button")
            guzik3.click()
            try:
                wpis = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/section/form/div[1]/div[2]/div/textarea")
                wpis
            except:
               print('paleta zablokowana, teraz ją odblokuje')
               guzik4 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[5]/button")
               guzik4.click()
               print('paleta odblokowana')
            else:
                wpis.send_keys(uwagi[i])
                guzik = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/section/form/div[2]/div/div/input[1]")
                guzik.click()
                guzik4 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[5]/button")
                guzik4.click()
                print('paleta zablokowana')

        paleta += 1
        i += 1

    # koniec pętli

    print('koniec programu za chwilę nastąpi wylogowanie')


    # zmienne do wylogowania
    zamykanie = driver.find_element(By.XPATH, "/html/body/div[3]/span")
    wylogowywanie = driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/button")
    wylogowywanie2 =  driver.find_element(By.XPATH, "/html/body/header/nav/div[2]/ul[2]/li[2]/a")
    wylogowanie3 = driver.find_element(By.XPATH, "/html/body/header/nav/div[2]/ul[2]/li[2]/ul/li[4]/a")


    # wylogowywanie
    time.sleep(15)
    wylogowywanie.click()
    wylogowywanie2.click()
    wylogowanie3.click()


    # zamykanie skryptu
    driver.close()























