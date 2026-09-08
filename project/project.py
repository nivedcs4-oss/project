# import mysql.connector
#
#
# class DbConnect:
#
#     def get_connection(self):
#         try:
#             self.connection = mysql.connector.connect(
#                 host="localhost",
#                 user="root",
#                 password="Lucky@2255",
#                 database="gym_db"
#             )
#             return self.connection
#
#         except Exception as e:
#             return None
# class GymMemberManager(DbConnect):
#     pass
#
# connection_istance = DbConnect()
# connection_istance.get_connection()
import mysql.connector


class DbConnect:

    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Lucky@2255",
                database="gym_db"
            )
            return self.connection

        except Exception as e:
            return None


class GymMemberManager(DbConnect):

    def get(self, id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            if id != None:
                query = "SELECT * FROM member WHERE id = %s"
                values = (id,)
                self.cursor.execute(query, values)
                record = self.cursor.fetchone()
                return record

            else:
                query = "SELECT * FROM member"
                self.cursor.execute(query)
                records = self.cursor.fetchall()
                print(records)

        except Exception as e:
            print(e)

    def post(self, **kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = "insert into member(name,place,plan,mobile,fee,joined)Values(%s,%s,%s,%s,%s,%s)"

            values = [v for v in kwargs.values()]

            self.cursor.execute(query, values)
            self.connect.commit()

            print("New member added successfully.....!")

        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            record = self.get(id=id)

            if record != None:
                self.cursor = self.connect.cursor()

                query = "DELETE FROM member WHERE id = %s"
                values = (id,)

                self.cursor.execute(query, values)
                self.connect.commit()

                print("Member deleted successfully.....!")

            else:
                print("Member not found.....!")

        except Exception as e:
            print(e)

    def put(self, id=None, **kwargs):
        try:
            record = self.get(id=id)

            if record != None:
                self.cursor = self.connect.cursor()

                placeholder = ""

                for k in kwargs.keys():
                    placeholder += k + "=%s,"

                placeholder = placeholder.rstrip(",")

                query = f"UPDATE member SET {placeholder} WHERE id=%s"

                values = [v for v in kwargs.values()]
                values.append(id)

                self.cursor.execute(query, values)
                self.connect.commit()

                print("Member details updated successfully")

            else:
                print("Member not found")

        except Exception as e:
            print(e)


connection_instance = DbConnect()
print(connection_instance.get_connection())

member_instance = GymMemberManager()

member_instance.get()

member_instance.put(
    id=3,
    name="Lucky",
    place="Kochi",
    plan="5000",
    mobile="7994672536",
    fee=5000,
    joined="2026-09-02"
)

member_instance.delete(id=2)