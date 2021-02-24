import requests
from bs4 import BeautifulSoup
from contextlib import closing
import tqdm


winsdk_url = 'https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/'

winsdk_resp = requests.get(winsdk_url)
raw_url = []
soup = BeautifulSoup(winsdk_resp.text,'lxml')
for tag in soup.find_all("a", class_="c-call-to-action c-glyph f-secondary"):
    raw_url.append(tag.get('href'))
r = requests.get('https:'+raw_url[0])
dst64_url = r.url.replace('winsdksetup.exe', 'Installers/X64%20Debuggers%20And%20Tools-x64_en-us.msi')
dst32_url = r.url.replace('winsdksetup.exe', 'Installers/X86%20Debuggers%20And%20Tools-x86_en-us.msi')

with closing(requests.get(dst32_url, stream=True)) as response:
    chunk__size = 1024
    content_size = response.headers['content-length']
    with open('./X86 Debuggers And Tools-x86_en-us.msi', 'wb') as file:
        for data in tqdm.tqdm(response.iter_content(chunk_size=chunk__size),desc='Downloading',ascii=" .oO0",unit='kb'):
            file.write(data)

with closing(requests.get(dst64_url, stream=True)) as response:
    chunk__size = 1024
    content_size = response.headers['content-length']
    with open('./X64 Debuggers And Tools-x64_en-us.msi', 'wb') as file:
        for data in tqdm.tqdm(response.iter_content(chunk_size=chunk__size),desc='Downloading',ascii=" .oO0",unit='kb'):
            file.write(data)
