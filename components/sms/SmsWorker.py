from components.core import smsc
from components.managers.UserManager import UserManager

from dto.User import User


class SmsWorker:
    @staticmethod
    def send_sms(user: User, confirm_code: int):
        user.confirm_code = confirm_code
        UserManager.update_user_data(user)
        smsc.send_sms("79773349795", "Ваш пароль: " + str(confirm_code), sender="app")
