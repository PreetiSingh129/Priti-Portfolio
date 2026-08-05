from database.connection import get_connection


def save_message(name, email, subject, message):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO messages
        (
            name,
            email,
            subject,
            message
        )

        VALUES
        (%s,%s,%s,%s)
        """,

        (
            name,
            email,
            subject,
            message
        )
    )

    conn.commit()

    cursor.close()
    conn.close()


def get_all_messages():

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM messages
        ORDER BY created_at DESC
        """
    )

    messages = cursor.fetchall()

    cursor.close()
    conn.close()

    return messages


def delete_message(id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM messages WHERE id=%s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

def get_recent_messages(limit=5):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM messages
        ORDER BY id DESC
        LIMIT %s
        """,
        (limit,)
    )

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data