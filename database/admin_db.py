from database.connection import get_connection


def login(username, password):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT * FROM admin
        WHERE username=%s AND password=%s
        """,
        (username, password)
    )

    admin = cursor.fetchone()

    cursor.close()
    conn.close()

    return admin