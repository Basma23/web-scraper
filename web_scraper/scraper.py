import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

def get_citations_needed_count(URL):
    '''
    get_citations_needed takes in a url and returns an integer
    '''
    # URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    citation_needed = soup.find_all('a', href="/wiki/Wikipedia:Citation_needed")
    print(len(citation_needed))
    return len(citation_needed)

def get_citations_needed_report(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results =soup.find_all('a', href="/wiki/Wikipedia:Citation_needed")
    content = []
    for i in range (len(results)):
        citation_needed = i + 1
        print(f'citations number{citation_needed}')
        print('-'*100)
        print(results[i].parent.parent.parent.getText())
        content.append(results[i].parent.parent.parent.getText().strip())
        return content




if __name__ == "__main__":
    get_citations_needed_count(URL)
    get_citations_needed_report(URL)