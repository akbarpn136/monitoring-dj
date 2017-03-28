class IsAuthenticated(object):
    def __init__(self, isAuth):
        super(IsAuthenticated, self).__init__()
        self.isAuth = isAuth

    def check(self):
        if self.isAuth:
            return True
        else:
            return False
