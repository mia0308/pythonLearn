import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.149 '
                  'Safari/537.36 '
}
response = requests.get(url, headers=headers)  # GET请求
print(response)
html = response.text

# 页面解析 re(标准库) BeautifulSoup（第三方库）
soup = BeautifulSoup(html, 'html.parser')
movie_list = soup.find('ol', class_='grid_view')
# print(movie_list)
movies = movie_list.find_all('li')
# print(movies[0])
# names = []
# for movie in movies:
#     name = movie.find('span', class_='title').get_text()
#     names.append(name)
# print(names)
urls = []
for movie in movies:
    url = movie.find('div', class_='hd').find('a')
    urls.append(url.get('href'))
print(urls)
f = open(r'result.txt', 'w')
for url in urls:
    f.write(url + '\n')
f.close()
