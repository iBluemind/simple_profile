from config import MYSQL_DATABASE, MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD

class AccessDAO(object):
    def __init__(self, driver, db=None, host=None,
                       user=None, password=None, port=None):
        self.driver = driver
        self._db = db
        self._host = host
        self._user = user
        self._password = password
        self._port = port

    @property
    def db(self):
        if getattr(self, '_db', None) is None:
            self._db = MYSQL_DATABASE
        return self._db

    @property
    def host(self):
        if getattr(self, '_host', None) is None:
            self._host = MYSQL_HOST
        return self._host

    @property
    def port(self):
        if getattr(self, '_port', None) is None:
            self._port = MYSQL_PORT
        return self._port

    @property
    def user(self):
        if getattr(self, '_user', None) is None:
            self._user = MYSQL_USER
        return self._user

    @property
    def password(self):
        if getattr(self, '_password', None) is None:
            self._password = MYSQL_PASSWORD
        return self._password

    @property
    def uri(self):
        return 'mysql+%s://%s:%s@%s:%s/%s?charset=utf8mb4&use_unicode=0' % (
            self.driver, self.user, self.password, self.host, self.port, self.db
        )
