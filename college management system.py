import mysql.connector as mysql

db = mysql.connect(host="localhost", user="root", password="#b2a1l12a1#", database="college")
command_handler = db.cursor(buffered=True)

def admin_session():
    while 1:
        print("")
        print("Admin Menu")
        print("1. Register new Student")
        print("2. Register new Teacher")
        print("3. Delete Existing Student")
        print("4. Delete Exixting Teacher")
        print("5. Logout")

        User_option = input(str("Option : "))
        if User_option == "1":
            print("")
            print("Register New Student")
            username = input(str("Student username: "))
            password = input(str("Student password : "))
            query_vals = (username, password)
            command_handler.execute("INSERT INTO users(username, password, privilege) VALUES(%s, %s, 'student')",query_vals)
            db.commit()
            print("")
            print(username + " has been registered as a student")
        
        elif User_option == "2":
            print("")
            print("Register New Teacher")
            username = input(str("Teacher username: "))
            password = input(str("Teacher password : "))
            query_vals = (username, password)
            command_handler.execute("INSERT INTO users(username, password, privilege) VALUES(%s, %s, 'teacher')",query_vals)
            db.commit() 
            print("")
            print(username + " has been registered as a Teacher")
        
        elif User_option == "3":
            print("")
            print("Delete Existing Student Account")
            username = input(str("Student Username : "))
            query_vals = (username, "student")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print("")
                print(username + " has been deleted")

        elif User_option == "4":
            print("")
            print("Delete Existing Teacher Account")
            username = input(str("Teacher Username : "))
            query_vals = (username, "teacher")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print("")
                print(username + " has been deleted")

        elif User_option == "5":
            break
        else:
            print("No valid option selected")




def auth_admin():
    print("")
    print("Admin Login")
    print("")
    username = input(str("Username: "))
    password = input(str("Password: "))
    if username == "admin":
        if password  == "password":
            admin_session()
        else:
            print("")
            print("Login details not recognised")


def main():
    while 1:
        print("Welcome to the college system")
        print("")
        print("1. Login as student")
        print("2. Login as teacher")
        print("3. Login as admin")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("Student login")
        elif user_option == "2":
            print("Teacher login")
        elif user_option == "3":
            auth_admin() 
        else:
            print("No valid option was selected")

main()           