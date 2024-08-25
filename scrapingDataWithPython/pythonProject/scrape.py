import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news?p=1')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

# print(res.text)
soup_res = BeautifulSoup(res.text, 'html.parser')
soup_res2 = BeautifulSoup(res2.text, 'html.parser')
# print(soup_res.a)
# print(soup_res.find('a'))  # find the first a tag same result with up line
# print(soup_res.find('div'))
# print(soup_res.find(id="score_41342637"))
# print(soup_res.select(".score"))  # select the class of score
# print(soup_res.select(".titleline")[0].a)
# print(soup_res.select(".score")[0])

links = soup_res.select(".titleline")
votes = soup_res.select(".subtext")
links2 = soup_res2.select(".titleline")
votes2 = soup_res2.select(".subtext")

mega_link = links2 + links
mega_vote = votes2 + votes


# print(links[0].a)
# print(votes[0].get("id"))
def sort_func(hn):
    return sorted(hn, key=lambda k: k["vote"], reverse=True)


def create_custom_hn(link, vote):
    hn = []
    for inx, item in enumerate(link):
        title = link[inx].getText()
        href = link[inx].a.get("href", None)
        my_vote = vote[inx].select(".score")
        if len(my_vote):
            point = int(my_vote[0].getText().replace(" points", ""))
            if point > 99:
                hn.append({"title": title, "link": href, "vote": point})

    return sort_func(hn)


pprint.pprint(create_custom_hn(mega_link, mega_vote))
