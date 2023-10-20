from selenium import webdriver
from selenium.webdriver.common.by import By

# Создайте экземпляр драйвера (в данном случае для браузера Chrome)
driver = webdriver.Chrome()

# Откройте веб-страницу, на которой находится картинка
driver.get('http://suninjuly.github.io/cats.html')

# Найдите элемент, содержащий картинку, по его селектору (CSS-селектору)
# Замените селектор на соответствующий на вашей веб-странице
image_element = driver.find_element(By.CSS_SELECTOR, 'img#bullet')

# Получите URL картинки из атрибута src
image_url = image_element.get_attribute('src')

# Сохраните картинку на вашем компьютере
import requests
response = requests.get(image_url)

# Укажите путь для сохранения картинки на вашем компьютере
save_path = 'C:/Users/User/Desktop/Новая папка/1.jpg'

# Откройте файл для записи в бинарном режиме и сохраните в него содержимое
with open(save_path, 'wb') as file:
    file.write(response.content)

# Закройте браузер после завершения операции
driver.quit()