from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    def hash_password(password):
        return pwd_context.hash(password)

    def verify_password(password, password_hashed):
        return pwd_context.verify(password, password_hashed)
