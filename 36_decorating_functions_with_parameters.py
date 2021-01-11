import functools

user = {"username": "jose", "access_level": "admin"}

def make_secure(func): # Decorator function
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            print(f"No admin permissions for {user['username']}")

    return secure_function

@make_secure
def get_admin_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"

print(get_admin_password("admin"))
print(get_admin_password("billing"))