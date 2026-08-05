from database.connection import get_connection


def get_about():

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM about LIMIT 1"
    )

    data = cursor.fetchone()

    cursor.close()
    conn.close()

    return data



def update_about(data):

    conn = get_connection()

    cursor = conn.cursor()


    query = """
    UPDATE about SET

    name=%s,
    description=%s,
    degree=%s,
    college=%s,
    current_sgpa=%s,
    highest_sgpa=%s,
    interest1=%s,
    interest2=%s,
    interest3=%s,
    interest4=%s,
    career_goal=%s

    WHERE id=1
    """


    cursor.execute(query,data)

    conn.commit()

    cursor.close()
    conn.close()