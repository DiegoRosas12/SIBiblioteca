from mysql import connector

class Model:
    """
    *********************************************
    * A data model with MYSQL for a library DB *
    *********************************************
    """

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d
    
    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor() #Para consultas u operaciones en MySQL

    def close_db(self):
        self.cnx.close()

    """
    ****************
    * ZIP methods *
    ****************
    """

    def create_zip(self, zip, city, state):
        try: 
            sql = 'INSERT INTO zips (`zip`, `z_city`, `z_state`) VALUES (%s, %s, %s)'
            vals = (zip, city, state)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_zip(self, zip):
        try:
            sql = 'SELECT * FROM zips WHERE zip = %s'
            vals = (zip,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_zips(self):
        try:
            sql = 'SELECT * FROM zips'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_zips_city(self, city):
        try:
            sql = 'SELECT * FROM zips WHERE z_city = %s'
            vals = (city,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_zip(self, fields, vals):
        try:
            sql = 'UPDATE zips SET'+','.join(fields)+'WHERE zip = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_zip(self, zip):
        try:
            sql = 'DELETE FROM zips WHERE zip = %s'
            vals = (zip,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    

    """
    ****************
    * Books methods *
    ****************
    """

    def create_book(self, isbn, title, author, editorial, edition, publication, category, description, language, pages, shelving, quantity):
        try: 
            sql = 'INSERT INTO books (`isbn`, `b_title`, `b_author`, `b_editorial`, `b_edition`, `b_publidate`, `b_category`, `b_description`, `b_language`, `b_pages`, `b_shelving`, `b_quantity`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            vals = (isbn, title, author, editorial, edition, publication, category, description, language, pages, shelving, quantity)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_book(self, isbn):
        try:
            sql = 'SELECT * FROM books WHERE isbn = %s'
            vals = (isbn,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_books(self):
        try:
            sql = 'SELECT * FROM books'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_books_author(self, author):
        try:
            sql = 'SELECT  * FROM books WHERE b_author = %s'
            vals = (author,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_books_pages_range(self, pages_min, pages_max):
        try:
            sql = 'SELECT * FROM books WHERE b_quantity >= %s and b_quantity <= %s'
            vals = (pages_min, pages_max)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_book(self, fields, vals):
        try:
            sql = 'UPDATE books SET'+','.join(fields)+'WHERE isbn = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_book(self, isbn):
        try:
            sql = 'DELETE FROM books WHERE isbn = %s'
            vals = (isbn,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ****************
    * User methods *
    ****************
    """
    def create_user(self, name, flname, slname, email, phone, street, noext, noint, col, zip):
        try: 
            sql = 'INSERT INTO users (`u_fname`, `u_lname1`, `u_lname2`, `u_email`, `u_phone`, `u_street`, `u_noext`, `u_noint`, `u_col`, `u_zip`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            vals = (name, flname, slname, email, phone, street, noext, noint, col, zip)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
        
    def read_a_user(self, id_user):
        try:
            sql = 'SELECT users.*,zips.z_city,zips.z_state FROM users JOIN zips ON users.u_zip = zips.zip and users.id_user = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_users(self):
        try:
            sql = 'SELECT users.*,zips.z_city,zips.z_state FROM users JOIN zips ON users.u_zip = zips.zip'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_users_zip(self, zip):
        try:
            sql = 'SELECT users.*,zips.z_city,zips.z_state FROM users JOIN zips ON users.u_zip = zips.zip and users.u_zip = %s'
            vals = (zip,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_user(self, fields, vals):
        try:
            sql = 'UPDATE users SET'+','.join(fields)+'WHERE id_user = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_user(self, id_user):
        try:
            sql = 'DELETE FROM users WHERE id_user = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ****************
    * Loan methods *
    ****************
    """
    def create_loan(self, id_user, initdate, expdate):
        try: 
            sql = 'INSERT INTO loans (`id_user`, `loan_date`, `expiration_date`) VALUES (%s, %s, %s)'
            vals = (id_user, initdate, expdate)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_loan = self.cursor.lastrowid
            return id_loan
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_loan(self, id_loan):
        try:
            sql = 'SELECT loans.*,users.*,zips.* FROM loans JOIN users ON users.id_user = loans.id_user and loans.id_loan = %s JOIN zips ON zips.zip = users.u_zip'
            vals = (id_loan,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_loans(self):
        try:
            sql = 'SELECT loans.*,users.*,zips.* FROM loans JOIN users ON users.id_user = loans.id_user JOIN zips ON zips.zip = users.u_zip'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_loans_loandate(self, initdate):
        try:
            sql = ' SELECT loans.*, users.*, zips.* FROM loans JOIN users ON users.id_user = loans.id_user and loans.loan_date = %s JOIN zips ON zips.zip = users.u_zip'
            vals = (initdate,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_loans_users(self, id_user):
        try:
            sql = ' SELECT loans.*, users.*, zips.* FROM loans JOIN users ON users.id_user = loans.id_user and loans.id_client = %s JOIN zips ON zips.zip = users.u_zip'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_loan(self, fields, vals):
        try:
            sql = 'UPDATE loans SET'+','.join(fields)+'WHERE id_loan = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_loan(self, id_loan):
        try:
            sql = 'DELETE FROM loans WHERE id_loan = %s'
            vals = (id_loan,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ****************
    * Loan details methods *
    ****************
    """

    def create_loan_detail(self, id_loan, isbn, status, delivery):
        try: 
            sql = 'INSERT INTO loans_details (`id_loan`, `isbn`, `lds_status`, `delivery_date`) VALUES (%s, %s, %s, %s)'
            vals = (id_loan, isbn, status, delivery)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_loans_detail(self, id_loan, isbn):
        try:
            sql = 'SELECT books.isbn, books.b_title, books.b_author, books.b_editorial, books.edition, books.b_publidate, books.b_category, books.b_description, books.b_language, books.b_pages, books.b_shelving, books.b_quantity, loans_details.lds_status, loans_details.delivery_date FROM loans_details JOIN books ON loans_details.isbn = books.isbn and loans_details.id_loan = %s and loan_details.isbn = %s'
            vals = (id_loan,isbn)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_loan_details(self, id_loan):
        try:
            sql = 'SELECT books.isbn, books.b_title, books.b_author, books.b_editorial, books.edition, books.b_publidate, books.b_category, books.b_description, books.b_language, books.b_pages, books.b_shelving, books.b_quantity, loans_details.lds_status, loans_details.delivery_date FROM loans_details JOIN books ON loans_details.isbn = books.isbn and loans_details.id_loan = %s'
            vals = (id_loan,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_loan_details(self, fields, vals):
        try:
            sql = 'UPDATE loans_details SET'+','.join(fields)+'WHERE id_loan = %s and isbn = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_loan_details(self, id_loan, isbn):
        try:
            sql = 'DELETE FROM loans_details WHERE id_loan = %s and isbn = %s'
            vals = (id_loan, isbn)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err








