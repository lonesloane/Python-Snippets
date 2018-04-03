class Blog:

    def read(self):
        print('Read the blog')

    def write(self):
        print('Write the blog')


class Proxy:

    def __init__(self, target):
        self.target = target

    def __getattr__(self, item):
        return getattr(self.target, item)


class AnonUserBlogProxy(Proxy):

    def __init__(self, blog):
        super().__init__(blog)

    def write(self):
        print('Only authorized users can write blog posts')


# === usage ===

blog = Blog()
blog.write()

proxy = AnonUserBlogProxy(blog)
proxy.write()
