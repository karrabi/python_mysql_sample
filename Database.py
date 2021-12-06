import mysql.connector


class DB:

    def __init__(self, db_name):
        self.db_conn = mysql.connector.connect(
            host='localhost',
            user='frompython',
            password='P@ssw0rd'
        )
        self.dbname = db_name
        print('Connected to MySQL: '.format(self.db_conn.is_connected()))
        self.CreateOrUse()

    def CreateOrUse(self):
        print(self.db_conn.database)
        cursor = self.db_conn.cursor()
        cursor.execute('SHOW DATABASES')
        exists = False
        for name in cursor:
            if self.dbname in name:
                exists = True
        if not exists:
            cursor.execute('Create Database ' + self.dbname + ' DEFAULT CHARACTER SET latin1 COLLATE latin1_general_ci')
            print('Database {} create successfully'.format(self.dbname))
            cursor.execute('use ' + self.dbname)
            print('database used Sattus:' + str(self.db_conn.database))
        else:
            cursor.execute('use ' + self.dbname)
            print('Database {} already Exists and used now'.format(self.dbname))
            print('database used Sattus:' + str(self.db_conn.database))

        self.CreateTables()

    def CreateTables(self):
        cursor = self.db_conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS tb01 (id BIGINT NOT NULL AUTO_INCREMENT' +
                       ', field01 VARCHAR(255), field02 BIGINT, PRIMARY KEY (id))')

    def InsertRecord(self, field01, field02):
        cursor = self.db_conn.cursor()
        sql = 'INSERT INTO  tb01 (field01 , field02) VALUES ( %s , %s )'
        args = (field01, field02)
        cursor.execute(sql, args)
        self.db_conn.commit()
        print(cursor.rowcount, ' record inserted.')

    def GetAllRecords(self):
        cursor = self.db_conn.cursor()
        sql = 'SELECT * FROM tb01'
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def GetRecord(self, row_id):
        cursor = self.db_conn.cursor()
        sql = 'SELECT * FROM tb01 WHERE id = %s '
        args = (str(row_id),)
        cursor.execute(sql, args)
        result = cursor.fetchall()
        return result
