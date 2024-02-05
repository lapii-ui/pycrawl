import requests
from bs4 import BeautifulSoup

url = "https://coloris-demo.568win.com/api/game-provider/v2/player-login"


from playwright.sync_api import sync_playwright, Playwright
import requests
from bs4 import BeautifulSoup


def run(playwright: Playwright, url):
    with playwright.firefox.launch() as browser:
        page = browser.new_page()
        page.goto(url)
        dump_frame_tree(page.main_frame, "")


def dump_frame_tree(frame, indent):
    print(indent + frame.name + '@' + frame.url)
    print(frame.frame_element())
    soup = BeautifulSoup(frame.content(), 'html.parser')
    # print(soup.prettify())
    # Opening a file for writing
    file_object = open("sportData.txt", "w")
    file_object.write(soup.prettify())
    for child_frame in frame.child_frames:
        print(child_frame)
        if child_frame.name == 'sportsFrame':
            dump_frame_tree(child_frame, indent)

url = "https://coloris-demo.568win.com/api/game-provider/v2/player-login"

payload = {
    "GameId": 7527,
    "Ip": "61.220.125.7",
    "FromUrl": "https://demo-ng.568win.com",
    "IsFromMobile": False,
    "EntranceLocation": "GameLobby",
    "Lang": "en",
    "OnlineId": 325613
}

bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3IjoiMSIsIm4iOiJsYXBpaV9fdG1wX18wMDEiLCJjIjoiNDkyMzQ5IiwiY3UiOiJUTVAiLCJpIjoiNjEuMjIwLjEyNS43IiwiYSI6IjEiLCJwIjoiMiIsImlhIjoiRmFsc2UiLCJpY3AiOiJUcnVlIiwiaXBwZSI6IlRydWUiLCJtcyI6IjIwNTYiLCJwYSI6IjEiLCJuYmYiOjE3MDcxNDY0NTIsImV4cCI6MTcwNzE0ODI1MiwiaXNzIjoiNTY4d2luIiwiYXVkIjoiMV80OTIzNDlfbGFwaWlfX3RtcF9fMDAxIn0.kPw6vHj4js9qbQls0kUrm5452f9TFTAp3mgM3o0jygY"

headers = {
    "Authorization": f"Bearer {bearer_token}"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    print("POST request successful")
    json_data = response.json()
    print("Response:", json_data)
    game_url = json_data["Data"]["Url"]

    with sync_playwright() as playwright:
        run(playwright, game_url)