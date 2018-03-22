import bs4
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_info(name):
    base_url = 'http://www.krak.dk'
    browser = webdriver.Firefox()
    browser.get(base_url)
    browser.implicitly_wait(3)

    search_field = browser.find_element_by_id('e-what-all')
    search_field.send_keys(name)
    search_field.submit()

    sleep(3)
    # browser.implicitly_wait(3)

    link_to_persons = browser.find_elements_by_link_text('Personer')
    link_to_persons[0].click()

    sleep(3)

    page_source = browser.page_source

    soup = bs4.BeautifulSoup(page_source, 'html5lib')
    event_cells = soup.find_all('div', {'class': 'hit-header-block-center'})

    entries_str = []
    for e in event_cells:
        lines = e.text.splitlines()
        lines = [l for l in lines if l]

        entry_str = '\n'.join(lines[:-3])
        entries_str.append(entry_str)

    return entries_str


def save_to_file(content, out_path='./addresses.txt'):
    with open(out_path, 'w') as f:
        f.write(content)



entries = get_info('Møller')
save_to_file('\n\n'.join(entries))
