from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.teams import Team
from model.years import Year


class DAO():
    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct t.year  from teams t 
                    where t.year >=1980
                    """

        cursor.execute(query)

        for row in cursor:
            results.append(Year(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllTeams():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct *  from teams t 
                       """

        cursor.execute(query)

        for row in cursor:
            results.append(Team(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllNodes(n, idMapA):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct *  from teams t 
                    where t.year =%s
                    """

        cursor.execute(query, (n,))

        for row in cursor:
            result.append(idMapA[row["ID"]])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdgesv1(n, idMapA):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct t.ID as id,t2.ID as id2 ,SUM(s.salary+ s2.salary) AS peso
                    from teams t, teams t2 , salaries s ,salaries s2 
                    where t.year =%s
                    and t2.`year` =t.year
                    and t.ID<t2.ID 
                    and t.ID=s.teamID
                    and t2.ID =s2.teamID 
                    group by t.ID,t2.ID 
                    order by peso desc
                         """

        cursor.execute(query, (n, ))

        for row in cursor:
            result.append(
                Connessione(
                    idMapA[row["id"]],
                    idMapA[row["id2"]],
                    row["peso"]
                )
            )
        cursor.close()
        conn.close()
        return result