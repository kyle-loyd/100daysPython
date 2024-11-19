from bs4 import BeautifulSoup


def get_billboard_song_list(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    element_list = soup.select("li.o-chart-results-list__item h3")
    return [element.getText().replace('\n', '').replace('\t', '') for element in element_list]
