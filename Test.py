from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

driver = webdriver.Chrome(executable_path='C:/chromedriver_win32/chromedriver.exe')
driver.maximize_window()
login_url = 'https://www.linkedin.com/login'
driver.get(login_url)
email_xpath = """//*[@id="username"]"""
email_id = 'Your Email'
find_email_element = driver.find_element_by_xpath(email_xpath)
find_email_element.send_keys(email_id)

time.sleep(3)

password_xpath = """//*[@id="password"]"""
password = 'Your Password'
find_pass_element = driver.find_element_by_xpath(password_xpath)
find_pass_element.send_keys(password)
find_pass_element.send_keys(Keys.ENTER)

urls_list = [
              'https://www.linkedin.com/in/eldor-ibragimov-aa71b613b/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=c69b4543-1ed3-4c5d-8374-0ee3dd62c030&external_page_instance=122d39a6-8f49-4475-b3e3-ca4fe1d2cde7',
            'https://www.linkedin.com/in/kartavya-singh-826537186/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=c69b4543-1ed3-4c5d-8374-0ee3dd62c030&external_page_instance=0e0c2c14-c6cf-4972-83b3-abae7e21a76a', 'https://www.linkedin.com/in/aamirr/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=c69b4543-1ed3-4c5d-8374-0ee3dd62c030&external_page_instance=8657c9f8-a1c3-4ec5-a1db-d1c1ed39a5aa', 'https://www.linkedin.com/in/tishant-chandrakar/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=c69b4543-1ed3-4c5d-8374-0ee3dd62c030&external_page_instance=86708351-9570-414c-a440-fb6d3f71565d', 'https://www.linkedin.com/in/anthony-radtke-356207133/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=c69b4543-1ed3-4c5d-8374-0ee3dd62c030&external_page_instance=0ae76034-d83b-43ee-8e54-f11639c77bda', 'https://www.linkedin.com/in/yunbo-wang/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=c69b4543-1ed3-4c5d-8374-0ee3dd62c030&external_page_instance=7c9c41f8-465f-4e0d-9c50-537a5d6c5aaa', 'https://www.linkedin.com/in/anmol-gulwani/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=c69b4543-1ed3-4c5d-8374-0ee3dd62c030&external_page_instance=daffc2ed-3eb1-4be4-b343-ac582ea65f15', 'https://www.linkedin.com/in/thenandkishorkumawat/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=c69b4543-1ed3-4c5d-8374-0ee3dd62c030&external_page_instance=90e55f08-24b5-434e-a048-213e964555f8', 'https://www.linkedin.com/in/manish-thanneeru/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=c69b4543-1ed3-4c5d-8374-0ee3dd62c030&external_page_instance=8a7cf048-ca63-414c-b1ec-ed7f7b7fc8da', 'https://www.linkedin.com/in/taras-bulubas-b1448b3/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=c69b4543-1ed3-4c5d-8374-0ee3dd62c030&external_page_instance=c7959a8d-dadf-47eb-a08c-b71d9922c7c3', 'https://www.linkedin.com/in/pronoysarkar/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=c69b4543-1ed3-4c5d-8374-0ee3dd62c030&external_page_instance=813b3cf8-8629-40d9-8fed-5156904b0a89', 'https://www.linkedin.com/in/saket-mohanty-b5039198/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=c69b4543-1ed3-4c5d-8374-0ee3dd62c030&external_page_instance=b53fd13f-117c-420b-98a0-07809e8aefd5', 'https://www.linkedin.com/in/sathvik-nallamalli/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=c69b4543-1ed3-4c5d-8374-0ee3dd62c030&external_page_instance=3818af88-c32f-4053-913e-eecdacd0ce98', 'https://www.linkedin.com/in/abrarmajeedi/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=c69b4543-1ed3-4c5d-8374-0ee3dd62c030&external_page_instance=98e489f7-2118-4f71-9d46-faa01e33f6f7', 'https://www.linkedin.com/in/chiravdave?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=dfcc1bd4-227e-45cc-947c-f19569a1798d', 'https://www.linkedin.com/in/jeremy-luna-717291139?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=17be84ef-30c0-43b5-9a66-8efaad96664a', 'https://www.linkedin.com/in/varun-rajasekar-70a653119?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=c6dbea33-1187-45ed-8fca-0b68aa7237f4', 'https://www.linkedin.com/in/andeririondo?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=09d0cd41-3f49-40f7-a3c2-b1a4eb34983b', 'https://www.linkedin.com/in/hoorarezaeim?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=18bf1a8e-f727-41ab-8735-c51081ec5a2b', 'https://www.linkedin.com/in/yacine-brahim-002104193?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=f54743a4-9146-426b-a1e0-c4aef128b9ee', 'https://www.linkedin.com/in/xiangle-cheng-b837ba107?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=267138e5-915f-4a4f-bb62-2544dffc0f57', 'https://www.linkedin.com/in/msharm05/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=b1d012b9-ae0b-4cc6-9f97-99e5713684b8', 'https://www.linkedin.com/in/navaneeth-kt-0978b513b?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=e729270f-f414-4c39-97e3-3585880793f8', 'https://www.linkedin.com/in/terrance-whitehurst/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=5b6530a4-903c-4e0c-8288-85129fb1b7a6', 'https://www.linkedin.com/in/harshal-mittal-48487a138?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=31556420-b4ef-4ce9-8c78-ec2463b195cb', 'https://www.linkedin.com/in/ross-byrne-5992b5107/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=53bf8513-40f1-4d6f-809e-c85a5ec67233', 'https://www.linkedin.com/in/manikanthr5/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=87e66e2f-f0d0-4ef8-b5b3-9b89c77810e9', 'https://www.linkedin.com/in/himansu-didwania?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=45d24e75-56af-4356-8006-81d0aebef443', 'https://www.linkedin.com/in/arunika-yadav-aa2572121?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=795f4712-8aaa-45d2-a10d-4de5207b6891', 'https://www.linkedin.com/in/zhaoqi-zhang-05916aa6?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=8fbe6507-f54d-416e-9ce7-686a23d7248f', 'https://www.linkedin.com/in/yongwoo-cho-00629a169?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=a8f05209-1581-4c9d-b888-636d6a8542af', 'https://www.linkedin.com/in/maitreya-rayabharam?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=630f0a49-4cd5-4338-a7b3-837baebc9027', 'https://www.linkedin.com/in/nggih?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=51cfa15b-f5cd-4846-ad21-9450e52023f4', 'https://www.linkedin.com/in/narendoraiswamy?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=305250e6-482b-4b26-a0e4-2eba7e2fece8', 'https://www.linkedin.com/in/siddhartha-dhar?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=49d23b05-49c6-481a-88d6-5448082846ac', 'https://www.linkedin.com/in/yash-here?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=d21f2ff7-bdfd-41cb-b0a8-8cd11ac0537a', 'https://www.linkedin.com/in/kosate?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=b098319a-d92c-4c19-a557-b4d5cd9fa4a4', 'https://www.linkedin.com/in/adriaciurana?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=c07674cc-5756-4a09-a79d-cd97a038b8d3', 'https://www.linkedin.com/in/dung-nguyen-6a5227143?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=d5a3a737-14d8-45b5-8bb8-5288d2e777d1', 'https://www.linkedin.com/in/mohammad-ahmad-ai/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=4c9c4c53-3748-405e-88a3-2e5408ad874a', 'https://www.linkedin.com/in/mirkomastrelli/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=88eb80aa-d1b3-42e8-a74a-aaef971171de', 'https://www.linkedin.com/in/sean-leary-0839b14/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=6ca481ea-5a48-42e2-956a-5be9fb3b2a23', 'https://www.linkedin.com/in/dmitry-temnov-b9367b174/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=84dc8c19-3b05-495d-a889-07440f45ee4f', 'https://www.linkedin.com/in/jo%c3%a3o-lucas-felipe-4b5136148/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=f1596833-fb0f-4ce5-84b0-eed00db18b83', 'https://www.linkedin.com/in/amirhf?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=a5c77264-6d57-407f-ba8b-9a70514b548a', 'https://www.linkedin.com/in/sachin-sharma-a20ab914a?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=0a4c4ebf-f86b-4510-b1a9-76ef9dc3e1c3', 'https://www.linkedin.com/in/chandni-soni-930057a7/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=9675f72d-e74e-4b88-aa0b-91b326f4508b', 'https://www.linkedin.com/in/dohyeong-kim-1389b0103/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=3a499b65-c2c5-4f28-869b-8c158b7b1063', 'https://www.linkedin.com/in/jonathon-rice-040269153?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=d7c63d08-1521-435a-a1fb-9219cfff42e9', 'https://www.linkedin.com/in/deepakaltran?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=6ad15461-870f-4c82-be33-1b14d60fa4a1&external_page_instance=0eaa8d78-c139-473f-94a0-487f22ea00ea']

# urls = open('Url_list.txt', 'r')
# content = urls.read()
# urls_list.append(content)
# urls.close()

name_list = []
title_list = []
company_list = []
country_list = []
linkedin_list = []

for link in urls_list:
    time.sleep(2)
    driver.get(link)
    driver.implicitly_wait(10)
    src = driver.page_source
    html_soup = bs(src, 'lxml')

    name = html_soup.find('h1', {'class': 'text-heading-xlarge inline t-24 v-align-middle break-words'})
    name_text = name.get_text().strip()
    text_0 = name_text
    name_list.append(text_0)

    try:
        title = html_soup.find('h3', {'class': 't-16 t-black t-bold'})
        title_text = title.get_text().strip()
        text_1 = title_text
        title_list.append(text_1)
    except:
        erroe = "not found Ttile"
        title_list.append(erroe)

    try:
        company = html_soup.find('p', {'class': 'pv-entity__secondary-title t-14 t-black t-normal'})
        company_text = company.get_text().strip()
        text_3 = company_text
        company_list.append(text_3)

    except:
        error = 'Company Not Found'
        company_list.append(error)

    country = html_soup.find('span', {'class': 'text-body-small inline t-black--light break-words'})
    country_text = country.get_text().strip()
    text_2 = country_text
    country_list.append(text_2)

    linkedin_url = linkedin_list.append(link)


data = {'Name': name_list,
        'Company': company_list,
        'Title': title_list,
        'Country': country_list,
        'Linkedin': linkedin_url}

df = pd.DataFrame(data)
df.to_csv('Profiles_Data.csv')
driver.quit()
