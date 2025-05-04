from sqlalchemy import create_engine, text


class Users:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_users(self):
        with self.db.connect() as conn:
            result = conn.execute(text("SELECT * FROM users"))
            return result.fetchall()

    def add_user(self, user_email, subject_id):
        with self.db.connect() as conn:
            conn.execute(
                text(
                    "INSERT INTO users (user_email, subject_id) VALUES (:email, :subject_id)"),  # noqa
                {"email": user_email, "subject_id": subject_id}
            )
            conn.commit()

    def update_user_subject(self, user_email, new_subject_id):
        with self.db.connect() as conn:
            result = conn.execute(
                text(
                    "UPDATE users SET subject_id = :subject_id WHERE user_email = :email"),  # noqa
                {"subject_id": new_subject_id, "email": user_email}
            )
            conn.commit()
            return result.rowcount

    def delete_user(self, user_email):
        with self.db.connect() as conn:
            result = conn.execute(
                text("DELETE FROM users WHERE user_email = :email"),
                {"email": user_email}
            )
            conn.commit()
            return result.rowcount
