from server.models import add_user
from utils.password import get_new_password, check_strong_password
from utils.users import get_new_user_name
import utils.color as uclr

# Работа с цветом
print(uclr.hex_to_rgb("#432123"))


# Работа с пользователями
print("Add user in system")

for i in range(15):
    login = get_new_user_name()
    pswd = get_new_password()

    if check_strong_password(pswd):
        add_user(login, pswd)


