import pymysql
import config


class MySQL_config:
    def __init__(self):
        self.host = config.host
        self.port = config.port
        self.user = config.user
        self.password = config.password
        self.database = config.database
        self.connection = self.connect()
        self.cursor = self.connection.cursor()
        # инициализирует переменные внутри класса

    def connect(self):
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            cursorclass=pymysql.cursors.DictCursor
        )
        # подключается к базе данных

    def output(self, database):
        self.cursor.execute(f"SELECT * FROM {database}")
        return self.cursor.fetchall()
        # возвращает базу данных с именем database

    def insert(self, database, cells, values):
        #  "INSERT INTO database (name, age) VALUES ("Anna", 20);"
        self.cursor.execute(f"INSERT INTO {database} {cells} VALUES {values};")
        self.connection.commit()
        # добавляет в базу данных database елемент value в ячейку cells

    def editing(self, database, values, cells):
        # "UPDATE database SET password = 'xxxxxx' WHERE id = 'id'"
        self.cursor.execute(f"UPDATE {database} SET {values} WHERE {cells}")
        self.connection.commit()
        # изменяет в базе данных значение values для элемента cells

    def del_line(self, database, id):
        # "DELETE FROM database WHERE id = 'id';"
        self.cursor.execute(f"DELETE FROM {database} WHERE id = {id};")
        self.connection.commit()
        # удаляет из базы данных строку по PRIMARY KEY id
