# finduser.py

The script will search usernames across 70 social networks. It is nice if you want to determine the usage of the same username on different social networks.

It is a rewrite and clean-up of the finduser utility by https://github.com/xHak9x/finduser

One can easily extend the range of social media sides by appending one with a placeholder for search string ```{user_to_search}``` for the user name onto the social_media_urls.txt file.

I generated this one with the below code:

```bash
grep -oP '(?<=-i).*(?=-H)' finduser.sh | sed -e s/\$\{username\}/\{user_to_search\}/g -e 's/"//g' > social_media_urls.txt
```
