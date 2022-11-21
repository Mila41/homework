import sqlite3


def get_connection():
    connection = sqlite3.connect('students.db')
    return connection


def close_connection(connection):
    if connection:
        connection.close()

def get_school_name(school_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_quary = ('SELECT * FROM School WHERE School_id = ?')
        cursor.execute(select_quary, (school_id,))
        record = cursor.fetchone()
        close_connection(connection)
        return record[1]
    except (Exception, sqlite3.Error) as error:
        print('Ошибка в получении данных по школе', error)

def get_student(school_id):
    try:
        school_name = get_school_name(school_id)
        connection = get_connection()
        cursor = connection.cursor()
        select_quary = ('SELECT * FROM Student WHERE School_id = ?')
        cursor.execute(select_quary, (school_id,))
        records = cursor.fetchall()
        print('Студенты из школы ', school_name)
        for row in records:
            print('ID студента', row[0])
            print('Имя студента', row[1])
            print('ID школы', row[2])
            print('Название школы ', school_name, '\n')   
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print('Ошибка в получении данных по школе', error)

print('ДЗ \n')
get_student(1)
