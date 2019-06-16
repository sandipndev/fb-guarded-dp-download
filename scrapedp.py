from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import re

# Input the Facebook Profile URL
url = input("Enter the profile link: ")

# Reading and parsing the HTML
html = urlopen(url).read().decode()
entity_id = re.findall( "entity_id[^0-9]+([0-9]+)" , html)[0]
soup = BeautifulSoup(html, 'html.parser')

user_name = soup.select_one("span#fb-timeline-cover-name").text

# Using Graph API
link_to_profile_pic = f"https://graph.facebook.com/{entity_id}/picture?width=10000"

print(f"The profile picture for {user_name} is at {link_to_profile_pic}")

ans = input("Do you want to save the Profile Picture(Y/N)? ")

if ans == "Y" or ans == "y":
    # Saving the image
    urlretrieve(f"{link_to_profile_pic}", f"dp-{entity_id}.jpg")
    print(f"{user_name}'s profile picture saved as dp-{entity_id}.jpg")