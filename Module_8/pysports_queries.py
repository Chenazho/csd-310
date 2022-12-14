import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports", 
    "raise_on_warnings": True 
}

try: 
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to mysql on host {} with database {}" .format(config["user"], config["host"], config["databases"]))
    input("\n\n Press any key to continue...")
except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_CHANGE_USER_ERROR:
            print(" The supplied username and password are invalid")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(" The specified database does not exists")
        else: 
            print(err)
finally: 
    db.close()


cursor = config.cursor()

cursor.execute('SELECT team_id, team_name, mascot FROM team')

teams = cursor.fetchall()
for team in teams:
    print('Team Name: {}'.format(team[1]))