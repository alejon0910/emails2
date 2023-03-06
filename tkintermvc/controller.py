from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import EmailAddress
from tkinterr_mvc import View


class Controller:
    def __init__(self, model, view):
        self.engine = create_engine('sqlite:///emails.sqlite', echo=True)
        self.model = model
        self.view = view

    def save(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:
            with Session(self.engine) as sess:
                email_address = EmailAddress(email=email)
                sess.add(email_address)
                sess.commit()

                self.view.show_success(f'The email {email} saved!')

                return "saved"


        except ValueError as error:
            # show an error message
            raise ValueError(error)
