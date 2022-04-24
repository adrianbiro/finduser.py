#!/usr/bin/python3
import requests
import threading
import concurrent.futures


green = "\033[0;32m"
clear = "\033[0m"
user_to_search = input(f"{green}User name to search:{clear}\n> ")



def get_links():
    with open("social_media_urls.txt", "r") as links_file:
        links = []
        for i in links_file.readlines():
            links.append(i.replace("\n", "").strip().replace("{user_to_search}", user_to_search))
        return links

def do_request_2():
    response = requests.get(url)
    if response.status_code == 200:
        print(f"\t{green}Exists\t{format_link}{clear}")
    else:
        print(f"Doesn't exist {format_link.replace('https://', '')}")

def do_request():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(do_request_2, linsk)


#    with open(f'{user_to_search}.txt', "w") as f:
#        response = requests.get(url)
#        if response.status_code == 200:
#            print(f"\t{green}Exists\t{format_link}{clear}")
#            f.write(f'{format_link}\n' )
#        else:
#            print(f"Doesn't exist {format_link.replace('https://', '')}")


links = get_links()

threads = [threading.Thread(target=do_request, args=(url)) for url in links]

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()





