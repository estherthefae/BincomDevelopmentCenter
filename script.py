import webbrowser
import cgi
import js

from mako.template import Template
import mysql.connector
from mysql.connector import Error
import datetime

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='bincomphptest',
                                         user='root',
                                         password='')
    db_Info = connection.get_server_info()
except Error as e:
    print("Error while connecting to MySQL", e)


def question_1():
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        query = """SELECT `party_score`, `party_abbreviation` FROM `announced_pu_results` 
                             WHERE `polling_unit_uniqueid` = 1"""
        cursor = connection.cursor()
        cursor.execute(query)
        individual_polling_unit = cursor.fetchall()
        print(individual_polling_unit)


def question_2():
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("select database();")
        # record = cursor.fetchone()
        query = """SELECT `polling_unit_id` FROM `polling_unit` 
                            WHERE `lga_id` = 2"""
        cursor = connection.cursor()
        cursor.execute(query)
        individual_polling_unit = cursor.fetchall()
        result = []
        for i in individual_polling_unit:
            result.append(i[0])
        total_lga = 0
        for num in result:
            next_query = f"SELECT SUM(`party_score`) FROM `announced_pu_results` WHERE `polling_unit_uniqueid` = {num}"
            cursor = connection.cursor()
            cursor.execute(next_query)
            answer = cursor.fetchall()
            solution = answer[0][0]
            if solution is None:
                pass
            else:
                total_lga += solution


def question_3():
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        query = f"""INSERT INTO `announced_pu_results` VALUES (1588, 100, 'PDP', 500, 'Tunmise', {datetime.datetime.today().strftime('%Y-%m-%d')}, '')"""
        cursor = connection.cursor()
        result = cursor.execute(query)


#
# tmp = Template(filename='QuestionOne.html')
# solution = tmp.render(a=total_lga)
#
# solution = tmp.render(a=total_lga)
#     with open(file='QuestionOne.html', mode='w') as file:
#         file.write(solution)


form_input = cgi.FieldStorage()
print(form_input.getvalue(key="name"))

