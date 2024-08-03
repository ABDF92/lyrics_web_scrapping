import requests as r
import pprint
from bs4 import BeautifulSoup as bs
import re

def get_song_name():
    song = input("Enter Song Name" + "\n")
    return song.replace(" ", "+")

def get_soup(url):
    try:
        req = r.get(url)
        req.raise_for_status()
        return bs(req.content, 'html.parser')
    except r.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def extract_song_links(soup):
    member = soup.find_all(class_="entity_full_member_box")
    elements_with_name = soup.find_all(attrs={"name": True})
    
    link = "https://www.megalobiz.com"
    data_dict = {}

    for box in member:
        href = link + box.find('a')['href']
        info_div = box.find(class_="entity_name")
        string_data = info_div.get_text(strip=True)

        for element in elements_with_name:
            name_attr = element.get("name")
            element_content = element.get_text(strip=True)
        data_dict.update({string_data: href})
    
    return list(data_dict.items())

def get_user_choice(list_data):
    for index, (key, _) in enumerate(list_data):
        print(f"{index + 1}: {key}")
    
    while True:
        try:
            user_choice = int(input("Choose the link you want or enter S to show the lyrics")) - 1
            if 0 <= user_choice < len(list_data):
                return list_data[user_choice]
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the song choice.")

def extract_lyrics(soup, new_data):
    member_1 = soup.find_all(id=new_data)

    for lrc in member_1:
        lrc = str(lrc)
        lrc = lrc.replace("<br/>", "")

    ptrn = r".*\[00"
    lrcc = re.search(ptrn, lrc)
    if lrcc:
        st_index = lrcc.start()
        en_index = lrc.rfind('</span')
        return lrc[st_index:en_index]
    return None

def save_lyrics(song, lyrics):
    song = song.replace("+", " ").title()
    with open(f"{song}.lrc", 'w', encoding='utf-8') as file:
        file.write(lyrics)

def main():
    song = get_song_name()
    url = f"https://www.megalobiz.com/search/all?qry={song}&searchButton.x=0&searchButton.y=0"
    soup = get_soup(url)
    
    if soup:
        list_data = extract_song_links(soup)
        s_key, s_value = get_user_choice(list_data)

        url_new = s_value
        match = re.search(r'\d+$', url_new)
        if match:
            last_digits = match.group()
            new_data = f"lrc_{last_digits}_lyrics"

            soup = get_soup(url_new)
            if soup:
                final_lrc = extract_lyrics(soup, new_data)
                if final_lrc:
                    save_lyrics(song, final_lrc)
                    print(final_lrc)
                else:
                    print("Lyrics not found.")
            else:
                print("Failed to fetch the song page.")
        else:
            print("Invalid song URL format.")
    else:
        print("Failed to fetch the search results page.")

if __name__ == "__main__":
    main()
