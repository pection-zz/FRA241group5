import MySQLdb

class Databaze:

    #attribute.
    database = 0 #store database object.
    cur = 0 #store database cursor object.

    #initailise database from server which has username and password.
    def __init__(self,server='localhost',username='root',password='',database='zumodatabase',use_unicode=False,charset='utf8'):
        self.database = MySQLdb.connect(server, username , password ,database,use_unicode=use_unicode,charset=charset) #initailise database.
        self.cur = self.database.cursor() #initialise cursor.

    #select the (differant) select from table where column in IS tuple and print them (reverse) according to column order.
    def SELECT(self,select='*',table='*',column='',IS=(''),different = False,order='',reverse=False):
        SQL = "SELECT " #SQL store SQL command.
        if different: # check if you want to select the difference.
            SQL += "DISTINCT "
        SQL += "`"+select+"` "
        SQL += "FROM `"+table+ "` "
        if column != '': #check if you have condition.
            if type(IS) is tuple: # for multiple.
                isis = str(IS)
            else: #for only one.
                isis = "("+str(IS)+")"
            SQL += " WHERE `" + column + "` IN "+isis+" "
        if order != '': #check if you want to sort the information.
            SQL += "ORDER BY `"+order+"` "
            if reverse: #sort them reverse.
                SQL += "DESC "
            else: #sort them normally.
                SQL += "ASC "
        SQL = SQL[:-1]+";"
        self.cur.execute(SQL) #find by SQL language.
        return self.cur.fetchall() #list of the item you want.

    #count the (different) column which pass the condition from table.
    def COUNT(self,table='*',count='',column='',IS=(''),different=False):
        SQL = "SELECT COUNT(" #SQL store SQL command.
        if different: # check if you want to select the difference.
            SQL += " DISTINCT "
        SQL += count+") "
        SQL += "FROM `"+table+ "` "
        if column != '': #check if you have condition.
            if type(IS) is tuple: # for multiple.
                isis = str(IS)
            else: #for only one.
                isis = "("+str(IS)+")"
            SQL += " WHERE `" + column + "` IN "+isis+" "
        SQL = SQL[:-1]+";"
        self.cur.execute(SQL) #find by SQL language.
        return self.cur.fetchall()  #list of the item you want.

    # insert value i to column i in table.
    def ADD(self,table=None,column=[],value=[]):
        if (table is None) or (len(column) != len(value)): #checking error.
            if table is None: #printing error.
                print "error: insert to what?"
            elif len(column) != len(value):
                print "error: length of column and value isn't match"
        else:
            SQL = "INSERT "+"INTO `" +table + "`(`" #create SQL syntax.
            for element in column: #append each element in the column list to SQL syntax.
                SQL += str(element) + "` , `"
            SQL = SQL[:-3] + ") "
            SQL += "VALUES " + "("
            for element in value:
                if type(element) == int: #if element inside value list is integer then append it as interger.
                    SQL += str(element) + " , "
                else: #if element inside value list isn't integer then append it as string.
                    SQL += "'" +str(element) + "' , "
            SQL = SQL[:-2] + ");"
            self.cur.execute(SQL) #insert by SQL language.
            self.database.commit()  #commit change in sarver.

    #use your own SQL language
    def SQL(self,code):
        self.cur.execute(code) #code by SQL language.
        return self.cur.fetchall()  #list of the item you want.

    #change each element in fom list to each element in to list of table, and set condition where[0] = where[1].
    def CHANGE(self,table=None,column=[],to=[],where=[]):
        if (table==None): #printing error.
            print "error: insert to what?"
        elif (len(column) != len(to)): #printing error.
            print "error: length of fom and to isn't match"
        else: #no error.
            SQL = "UPDATE `"+table+"` SET " #set SQL syntax for changing.
            for i in range(0,len(column)): #loop through fom and to
                if type(to[i]) == int: #if element inside to list is integer then append it as interger.
                    SQL += "`"+str(column[i])+"`="+str(to[i])+" , "
                else: #if element inside to list isn't integer then append it as string.
                    SQL += "`"+str(column[i])+"`='"+str(to[i])+"' , "
            SQL = SQL [:-2]
            if where is not None: #check if condition exist.
                if type(where[1]) == int: #if where[1] is integer then append it as interger.
                    SQL += 'WHERE `'+str(where[0])+"`=" + str(where[1])+" "
                else: #if where[1] isn't integer then append it as string.
                    SQL += 'WHERE `'+str(where[0])+"`='" + str(where[1])+"' "
            self.cur.execute(SQL) #insert by SQL language.
            self.database.commit()  #commit change in sarver.


    #select the maximum value from column of table.
    def SELECT_MAX(self,table=None,column=''):
        if (table == None): #printing error.
            print "error: insert to what?"
        elif (column == None): #printing error.
            print "error: no column name ''"
        else:
            SQL = "SELECT MAX(`"+column+"`) FROM `"+table+"` "
            self.cur.execute(SQL) #insert by SQL language.
            return self.cur.fetchall()  #list of the item you want.

    #close database when you don't want to use it anymore.
    def Close(self):
        self.database.close()

    def monthToNum(self,shortMonth):

        return{'Jan' : 1,'Feb' : 2,'Mar' : 3,'Apr' : 4,'May' : 5,'Jun' : 6, 'Jul' : 7,'Aug' : 8,'Sep' : 9, 'Oct' : 10,'Nov' : 11,'Dec' : 12}[shortMonth]

'''#for testing.
a = []
db = Databaze(database = 'zumodatabase')
#a = db.SELECT(select='Stars',table='comment',column='IDuser',IS=(1,3),different=True,order='CommentID',reverse=True)
#a = db.COUNT(table='comment',count='IDcomment',column='Stars',IS=(3,4,5),different=True)
#a = db.CHANGE(table='comment',fom=['Stars','Comment'],to=[1,'hello'],where=['CommentID',3])
a = db.SELECT_MAX(table='comment',column='CommentID')
#a = db.INSERT(table='comment',column=['CommentID','IDuser','IDcomment','Comment','Stars','Date'],value=[7,2,1,"love it",5,'2016-10-24 11:34:00'])
for e in a:
    print e
db.Close()'''