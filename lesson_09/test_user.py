import pytest
from sqlalchemy import text
from ClassUsers import Users


@pytest.fixture(scope="module")
def users_db():
    return Users("postgresql://postgres:123@localhost:5432/QA")

# Вывод таблицы users


def test_get_users(users_db):
    users = users_db.get_users()
    assert isinstance(users, list)
    if users:
        first_row = users[0]
        assert 'user_id' in first_row._mapping
        assert 'user_email' in first_row._mapping
        assert 'subject_id' in first_row._mapping

# Очистка тестового пользователя


@pytest.fixture(autouse=True)
def cleanup_user(users_db):
    yield
    with users_db.db.connect() as conn:
        conn.execute(
            text("DELETE FROM users WHERE user_email = :email"),
            {"email": "test@mail.ru"}
        )
        conn.commit()
# Добавление тестового пользователя


def test_add_user(users_db):
    users_db.add_user("test@mail.ru", 3)
    users = users_db.get_users()
    emails = [row._mapping["user_email"] for row in users]
    assert "test@mail.ru" in emails

# Редактирование тестового пользователя


def test_update_user_subject(users_db):
    users_db.add_user("test@mail.ru", 3)
    updated_rows = users_db.update_user_subject("test@mail.ru", 5)
    assert updated_rows == 1  # Должна обновиться ровно одна строка
    users = users_db.get_users()
    for user in users:
        if user._mapping["user_email"] == "test@mail.ru":
            assert user._mapping["subject_id"] == 5
            break
    else:
        pytest.fail("Пользователь не найден после обновления")

# Удадение пользователя


def test_delete_user(users_db):
    users_db.add_user("test@mail.ru", 3)
    deleted_rows = users_db.delete_user("test@mail.ru")
    assert deleted_rows == 1
