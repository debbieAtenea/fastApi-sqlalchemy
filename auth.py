from typing import Optional
from connect import session
from models import usersFast


class AuthByToken:
    """ Authorise a connection and making changes with a token given. """
    def auth_by_token(token: str) -> Optional[bool]:
        users = session.query(usersFast).filter(usersFast.token == token).all()
        for user in users:
            if token in user.token:
                return True


if __name__ == '__main__':
    AuthByToken()