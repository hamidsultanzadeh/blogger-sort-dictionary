import json

from blogger import Blogger
from goco import Goco

GoogleApi = Goco("files/credentials.json")
MyBlog = GoogleApi.connect(scope='blogger', service_name='blogger', version='v3')


def getPostById(blogger):

    print("GET request sending...")

    response:dict = MyBlog.posts().list(blogId=blogger.blogId).execute()

    print("GET request done")
    return response['items'][0]['content']


def savePostById(bg: Blogger):
    print("PUT Request sending...")

    myJson = """
     "kind": "blogger#post",
     "id": {},
     "blog": {},
     "url": "http://sultanzadehhenglish.blogspot.com/2020/06/dictionary.html",
     "selfLink": "https://www.googleapis.com/blogger/v3/blogs/3429621621024834681/posts/1276803922336852881",
     "title": "Dictionary",
     "content": {}
    """.format("\""+bg.postId+"\"", "{" + """"id": \"{}\"""".format(bg.blogId) + "}",bg.content)

    myJson = "{"+myJson+"}"

    MyBlog.posts().update(blogId=bg.blogId,postId=bg.postId,body=json.loads(myJson)).execute()

    print("PUT Request done")
