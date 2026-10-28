def login(username, password):
    if username == "admin" and password == "123456":
        return "Dang nhap thanh cong"
    return "Dang nhap that bai"


print(login("admin", "123456"))