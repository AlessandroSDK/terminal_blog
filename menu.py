

class Menu(object):
    def __init__(self):
        self.user = input("Enter your author name")
        if self._user_has_command():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()
        # Ask user for author name
        # Check if they've already got an account
        # If not, prompt them to create one

    def _user_has_account(self):
        pass

    def _prompt_user_for_account(self):
        pass

    def run_menu(self):
        # User read or write blogs?
        # if read:
            # list blogs in database
            # allow user pick one
            # displays posts
        # if write
            # check if user has a blog
            # if they do, prompt to write a post
            # if not, prompt to create a post
        pass