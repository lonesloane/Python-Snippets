class ISubject:
    """
    Define the common interface for RealSubject and Proxy so that
    a Proxy can be used anywhere a RealSubject is expected
    """
    def request(self): pass


class RealSubject(ISubject):

    def __init__(self):
        pass

    def request(self):
        print('RealSubject dealing with the request')


class Proxy(ISubject):
    """
    Maintain a reference that lets the proxy access the real subject.
    Expose an interface indentical to that of the RealSubject
    """

    def __init__(self, real_subject: RealSubject):
        self.real_subject = real_subject

    def request(self):
        print('Proxy doing something before passing on to the RealSubject')
        self.real_subject.request()


# === usage ===

rs = RealSubject()
proxy = Proxy(rs)

proxy.request()
