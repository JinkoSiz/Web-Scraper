from bs4 import BeautifulSoup
import requests
import pprint

hn = []


def create_custom_hn(links, votes):
    for idx, item in enumerate(links):
        title = links[idx].get_text()
        a_tags = links[idx].find_all('a')
        for tag in a_tags:
            href = tag['href']
            break
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].get_text().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})


if __name__ == '__main__':
    for page in range(1, 11):
        res = requests.get(f'https://news.ycombinator.com/news?p={page}')
        soup = BeautifulSoup(res.text, 'html.parser')

        links = soup.select('.titleline')
        subtext = soup.select('.subtext')

        create_custom_hn(links, subtext)

    pprint.pprint(sorted(hn, key=lambda k: k['votes'], reverse=True))
