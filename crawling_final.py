import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup


base_url = 'https://blog.naver.com/PostView.naver?blogId='
input_url = input('블로그 주소를 입력하세요.\n')
# 한글 검색 자동 변환
id = input_url.split('/')[3] #아이디 추출 
number = input_url.split('/')[4] #게시글번호 추출 
url = base_url+id+'&logNo='+number

html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")

img_list = soup.find_all("img", class_ = 'se-image-resource')

n = 1
for i in img_list:
    imgUrl = i.get("data-lazy-src") #이미지 소스 imgUrl 변수에 저장
    print(imgUrl)
    with urlopen(imgUrl) as f: #이미지 소스 방문
        with open('./img/'+id+'_'+str(n)+'.jpg','wb') as h: #텍스트가 아닌 이미지이므로 wb로 넣어줌
            img = f.read()
            h.write(img)
    n += 1
    print(imgUrl)
print('다운로드 완료')        
