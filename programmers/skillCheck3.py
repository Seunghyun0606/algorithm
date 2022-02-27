'''
검색어 웹페이지 매칭점수 매기기

기본점수 : 텍스트 중 검색어가 등장하는 횟수 (대소문자 무시)
외부링크 수 : 다른 외부 페이지로 연결된 링크 개수
링크점수 : 해당 웹페이지로 연결된 외부 페이지의 ( 기본점수 // 외부링크 수 )
매칭점수 : 기본점수 + 링크점수

매칭점수가 가장높은 페이지의 index
여러개면 가장 index가 작은 페이지

'''

# 하기 문제는 parser로 풀면안된다. meta tag가 없는 경우도 있을 수 있다.
# 따라서 정규표현식으로 풀어야한다

word = 'blind'
word = word.lower()
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]



from html.parser import HTMLParser
from collections import defaultdict

class MyHTMLParser(HTMLParser):
    text = ''
    current_url = ''
    href = ''
    def handle_starttag(self, tag, attrs):

        if tag == 'a' or 'meta':
            for attr in attrs:
                key, value = attr

                # 연결된 page url
                if key == 'href':
                    self.href += value + ' '

                # 현재 page url
                elif key == 'content':
                    self.current_url = value

    def handle_data(self, data):
        self.text += data

# text 구분자를 위한 dict 형성
text_indicator = defaultdict(int)
for i in 'abcdefghijklmnopqrstuvwxyz':
    text_indicator[i] += 1

page_index = defaultdict(int)
# page 별 연결된 주소 
page_urls = [ [0] ]
# page 별 body score
page_body_score = [0] * (len(pages) + 1)


# word check
def check_word(temp_word, word):
    if temp_word == word:
        page_body_score[page_index[parser.current_url]] += 1
        return True
    return False


for idx, page in enumerate(pages):

    parser = MyHTMLParser()
    parser.feed(page)

    # page index
    page_index[parser.current_url] = idx + 1

    # page 별 연결된 주소
    page_urls.append(parser.href.split())
    texts = parser.text.split()

    for text in texts:
        text = text.lower()
        # print(text)
        temp_word = ''
        for t in text:
            if text_indicator[t]:
                temp_word += t

            # 구분자가 나오면 다른 word
            else:
                if check_word(temp_word, word):
                    temp_word = ''
        check_word(temp_word, word)


page_link_score = [0] * (len(pages) + 1)
for idx in range(1, len(page_urls)):
    page_url = page_urls[idx]
    for url in page_url:
        if page_index[url]:
            page_link_score[page_index[url]] += page_body_score[idx] / len(page_urls[idx])
result = [ x+y for x,y in zip(page_body_score, page_link_score)]

least = 0
answer = 0
for i in range(len(result) - 1, 0, -1):
    if least <= result[i]:
        least = result[i]
        answer = i - 1
print(answer)
print(page_body_score)
print(result)
print(page_urls)
