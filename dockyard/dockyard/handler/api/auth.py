from dockyard.handler import BaseHandler
from dockyard.const import APIStatus
from dockyard.utils import encrypt

class ApiAuthHandeler(BaseHandler):
    def post(self, *args, **kwargs):
        self.parse_arg_str("user_email")
        self.parse_arg_str("user_pwd")

        self.user["user_email"] = self.data["user_email"]

        if not self.user:
            return self.error(APIStatus["STAT_API_USER_UNEXIST"])
        if self.user["user_pwd"] != encrypt(self.data["user_pwd"]):
            return self.error(APIStatus["STAT_API_USER_PWD_ERR"])

        self.set_secure_cookie("user", self.user.str_id)
        self.success()