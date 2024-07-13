from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import csv
import os
 
user = "@username"

def linkExistsInCSV(link):
    csvFileName = "videos info/videos_info.csv"
    isFileExists = os.path.isfile(csvFileName)
    if isFileExists:
        with open(csvFileName, "r", newline="", encoding="utf-8") as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                if row[5] == link:
                    return True
    return False

def downloadVideo(link, id):
    print(f"Downloading video {id} from: {link}")

    cookies = {
        '_gid': 'GA1.2.1881320606.1689102811',
        '_gat_UA-3524196-6': '1',
        '__gads': 'ID=ffd1dbca9f1b2fab-22958b1879e200f4:T=1688346370:RT=1689102811:S=ALNI_Mbi1j9Q11uuAilZBcgkpx_ySuEDpg',
        '__gpi': 'UID=00000c906fbd79dc:T=1688346370:RT=1689102811:S=ALNI_Ma8tl2LV2HNIcx8iLD-OYPBA3NkTw',
        '_ga': 'GA1.2.1432804600.1688346371',
        '_ga_ZSF3D6YSLC': 'GS1.1.1689102810.13.1.1689102815.0.0.0',
    }

    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_gid=GA1.2.1881320606.1689102811; _gat_UA-3524196-6=1; __gads=ID=ffd1dbca9f1b2fab-22958b1879e200f4:T=1688346370:RT=1689102811:S=ALNI_Mbi1j9Q11uuAilZBcgkpx_ySuEDpg; __gpi=UID=00000c906fbd79dc:T=1688346370:RT=1689102811:S=ALNI_Ma8tl2LV2HNIcx8iLD-OYPBA3NkTw; _ga=GA1.2.1432804600.1688346371; _ga_ZSF3D6YSLC=GS1.1.1689102810.13.1.1689102815.0.0.0',
        'hx-current-url': 'https://ssstik.io/en',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': 'VEQ1NW02',
    }




    print("STEP 4: Getting the download link")
    print("If this step fails, PLEASE read the steps above")
    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    downloadSoup = BeautifulSoup(response.text, "html.parser")

    response1 = requests.get(link)

    EngagemSoup = BeautifulSoup(response1.content, "html.parser")

    downloadLink = downloadSoup.a["href"]
    videoTitle = f"{user}-{id}"

    print("STEP 5: Saving the video :)")
    mp4File = urlopen(downloadLink)
    # Feel free to change the download directory
    with open(f"videos/{user}-{id}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break
    # Scrape description
    description = downloadSoup.p.getText().strip()
    
    
    # Scrape number of likes
    like_element = EngagemSoup.find("strong", attrs={"data-e2e": "like-count", "class": "tiktok-5g8l3h-StrongText"})
    if like_element:
        likes = like_element.text
    else:
        likes = "N/A"
     
    # Scrape number of comments
    comment_element = EngagemSoup.find("strong", attrs={"data-e2e": "comment-count", "class": "tiktok-5g8l3h-StrongText"})
    if comment_element:
        comments = comment_element.text
    else:
        comments = "N/A"
    # Save video info to CSV
        
    csvFileName = "videos info/videos_info.csv"
    isFileExists = os.path.isfile(csvFileName)
    with open(csvFileName, "a", newline="", encoding="utf-8") as csvFile:
        writer = csv.writer(csvFile)
        if not isFileExists:
            writer.writerow(["User", "Video Title", "Description", "Likes", "Comment", "Links"])  # Add header if the file is newly created
        writer.writerow([user, videoTitle, description, likes, comments, link])
        
print("STEP 1: Open Chrome browser")
driver = webdriver.Chrome()
# Change the tiktok link
driver.get(f"https://www.tiktok.com/{user}")

# IF YOU GET A TIKTOK CAPTCHA, CHANGE THE TIMEOUT HERE
# to 60 seconds, just enough time for you to complete the captcha yourself.
time.sleep(20)

scroll_pause_time = 1
screen_height = driver.execute_script("return window.screen.height;")
i = 1

print("STEP 2: Scrolling page")
while True:
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    if (screen_height) * i > scroll_height:
        break 

soup = BeautifulSoup(driver.page_source, "html.parser")
# this class may change, so make sure to inspect the page and find the correct class
videos = soup.find_all("div", {"class": "tiktok-16ou6xi-DivTagCardDesc"})

print(f"STEP 3: Time to download {len(videos)} videos")
for index, video in enumerate(videos):
    print(f"Downloading video: {index}")
    video_link = video.a["href"]
    if linkExistsInCSV(video_link):
        print(f"Video with link '{video_link}' already exists in the CSV file. Skipping download.")
        continue
    downloadVideo(video_link, index)
    time.sleep(10)
