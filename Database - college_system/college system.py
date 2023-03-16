import mysql.connector as mysql
#studentul poate vizualiza prezentele din tabelul attendance, ce are coloanele id, username, data, status
#profesorul poate vizualiza, adauga si modifica prezentele studentului

db = mysql.connect(host="localhost", user="root", database="college")
command_handler = db.cursor(buffered=True) #buffered=True - se pot executa mai multe operatii in db in acelasi timp

def student_session():
    print('Login succesful!')
    print('Welcome to the session!')
    while True:
        print('')
        print('STUDENT MENU')
        print('* View Register *')
        primt(' ** Download Register **')
        print('o Logout o')
        user_option = input(str("Option: "))
        if user_option == '*':
            username = (str(username),)
            print('')
            print('View Grades')
            command_handler.execute("SELECT date, username, status FROM attendance WHERE username  = %s",username)
            records = command_handler.fetchall() # records va primi toate datele din tabelul attendance
            for record in records:
                print(record)
        if user_option == '**':
            print('Downloading Register')
            username = (str(username),)
            print('')
            print('View Grades')
            command_handler.execute("SELECT date, username, status FROM attendance WHERE username  = %s",username)
            records = command_handler.fetchall()
            for record in records:
                with open("/home/mikhaelos11/Desktop/register.txt", "w") as f:
                    f.write(str(records)+"\n")  #se vor scrie datele intr un fisier text salvat la adresa specificata
                    f.close()
                    print("All records saved")
        elif user_option == 'o':
            break
        else: 
            print("No valid option selected")


def teacher_session():
    print('Login succesful!')
    print('Welcome to the session!')
    while True:
        print('')
        print('TEACHER MENU')
        print('* Mark student register *')
        print('** View register **')
        print('o Logout o')
        user_option = input(str("Option: "))
        if user_option == '*':
            print('')
            print('Mark student register ')
            command_handler.execute("SELECT username FROM users WHERE privilege = 'student'")
            records = command_handler.fetchall()
            date = input(str("DATE : DD/MM/YYYY : "))
            for record in records:
                record = str(record).replace("'","")
                record = str(record).replace(",","")
                record = str(record).replace("()","")
                record = str(record).replace(")","")
                # PRESENT | ABSENT |LATE
                status = input(str("Status for " + str(record) + "P/A/L"))
                query_vals = (str(record),date,status)
                command_handler.execute("INSERT INTO attendance(username, date, status) VALUES(%s,%s,%s)",query_vals)
                db.commit()
                print(record + " Marked as " + status)
            
        elif user_option == '**':
            print('')
            print('Viewing all student register')
            command_handler.execute("SELECT username,date,status FROM attendance")
            records = command_handler.fetchall()
            print("displaying all registers")
            for record in records:
                print(record)
            
        elif user_option == 'o':
            break #se va opri executia si va fi afisat meniul din main
        else: 
            print("No valid option selected")
    

def admin_session():
    print('Login succesful!')
    print('Welcome to the session!')
    while True:
        print('')
        print('ADMIN MENU')
        print('* Register new student *')
        print('** Register new teacher **')
        print('*** Delete existing student ***')
        print('**** Delete existing teacher ****')
        print('o Logout o')

        user_option = input(str("Option: "))
        if user_option == '*':
            print('')
            print('Register new student')
            username = input(str("Student Username: "))
            password = input(str("Student Password: "))
            query_vals=(username, password)
            command_handler.execute("INSERT INTO users(usermane, password, privilege) VALUES (%s,%s, 'student')", query_vals)
            db.commit()
            print(username + " has been registered as a student") #se scriu in tabelul users valorile username,password, status

        elif user_option == '**':
            print('')
            print('Register new teacher')
            username = input(str("Teacher Username: "))
            password = input(str("Teacher Password: "))
            query_vals=(username, password)
            command_handler.execute("INSERT INTO users(usermane, password, privilege) VALUES (%s,%s, 'teacher')", query_vals)
            db.commit()
            print(username + " has been registered as a teacher")
        elif user_option == '***':
            print('')
            print('Delete existing student account')
            username = input(str("Student Username: "))
            query_vals=(username,'student')
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1: #returneaza numarul de randuri afectate de SELECT
                print(f"No student named {username} was found")
            else:
                print(username + " has been deleted")
        elif user_option == '****':
            print('')
            print('* Delete existing teacher account *')
            username = input(str("Teacher Username: "))
            query_vals=(username,'teacher')
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print(f"No teacher named {username} was found")
            else:
                print(username + " has been deleted")
        elif user_option == "o":
            break
        else: 
            print("No valid option selected")
        
def auth_student():
    print('---------------')
    print('Student login')
    print('---------------')
    username = input(str('Username: '))
    password = input(str('Password: '))
    query_vals = (username, password,"student")
    command_handler.execute("SELECT username FROM users WHERE username = %s AND password = %s AND privilege = %s"% query_vals)
    if command_handler.rowcount < 1:
        print("Login not recognised")
    else:                   #daca sunt recunoscute credentialele, va intra in executie student_session()
        student_session()
        
            
        
def auth_teacher():
    print('---------------')
    print('Teacher login')
    print('---------------')
    username = input(str('Username: '))
    password = input(str('Password: '))
    query_vals = (username, password)
    command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'teacher'", query_vals)
    if command_handler.rowcount < 1:
        print("Login not recognised")
    else:
        teacher_session()
    pass
def auth_admin():
    print('---------------')
    print('Admin login')
    print('---------------')
    username = input(str('Username: '))
    password = input(str('Password: '))
    if username == 'admin':
        if password == 'password':
            admin_session()

        else:
            print('Incorrect password!')
    else:
        print('Login detail not recognised')
        

def main():

    while True:
        
        print("Bun venit la UniTBv!")
        print('')
        print('* Login as a student *')
        print('** Login as a teacher **')
        print('*** Login as administrator ***')
        user_option = input(str("Option: ")) 

        if user_option == '*':
            auth_student()
        elif user_option == '**':
            auth_teacher()
        elif user_option == '***':
            auth_admin()
        else:
            print('No valid option was selected')

main()

