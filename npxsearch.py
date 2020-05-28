class NpxSearch:

    def __init__(self, name_search):
        self.name = name_search

    def nsearch(self):
        try:
            from googlesearch import search
        except ImportError:
            print("No Module named 'google' Found")
        res = []
        for i in search(query=self.name, tld='co.in', lang='en', num=10, stop=5, pause=5):
            res.append(i)
        return res


