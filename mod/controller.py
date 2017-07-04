import MySQLdb

connect = MySQLdb.connect (host = "localhost",
                        user = "myuser",
                        passwd = "key",
                        db = "databse",
                        charset='utf8', 
                        use_unicode=False)
cursor = connect.cursor ()
