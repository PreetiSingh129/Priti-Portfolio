from database.connection import get_connection


def get_all_skills():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM skills ORDER BY id DESC"

    cursor.execute(query)

    skills = cursor.fetchall()

    cursor.close()
    conn.close()

    return skills

def delete_skill(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM skills WHERE id=%s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()