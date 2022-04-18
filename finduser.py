#!/usr/bin/python3
import requests

green = "\033[0;32m"
clear = "\033[0m"
user_to_search = input(f"{green}User name to search:{clear}\n> ")

with open("social_media_urls.txt", "r") as links_file:
    links = []
    for i in links_file.readlines():
        links.append(i.replace("\n", ""))


with open(f'{user_to_search}.txt', "w") as f:

    for link in links:
        format_link = f'{link.strip().replace("{user_to_search}", user_to_search)}'
        response = requests.get(format_link)
        if response.status_code == 200:
            print(f"\t{green}Exists\t{format_link}{clear}")
            f.write(f'{format_link}\n' )
        else:
            print(f"Doesn't exist {format_link.replace('https://', '')}")
