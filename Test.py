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
email_id = 'email'
find_email_element = driver.find_element_by_xpath(email_xpath)
find_email_element.send_keys(email_id)

time.sleep(3)

password_xpath = """//*[@id="password"]"""
password = 'pass'
find_pass_element = driver.find_element_by_xpath(password_xpath)
find_pass_element.send_keys(password)
find_pass_element.send_keys(Keys.ENTER)

urls_list = ['https://www.linkedin.com/in/supunsetunga?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=769946d8-aacc-4a6f-9048-ea52757776bb&external_page_instance=117ed2ae-b3a1-4980-8009-52dddd7628dc', 'https://www.linkedin.com/in/pliskin-alexander/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=769946d8-aacc-4a6f-9048-ea52757776bb&external_page_instance=2464f34d-3835-4a46-bd64-7ecebffcda2d', 'https://www.linkedin.com/in/micaelferreira/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=47f842e4-6750-49c4-beb6-dfb1ba788774', 'https://www.linkedin.com/in/c-monahan/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=e71dc6e5-7689-4c50-8c16-fc57eea52be4', 'https://www.linkedin.com/in/pramit-marattha/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=4feca21a-a5ef-4b6b-b2b3-e1b8f400dbe7', 'https://www.linkedin.com/in/stevecook/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=f42fd9c4-9791-43db-a97e-900432a59291', 'https://www.linkedin.com/in/samuel-fatoki-51607b167/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=02076da5-c2db-4e8d-9ec9-f4bc7bb19f77', 'https://www.linkedin.com/in/%e5%87%8c%e7%be%bd-%e8%83%a1-0790a7149/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=db148463-02d2-4322-b650-729dec934874', 'https://www.linkedin.com/in/isnihal/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=e54445a9-bdcd-4a71-b335-05effbada8c7', 'https://www.linkedin.com/in/amritanshtripathi/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=88cd66c0-a4a8-446e-a564-46ec836cd36c', 'https://www.linkedin.com/in/jeremy-lewi-600aaa8/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=7c4ef961-ea79-45e9-a4b3-059d26d744a0', 'https://www.linkedin.com/in/qiyi-shan-6583b6152/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=802f34df-2adf-407a-a2ad-f7f7acc1fbeb', 'https://www.linkedin.com/in/ishneet-kaur-b8a846140/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=7ca66f05-5ea0-4e02-aff0-b21daba47ca5', 'https://www.linkedin.com/in/myrzamadi-temirkhan-8a761b178/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=72781716-6f8a-4eea-93af-3de745ee1dfd', 'https://www.linkedin.com/in/kediaabhishek10/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=394780bf-c98c-4335-85b6-e7dd6e4b03fc', 'https://www.linkedin.com/in/gligorijevic/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=026518e4-25e5-43bd-8a70-0bd6040b3ebc', 'https://www.linkedin.com/in/miloulisvelisarios/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=46e21779-9379-4d6f-963d-ef57a953022e', 'https://www.linkedin.com/in/sumeet-kumar-92035891/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=50a04df8-3ffc-4120-8d5d-9e440a5ef85c', 'https://www.linkedin.com/in/haythemkh/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=b5d2a213-a55a-43cc-bc76-021ebc21b040', 'https://www.linkedin.com/in/%ec%84%b1%ec%9c%a4-hunt-%ec%a1%b0-22b5b5155?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=833a62e9-4227-4d9d-95b8-d7bec3e9add4', 'https://www.linkedin.com/in/yunhui/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=9c956dc6-9b71-4160-a01c-b06b22ddd858', 'https://www.linkedin.com/in/anirudhmukundanraghavan/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=c6c962f0-36ba-42b8-a2a3-f5dba85e3b16', 'https://www.linkedin.com/in/revati-singh-a78bb9126/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=29788d0a-f366-469b-8fcd-7f4c87c47c7c', 'https://www.linkedin.com/in/imamarismunandar/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=6c7ff62a-730b-4825-ad1b-e89786cb9aa9', 'https://www.linkedin.com/in/ibrahim-shaikh-12b84a119/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=db9d8fae-601d-49f1-8b82-38d84430bfdd', 'https://www.linkedin.com/in/mahmoud-sultan/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=90f6c785-1b5b-4e1d-8c01-213a3bc13266', 'https://www.linkedin.com/in/sakilansari?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=e5c5d1fd-6e00-47f7-bb71-ad098bd70510', 'https://www.linkedin.com/in/someshkrbhaskar/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=3c95194d-37b4-440c-853b-7888f60ca17d', 'https://www.linkedin.com/in/karmakarabhishek/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=7276910e-473e-48c5-9c95-39624005f01e', 'https://www.linkedin.com/in/borja-rodriguez/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=15911883-8bfd-4039-9a4b-5496f7d3b4f8', 'https://www.linkedin.com/in/sanzhar-aubakirov-a0470a65/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=88590880-fdd0-45b3-8e28-baf5c564c16c', 'https://www.linkedin.com/in/yashkhem/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=b3ca5b88-f256-410a-a6f1-468bf74a2d2c', 'https://www.linkedin.com/in/neeraj-kesavan-41aa59128/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=50d846ec-5e16-4973-8026-5a44ef41212e', 'https://www.linkedin.com/in/tsitsimis?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=422ad9ed-e5ad-4eeb-914e-e42a34755136', 'https://www.linkedin.com/in/singalhimanshu?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=8b879a0f-9675-4dc0-b935-f85e66cbc641', 'https://www.linkedin.com/in/mohitwildbeast?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=cf2bb788-3408-40c1-b9ba-37661b701467', 'https://www.linkedin.com/in/mohamedelghamry/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=8876129b-3f4b-43ea-8587-60428e8f37a9', 'https://www.linkedin.com/in/nikita-malviya-874219142/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=18ebcf35-f46e-4ce6-91ea-752a79daceaa', 'https://www.linkedin.com/in/singhalshantanu/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=5d5ddec5-528b-44ea-960a-181298c1e69f', 'https://www.linkedin.com/in/mohdfarhanakram/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=ccaca322-82f7-49ca-a4dc-d81cc76e2a83', 'https://www.linkedin.com/in/tom-lee-8494b534?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=9c68528d-bd5f-44d7-adda-2f64f4d41441', 'https://www.linkedin.com/in/%e5%9b%9b%e5%b9%b3-%e5%88%98-33b888175/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=bc1bfdb6-0cd6-435f-a47e-0af5df3b7880', 'https://www.linkedin.com/in/prateek-sawhney-a0b134131?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=9c3d9097-a6c3-4338-a9a4-ed7ae672d790', 'https://www.linkedin.com/in/alancampos/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=d8fca2b9-1790-4f32-915a-c85c8467e2f7', 'https://www.linkedin.com/in/daveho3/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=f7b1e8fd-2ca3-4683-a717-3c8afc355503', 'https://www.linkedin.com/in/claudio-cusano-39774b4a/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=1bc1e400-825a-4680-b542-fc9bce330ebb', 'https://www.linkedin.com/in/vasileios-charatsidis-390169131/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=62715c9b-b262-40bc-b796-12b9b947d174', 'https://www.linkedin.com/in/ghollahkioko/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=48ec2944-9855-4dfd-bf4a-66a9950bfede', 'https://www.linkedin.com/in/eloukas/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=307a4956-a285-4617-896b-1754c0284eb2', 'https://www.linkedin.com/in/ignacio-van-loy-estero-074997161/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=ef547434-68df-44f2-87f1-f4e2d1230e8f', 'https://www.linkedin.com/in/anders-christiansen-s%c3%b8rby/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=83624d74-0360-4f31-afd9-972d0ebe87aa', 'https://www.linkedin.com/in/murali-kurapati-ba2604196?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=6079a411-012e-447d-873c-261227621e40', 'https://www.linkedin.com/in/kramo/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=7de6a601-b8fb-42bd-8c75-22e493aa0900', 'https://www.linkedin.com/in/sandro-luck-b9293a181/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=be0e576c-d5fa-46ac-95e7-75d4d189970c', 'https://www.linkedin.com/in/jinil-chencheril-sasidharan-06295223?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=3ef2d2b6-b315-4437-a132-8d6104a2af70&external_page_instance=78243cd8-2849-46e4-9ffd-e3918df31c01']
print("No of profiles:",len(urls_list))

# urls = open('Url_list.txt', 'r')
# content = urls.read()
# urls_list.append(content)
# urls.close()

name_list = []
title_list = []
company_list = []
country_list = []
linkedin_list = []

start = time.time()
print("start mining")

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
        erroe = "--"
        title_list.append(erroe)

    try:
        company = html_soup.find('h2', {'class': 'text-heading-small align-self-center flex-1'})
        company_text = company.get_text().strip()
        text_3 = company_text
        company_list.append(text_3)

    except:
        error = '--'
        company_list.append(error)

    country = html_soup.find('span', {'class': 'text-body-small inline t-black--light break-words'})
    country_text = country.get_text().strip()
    text_2 = country_text
    country_list.append(text_2)


    linkedin_list.append(driver.get(link))


total_time = str((time.time() - start))
print(f"Linkedin Extraction Procee took Time Is: {total_time} in seconds")

data = {'Name': name_list,
        'Company': company_list,
        'Title': title_list,
        'Country': country_list,
        'Linkedin': linkedin_list}

df = pd.DataFrame(data)
df.to_csv('Profiles_Data.csv')
driver.quit()


