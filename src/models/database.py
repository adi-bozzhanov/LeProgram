from os import path


class Database:

    def __init__(self):
        self.dataBasePath = self.getLepDBFilePath()

    def getLepDBFilePath(self):
        basePath = path.dirname(__file__)
        return path.abspath(path.join(basePath, "..", "..", "data/databases/lepDB.db"))

    def addTest(self, testObj):
        # testObj will be created before
        # data can be accessed through getter methods 
        pass

    def getTest(self, testId):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("SELECT * FROM Test WHERE TestID = ?", (testId,))
        testData = databaseCursor.fetchone()

        databaseCursor.close()
        lepDB.commit()
        lepDB.close()

        return testData


    def getLibrary(self, libraryID): # <-- used to have a testID parameter changed to have LibraryID idk if it was a mistake
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("SELECT * FROM Library WHERE LibraryID = ?", (libraryID,))
        libraryData = databaseCursor.fetchone()

        databaseCursor.close()
        lepDB.commit()
        lepDB.close()

        return libraryData

    def addNewAnswer(self, taskID):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("""INSERT INTO answers (TaskID, AnswerExp, IsCorrect)
                                              VALUES (?, ?, ?)""", (taskID, "", 0))

        lepDB.commit()
        lepDB.close()

    def loadAnswer(self, answerID):
        lepDB = sqlite3.connect(self.dataBasePath)
        lepDBCursor = lepDB.cursor()

        lepDBCursor.execute("SELECT * FROM Answers WHERE AnswersID = ?", (answerID,))
        answerTuple = lepDBCursor.fetchone()

        return answerTuple

a = Database()
#a.getLepDBFilePath()
