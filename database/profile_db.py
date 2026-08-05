from database.connection import get_connection


def get_profile():

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM profile LIMIT 1")

    profile = cursor.fetchone()

    cursor.close()

    conn.close()

    return profile
def get_dashboard_counts():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS total FROM projects")
    projects = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM skills")
    skills = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM certificates")
    certificates = cursor.fetchone()["total"]

    cursor.close()
    conn.close()

    return projects, skills, certificates

def get_dashboard_stats():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    stats = {}

    cursor.execute("SELECT COUNT(*) AS total FROM projects")
    stats["projects"] = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM skills")
    stats["skills"] = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM certificates")
    stats["certificates"] = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM achievements")
    stats["achievements"] = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM messages")
    stats["messages"] = cursor.fetchone()["total"]

    cursor.close()
    conn.close()

    return stats



def increase_visitor():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE portfolio_stats
        SET visitors = visitors + 1
        WHERE id = 1
    """)

    conn.commit()

    cursor.close()
    conn.close()


def get_visitor_count():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT visitors
        FROM portfolio_stats
        WHERE id = 1
    """)

    data = cursor.fetchone()

    cursor.close()
    conn.close()

    return data["visitors"]



