import MySQLdb

connect = MySQLdb.connect (host = "localhost",
                        user = "einnerlink",
                        passwd = "hey!n3r",
                        db = "sbienes",
                        charset='utf8', 
                        use_unicode=False)
cursor = connect.cursor ()
