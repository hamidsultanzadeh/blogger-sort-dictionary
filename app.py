import client
import requestutil
import util
from blogger import Blogger
from bs4 import BeautifulSoup


def main():
    fileName = "files/dictionary.txt"

    blogger = Blogger(client.BLOG_ID, client.POST_ID, "")

    html = requestutil.getPostById(blogger)

    content = BeautifulSoup(html, "lxml")
    blogger.content = content.get_text("\n")
    arr = blogger.content.split("\n")

    util.writeToFile(fileName, arr)

    arr = util.sortContent(fileName)

    if not isinstance(arr, list):
        print("\n******NO CONTENT******\n\n")
        return

    print("\n******Content*****\n\n", blogger.content, sep="",end="\n\n")

    blogger.content = util.formatter(arr)

    requestutil.savePostById(blogger)


if __name__ == '__main__':
    main()
