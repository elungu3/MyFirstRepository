from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC       #shortcut la expected condition in EC
browser = webdriver.Chrome()   #deschide browserul firefox
try:
    wait = WebDriverWait(browser, 10)   # asteapta 10 secunde sa se deschida browserul, daca nu se deschide, scriptul e FAIL
    browser.get("http://the-internet.herokuapp.com")   #deschide site-ul 'http://the-inter...'
    elements1 = browser.find_elements(By.TAG_NAME, 'a')   #gaseste toate cuvintele(elementele) din pagina care contin litera "a"
    elements2 = browser.find_elements(By.TAG_NAME, 'fooo')  #gaseste toate cuvintele(elementele) din pagina care contin "fooo"
    print(f'we found {len(elements1)} elements that is starting with "a" in your page')   #printeaza cate cuvinte(elemente contin "a")
    print(f'we found {len(elements2)} elements that is starting with "fooo" in your page')  #printeaza cate cuvinte(elemente contin "fooo")
    #browser.find_element(By.LINK_TEXT, 'Form Authentication')    #gaseste link text(text pe care apesi click si te duce pe alt link) "Form Authentication"
    form_auth_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Form Authentication')
    ))   #asteapta pana gaseste link-textul cu numele 'Form Authentication'
    form_auth_link.click()
    print(browser.current_url)   #printeaza link URL-ului pe care se afla browserul
    wait.until(EC.url_to_be('http://the-internet.herokuapp.com/login'))   #asteapta pana cand link pe care intra este cel mentionat.
    username = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#username')                         #Defineste variabila care asteapta pana cand gaseste CSS_SELECTORUL cu id username
    ))
    username.send_keys('tomsmith')   #apeland functia send_keys in variabila username, scrie in campul username 'Eduard'
    password = browser.find_element(By.CSS_SELECTOR, "#password")   #nu mai e nevoie sa folosesti wait.until pentru ca daca a aparut user, a aparut si password
    password.send_keys('SuperSecretPassword!')
    login = browser.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()   #facem click pe butonul de login.
    logout = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Logout')                           #asteapta pana apare si dupa apasa pe butonul de Logout
    )).click()
    logout_confirmation = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#flash')     #declaram o variabila care asteapta pana cand apare elementul care contine CSS_SELECTORUL flash
    ))
    assert "logged out" in logout_confirmation.text   #verifica daca avem 'logged out' in elementul declarat in variabila logout_confirmation
    # time.sleep(5)   #asteapta 5 secunde dupa rularea comenzilor de mai sus (nu e recomandat, e hardcoding)
#!!!!!!!!!!!!  DACA PRIMESTI EROAREA 'StaleElementReferenceException' s-a schimbat ceva in pagina web si trebuie sa verifici din nou testul !!!!!!!!!!
finally:    #la finalul rularii, orice s-ar intampla sa ruleze comanda urmatoare
    browser.quit()   #inchide browserul
print("The automation test has finished")
