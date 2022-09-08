class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value
        else:
            raise ValueError('The username must be between 5 and 15 characters.')

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_lenght_valid = len(value) >= 8
        is_uper_case_presented = [char for char in value if char.isupper()]
        is_number = [char for char in value if char.isdigit()]

        if not is_lenght_valid or not is_uper_case_presented or not is_number:
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)