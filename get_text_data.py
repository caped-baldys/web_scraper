import os
import requests
from bs4 import BeautifulSoup


class GetData:
    def article_data(url):

        # dir to store the text file from url
        working_dir = os.getcwd()

        # name of file is url
        # getting rid of https:// and blackcoffer.com
        file_name = (url.split("/"))[-2]

        # This is chrome
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

        # fetching page
        html_page = requests.get(url, headers=headers, allow_redirects=True)

        html_content = html_page.content

        soup = BeautifulSoup(html_content, "html.parser")

        # checking if the directory input
        # exist or not.
        if not os.path.exists("input"):

            # if the input directory is not present
            # then create it.
            sam = os.makedirs("input")

        # creating text file in w mode write mode
        full_file_path = f"{working_dir}\input"

        file = open(f"{full_file_path}\{file_name}.txt",
                    "w+", encoding="utf-8")

        # write web article in file

        for para in soup.find_all('p'):
            file.write(para.get_text()+"\n")
