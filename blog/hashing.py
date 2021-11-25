from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    def bcrypt(password: str):
        return pwd_context.hash(password)

    def verify_password(hashed_password, plain_password):
        # print(f'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ{hashed_password}, {plain_password}')
        return pwd_context.verify(plain_password, hashed_password)
