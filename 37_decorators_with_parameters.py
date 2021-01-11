import functools

# use ints with > for access_level, so admins can do user stuff

user = {"username": "jose", "access_level": "guest"}

def make_secure(access_level): # decorator factory
    def decorator(func): # Decorator function
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                print(f"No {access_level} permissions for {user['username']}")

        return secure_function
    return decorator

@make_secure("admin")
def get_admin_password():
    return "admin: 1234"

@make_secure("user")
def get_dashboard_password():
    return "user: user_password"

print(get_admin_password())
print(get_dashboard_password())

user = {"username": "maan", "access_level": "admin"}

print(get_admin_password())
print(get_dashboard_password())