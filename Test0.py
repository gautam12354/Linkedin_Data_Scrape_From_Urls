'''CTRl+B TO Run'''

'''
If your syntax is correct, but the script has unexpected behavior or output, this may be due to a semantic problem. 
Remember that syntax is the rules of how code is constructed, while semantics are the overall effect the code has. 
It is possible to have syntactically correct code that runs successfully, but doesn't do what we want it to do.
'''


# LAB: https://labs.cognitiveclass.ai/tools/jupyterlab/lab/tree/labs/PY0101EN/PY0101EN-1-1-Types.ipynb?lti=true
# Py4E

# https://towardsdatascience.com/training-machine-learning-models-online-for-free-gpu-tpu-enabled-5def6a5c1ce3
# https://ddf46429.springboard.com/uploads/resources/1550788813_Ebook__A_Beginner_s_Guide_to_Getting_Your_First_Data_Science_Job.pdf
# https://data-flair.training/blogs/data-science-tools/
# https://pythonprogramming.net/introduction-deep-learning-python-tensorflow-keras/
# https://towardsdatascience.com/top-10-python-libraries-for-data-science-cd82294ec266
# https://www.hackerearth.com/blog/developers/8-different-job-roles-data-science-big-data-industry
# https://www.mathsisfun.com/data/standard-deviation-formulas.html

# Anafortan
# EP40E

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
email_id = ''
find_email_element = driver.find_element_by_xpath(email_xpath)
find_email_element.send_keys(email_id)

time.sleep(3)

password_xpath = """//*[@id="password"]"""
password = ''
find_pass_element = driver.find_element_by_xpath(password_xpath)
find_pass_element.send_keys(password)
find_pass_element.send_keys(Keys.ENTER)

urls_list = ['https://www.linkedin.com/in/sentimentron?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=d7bc5303-f8bb-432e-8eff-921cec030b0e', 'https://www.linkedin.com/in/hongtao-lin/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=3af21f5c-62f6-4351-bcd7-85fad853b86d', 'https://www.linkedin.com/in/%e4%bd%b3%e8%be%89-%e8%80%bf-730961100/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=f1b0d0be-b720-4021-9978-cff5134eed8f', 'https://www.linkedin.com/in/%e6%9c%9d%e9%be%99-%e9%82%a2-b05139156?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=5532cdbc-d8e1-47a1-ab83-99410cdb7271', 'https://www.linkedin.com/in/saeednajafi?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=ef83a12a-4f08-49f9-993c-174f1ab5899a', 'https://www.linkedin.com/in/han-zhang-65a4857b?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=443dbd65-0084-4041-a8a3-410e35374e12', 'https://www.linkedin.com/in/jgontrum?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=b7640a26-cc51-403f-bd55-2200bf9200be', 'https://www.linkedin.com/in/%e6%b0%b8%e4%b8%9a-%e9%bb%84-85032b13a?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=15d95010-b142-4725-9f3c-a138c3b2fe83', 'https://www.linkedin.com/in/kylelo?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=b07213cf-11df-458e-b32d-ba0ce2d80cb1', 'https://www.linkedin.com/in/weidi-xu?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=c973749a-79d5-4391-928d-85a78f5c305b', 'https://www.linkedin.com/in/nikhilsingh291?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=dafcb00a-f549-4065-9e89-edbb63e32195', 'https://www.linkedin.com/in/keisuke-fukuta-b92619126?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=6e41bd48-308b-48bb-b2e2-324290e4a8a3', 'https://www.linkedin.com/in/jiashupu?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=116be9af-5125-43ad-872c-f466b38d4c0b', 'https://www.linkedin.com/in/yyaghoobzadeh?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=b969b8f3-02d8-4421-86f0-0168b6b3eee6', 'https://www.linkedin.com/in/misrarishabh/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=39a084d9-3d6c-453f-8376-2fc72c19c089', 'https://www.linkedin.com/in/%e6%b3%bd%e8%af%9a-%e8%a9%b9-746813166?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=29ce5f50-b53e-4d97-9751-d73ce668a30d', 'https://www.linkedin.com/in/qiji-zhou-7452159a?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=4a7c2dac-20f2-45af-92cc-d3a3905763de', 'https://www.linkedin.com/in/%e5%90%95%e5%95%b8%e5%a8%81-%e5%be%90-341389145?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=fa47d607-fa03-4b00-abe9-873f59aac0c6', 'https://www.linkedin.com/in/xin-rong-a5b4ba2b/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=eccf67d1-1a0e-4ffb-917e-78e9c618ab22', 'https://www.linkedin.com/in/angela-li-b8b78b36?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=0db8396b-0418-47af-b101-4181e7ca0a87', 'https://www.linkedin.com/in/fei-liu-unimelb?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=b0dcd9cc-09e0-4977-872a-ef3c68253627', 'https://www.linkedin.com/in/chandanu?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=46b76b80-58d3-4c91-aa5a-e48675cb3bb0', 'https://www.linkedin.com/in/krzysztofsopyla?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=5f23aa4a-c186-40d3-a53b-c18e5e087123', 'https://www.linkedin.com/in/erickrf?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=1d4bbe9c-9367-4fd4-bb8c-39c909d4e90b', 'https://www.linkedin.com/in/ted-zhao?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=8d7ea3ad-3993-4116-9b4f-b560180be432', 'https://www.linkedin.com/in/octavia-maria-%c8%99ulea-phd-a6058327/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=3e020e32-1d40-42fb-a78c-15182f4c95ee', 'https://www.linkedin.com/in/linbojin?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=9573ea32-ea66-486a-aa07-5361ae3cd6bb', 'https://www.linkedin.com/in/jiajia-ding?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=53d65a62-853c-4846-a872-dc210a659561', 'https://www.linkedin.com/in/samarhaider?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=3a0b38f7-a8c6-482c-92fd-4746628af0c3', 'https://www.linkedin.com/in/bin-liu-1180a52a?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=91af9b54-d245-4c48-8165-7a92786e59a7', 'https://www.linkedin.com/in/nitinmlvya?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=162f9e6c-0e46-4d7a-b5bf-bde757775096', 'https://www.linkedin.com/in/jacksonwoo?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=9577d8fc-565a-4657-a98a-ad5d0dc15294', 'https://www.linkedin.com/in/wuweilan?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=6ecdd54d-ec10-4140-ae75-f70ddb3d7b90', 'https://www.linkedin.com/in/paul-opitz?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=77fbb7f6-ea30-4472-a4a7-efd60cc7c5af', 'https://www.linkedin.com/in/%e6%b8%85%e6%b0%91-%e5%88%98-5a3148174?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=50f8d515-0da7-47d8-83db-3981951e5dcf', 'https://www.linkedin.com/in/mhagiwara?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=6bd4bfb1-da95-4749-83be-faf137afd063', 'https://www.linkedin.com/in/yuanzhigang10?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=830c3196-20ec-476f-8ca7-6d6be84654b1', 'https://www.linkedin.com/in/arka-sadhu-71991aa4?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=dd977139-89ae-45c3-ba4d-878d7ce3859a', 'https://www.linkedin.com/in/yeshuangzhu?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=b0bd58a8-8cd1-4858-8ad4-61599f2a7507', 'https://www.linkedin.com/in/%e6%99%a8%e6%99%a8-%e4%ba%8e-510401107?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=7063833c-2cb9-43ed-ae36-8a51b7a0bd1b', 'https://www.linkedin.com/in/vikrant-goyal-503666124?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=1ac47ac3-70c0-437c-9844-93aa7a035260', 'https://www.linkedin.com/in/jon-gauthier-33616229?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=730f427a-601a-49da-b72a-bf438ab705f0', 'https://www.linkedin.com/in/dongqing-yang-1b74982a?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=d58f518a-4051-499b-941f-9b06a9e0be69', 'https://www.linkedin.com/in/noah-yoshida?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=b9d1acee-e08f-4dad-94ea-de4ef2c110bc', 'https://www.linkedin.com/in/arifulhaqueuc?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=28e8a447-fb5e-4204-8abe-64e91f5e0d91', 'https://www.linkedin.com/in/camilothorne?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=84463322-6031-43ac-97b7-7fe30ca997d7', 'https://www.linkedin.com/in/%e6%98%8e-%e9%99%88-931782167?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=9241bce6-9d68-424e-9c9d-40fceb6e69b9', 'https://www.linkedin.com/in/wang-yuan-4440265a?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=f44c5b9e-eb0c-4605-acc4-d21801b7a25b', 'https://www.linkedin.com/in/%d0%b0%d0%bd%d1%82%d0%be%d0%bd-%d0%b5%d0%bc%d0%b5%d0%bb%d1%8c%d1%8f%d0%bd%d0%be%d0%b2-9307b17a?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=ebc308d5-97df-4ef5-85c0-938420a0b69c', 'https://www.linkedin.com/in/ammar-asmro/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=42504a97-c56c-4489-b40c-16bb70744540', 'https://www.linkedin.com/in/kevin-stowe-3a823628?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=e11b7145-851c-439c-a729-316434957d8a', 'https://www.linkedin.com/in/nicoladecao?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=99441010-2b27-46ac-9f4f-39fd12d4841f', 'https://www.linkedin.com/in/minghan-li-146389121?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=9d18600e-1330-49f8-80b4-2e81a7e88b85', 'https://www.linkedin.com/in/pyungin-paek-067a11141?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=f88f9864-8360-4e68-bdea-067fea798cb0', 'https://www.linkedin.com/in/violetyao?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=803c3b63-23f3-485b-bdec-1ef643d70fae', 'https://www.linkedin.com/in/mahome-yan-30342a90/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=04f839b4-4452-40e6-a713-29fc5efda7c7', 'https://www.linkedin.com/in/elmarzouki/?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=61d89d6b-5e10-4905-9f62-745175e762e2', 'https://www.linkedin.com/in/jrc1995?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=59f5a21c-5a66-41ea-a2e6-fbada20a28db', 'https://www.linkedin.com/in/suraj-rajan-4699b183?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=c9e62925-3b87-42bd-b577-81ca40e508d3', 'https://www.linkedin.com/in/nguyentramanh?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=16eae1a0-b27d-4312-9601-f5bafcdbf5a1', 'https://www.linkedin.com/in/chanran-kim?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=9000067e-1989-4a86-b217-4d277cf30dea', 'https://www.linkedin.com/in/aman304gupta?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=4532c2e1-45eb-41b8-be3b-9b96af5098c5', 'https://www.linkedin.com/in/kang-min-yoo-8a13b0179?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=782691c4-4138-4011-aa4c-0f4a902299c8&external_page_instance=7089fb64-6993-4cf3-9f29-07d2aa13c158']
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
        company = html_soup.find('h2', {'class': 'text-heading-small align-self-center flex-1 break-words'})
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
