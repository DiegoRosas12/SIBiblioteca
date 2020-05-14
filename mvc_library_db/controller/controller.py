from model.model import Model
from view.view import View
from datetime import date

class Controller:
    """
    *******************************
    * A controller for a library DB *
    *******************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.main_menu()

    """
    ***********************
    * General controllers *
    ***********************
    """
    def main_menu(self):
        o = '0'
        while o != '5':
            self.view.main_menu()
            self.view.option('5')
            o = input()
            if o == '1':
                self.zips_menu()
            elif o == '2':
                self.books_menu()
            elif o == '3':
                self.users_menu()
            elif o == '4':
                self.loans_menu()
            elif o == '5':
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields,vals
    
    """
    ************************
    * Controllers for zips *
    ************************
    """
    def zips_menu(self):
        o = '0'
        while o != '7':
            self.view.zips_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_zip()
            elif o == '2':
                self.read_a_zip()
            elif o == '3':
                self.read_all_zips()
            elif o == '4':
                self.read_zips_city()
            elif o == '5':
                self.update_zip()
            elif o == '6':
                self.delete_zip()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_zip(self):
        self.view.ask('Ciudad: ')
        city = input()
        self.view.ask('Estado: ')
        state = input()
        return [city,state]
    
    def create_zip(self):
        self.view.ask('Codigo Postal: ')
        i_zip = input()
        city, state = self.ask_zip()
        out = self.model.create_zip(i_zip, city, state)
        if out == True:
            self.view.ok(i_zip, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('El Codigo Posta ya esta registrado')
            else:
                self.view.error('No se pudo agregar el Codigo Postal.')
        return

    def read_a_zip(self):
        self.view.ask('CP: ')
        i_zip = input()
        zip = self.model.read_a_zip(i_zip)
        if type(zip) == tuple:
            self.view.show_zip_header(' Datos del CP '+i_zip+' ')
            self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            if zip == None:
                self.view.error('El Codigo Postal NO existe')
            else:
                self.view.error('Problema para leer el Codigo Postal')
        return

    def read_all_zips(self):
        zips = self.model.read_all_zips()
        if type(zips) == list:
            self.view.show_zip_header(' Codigos Postales ')
            for zip in zips:
                self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            self.view.error('Error al leer todos los codigos postales')
        return

    def read_zips_city(self):
        self.view.ask('Ciudad: ')
        city = input()
        zips = self.model.read_zips_city(city)
        if type(zips) == list:
            self.view.show_zip_header(' Codigos Postales para la ciudad de '+city+' ')
            for zip in zips:
                self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            self.view.error('Error al leer los codigos postales')
        return

    def update_zip(self):
        self.view.ask('Codigo Postal a modificar: ')
        i_zip = input()
        zip = self.model.read_a_zip(i_zip)
        if type(zip) == tuple:
            self.view.show_zip_header(' Datos del Codigo Postal '+i_zip+' ')
            self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            if zip == None:
                self.view.error('El Codigo Postal NO existe')
            else:
                self.view.error('Error al leer el codigo postal.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_zip()
        fields, vals = self.update_lists(['z_city','z_state'], whole_vals)
        vals.append(i_zip)
        vals = tuple(vals)
        out = self.model.update_zip(fields, vals)
        if out == True:
            self.view.ok(i_zip, 'actualizo')
        else:
            self.view.error('No se pudo actualizar el codigo postal')
        return

    def delete_zip(self):
        self.view.ask('CP a borrar: ')
        i_zip = input()
        count = self.model.delete_zip(i_zip)
        if count != 0:
            self.view.ok(i_zip, 'borro')
        else:
            if count == 0:
                self.view.error('El Codigo Postal NO xiste')
            else:
                self.view.error('Error al borrar el Codigo Postal.')
        return
    
    """
    ****************************
    * Controllers for books *
    ****************************
    """
    def books_menu(self):
        o = '0'
        while o != '8':
            self.view.books_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_book()
            elif o == '2':
                self.read_a_book()
            elif o == '3':
                self.read_all_books()
            elif o == '4':
                self.read_books_author()
            elif o == '5':
                self.read_books_pages_range()
            elif o == '6':
                self.update_book()
            elif o == '7':
                self.delete_book()
            elif o == '8':
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_book(self):
        self.view.ask('ISBN: ')
        isbn = input()
        self.view.ask('Titulo: ')
        title = input()
        self.view.ask('Autor: ')
        author = input()
        self.view.ask('Editorial: ')
        edit = input()
        self.view.ask('Edicion: ')
        edition = input()
        self.view.ask('Fecha de publicación: ')
        pubdate = input()
        self.view.ask('Categoria: ')
        category = input()
        self.view.ask('Descripcion: ')
        descrip = input()
        self.view.ask('Idioma: ')
        language = input()
        self.view.ask('Numero de paginas: ')
        nopages = input()
        self.view.ask('Estanteria: ')
        estant = input()
        self.view.ask('Cantidad disponible: ')
        quan = input()
        return [isbn,title,author,edit,edition,pubdate,category,descrip,language,nopages,estant,quan]

    def create_book(self):
        isbn, title, author, edit, edition, pubdate, category, descrip, language, nopages, estant, quan = self.ask_book()
        out = self.model.create_book(isbn, title, author, edit, edition, pubdate, category, descrip, language, nopages, estant, quan)
        if out == True:
            self.view.ok(title+' '+author, 'agrego')
        else:
            self.view.error('No se pudo agregar el libro.')
        return
    
    def read_a_book(self):
        self.view.ask('ISBN: ')
        isbn = input()
        book = self.model.read_a_book(isbn)
        if type(book) == tuple:
            self.view.show_book_header(' Datos del libro '+isbn+' ')
            self.view.show_a_book(book)
            self.view.show_book_midder()
            self.view.show_book_footer()
        else:
            if book == None:
                self.view.error('El libro no existe')
            else:
                self.view.error('Error al leer el libro')
        return
    
    def read_all_books(self):
        books = self.model.read_all_books()
        if type(books) == list:
            self.view.show_book_header(' Todos los libros ')
            for book in books:
                self.view.show_a_book(book)
                self.view.show_book_midder()
            self.view.show_book_footer()
        else:
            self.view.error('Error el leer todos los libros.')
        return

    def read_books_author(self):
        self.view.ask('Autor: ')
        author = input()
        books = self.model.read_books_author(author)
        if type(books) == list:
            self.view.show_book_header(' Libros del autor '+author+' ')
            for book in books:
                self.view.show_a_book(book)
                self.view.show_book_midder()
            self.view.show_book_footer()
        else:
            self.view.error('Error al leer los libros del autor')
        return

    def read_books_pages_range(self):
        self.view.ask('Paginas minimo: ')
        pages_min = input()
        self.view.ask('Paginas maximo: ')
        pages_max = input()
        books = self.model.read_books_pages_range(float(pages_min), float(pages_max))
        if type(books) == list:
            self.view.show_book_header(' Productos entre '+pages_min+' y '+pages_max+' ')
            for book in books:
                self.view.show_a_book(book)
                self.view.show_book_midder()
            self.view.show_book_footer()
        else:
            self.view.error('Error al leer los libros con ciertas paginas.')
        return

    def update_book(self):
        self.view.ask('ISBN a modificar: ')
        isbn = input()
        book = self.model.read_a_book(isbn)
        if type(book) == tuple:
            self.view.show_book_header(' Datos del producto '+isbn+' ')
            self.view.show_a_book(book)
            self.view.show_book_midder()
            self.view.show_book_footer()
        else:
            if book == None:
                self.view.error('El libro no existe')
            else:
                self.view.error('Error al bsucar y leer el libro')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_book()
        fields, vals = self.update_lists(['isbn','b_title','b_author','b_editorial','b_edition','b_publidate','b_category','b_description','b_language','b_pages','b_shelving','b_quantity'], whole_vals)
        vals.append(isbn)
        vals = tuple(vals)
        out = self.model.update_book(fields, vals)
        if out == True:
            self.view.ok(isbn, 'actualizo')
        else:
            self.view.error('No se pudo actualizar el libro')
        return

    def delete_book(self):
        self.view.ask('ISBN a borrar: ')
        isbn = input()
        count = self.model.delete_book(isbn)
        if count != 0:
            self.view.ok(isbn, 'borro')
        else:
            if count == 0:
                self.view.error('El libro no existe')
            else:
                self.view.error('Error al borrar el libro')
        return

    """
    ***************************
    * Controllers for clients *
    ***************************
    """
    def users_menu(self):
        o = '0'
        while o != '7':
            self.view.users_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_user()
            elif o == '2':
                self.read_a_user()
            elif o == '3':
                self.read_all_users()
            elif o == '4':
                self.read_users_zip()
            elif o == '5':
                self.update_user()
            elif o == '6':
                self.delete_user()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_user(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Apellido paterno: ')
        lname1 = input()
        self.view.ask('Apellido materno: ')
        lname2 = input()
        self.view.ask('Email: ')
        email = input()
        self.view.ask('Telefono: ')
        phone = input()
        self.view.ask('Calle: ')
        street = input()
        self.view.ask('No exterior: ')
        noext = input()
        self.view.ask('No interior: ')
        noint = input()
        self.view.ask('Colonia: ')
        col = input()
        self.view.ask('CP: ')
        zip = input()
        
        return [name,lname1,lname2,email,phone,street,noext,noint,col,zip]

    def create_user(self):
        name, lname1 ,lname2 , email, phone, street, noext, noint, col, zip = self.ask_user()
        out = self.model.create_user(name, lname1, lname2, street, noext, noint, col, zip, email, phone)
        if out == True:
            self.view.ok(name+' '+lname1+' '+lname2, 'agrego')
        else:
            self.view.error('Error al agregar usuario')
        return
    
    def read_a_user(self):
        self.view.ask('ID usuario: ')
        id_user = input()
        user = self.model.read_a_user(id_user)
        if type(user) == tuple:
            self.view.show_user_header(' Datos del usuario '+id_user+' ')
            self.view.show_a_user(user)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            if user == None:
                self.view.error('El usuario no existe')
            else:
                self.view.error('Error al leer el usuario')
        return

    def read_all_users(self):
        users = self.model.read_all_users()
        if type(users) == list:
            self.view.show_user_header(' Todos los usuarios ')
            for user in users:
                self.view.show_a_user(user)
                self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            self.view.error('Error al leer todos los clientes')
        return
    
    def read_users_zip(self):
        self.view.ask('Codigo Postal: ')
        zip = input()
        users = self.model.read_users_zip(zip)
        if type(users) == list:
            self.view.show_user_header(' Usuarios en el Codigo Postal '+zip+' ')
            for user in users:
                self.view.show_a_user(user)
                self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            self.view.error('Error al leer los usuarios por CP')
        return

    def update_user(self):
        self.view.ask('ID del usuario a modificar: ')
        id_user = input()
        user = self.model.read_a_user(id_user)
        if type(user) == tuple:
            self.view.show_user_header(' Datos del cliente '+id_user+' ')
            self.view.show_a_user(user)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            if user == None:
                self.view.error('El usuario no existe')
            else:
                self.view.error('Error al actualizar cliente')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_user()
        fields, vals = self.update_lists(['u_fname','u_lname1','u_lname2','c_email','c_phone','c_street','c_noext','c_noint','c_col','c_zip'], whole_vals)
        vals.append(id_user)
        vals = tuple(vals)
        out = self.model.update_user(fields, vals)
        if out == True:
            self.view.ok(id_user, 'actualizo')
        else:
            self.view.error('Error al actualizar al usuario')
        return

    def delete_user(self):
        self.view.ask('ID del usuario a borrar: ')
        id_user = input()
        count = self.model.delete_user(id_user)
        if count != 0:
            self.view.ok(id_user, 'borro')
        else:
            if count == 0:
                self.view.error('El usuario no existe')
            else:
                self.view.error('Error al borrar al usuario')
        return
    
    """
    **************************
    * Controllers for loans *
    **************************
    """
    def loans_menu(self):
        o = '0'
        while o != '11':
            self.view.loans_menu()
            self.view.option('11')
            o = input()
            if o == '1':
                self.create_loan()
            elif o == '2':
                self.read_a_loan()
            elif o == '3':
                self.read_all_loans()
            elif o == '4':
                self.read_loans_loandate()
            elif o == '5':
                self.read_loans_users()
            elif o == '6':
                self.update_loan()
            elif o == '7':
                self.add_loan_details()
            elif o == '8':
                self.update_loan_details()
            elif o == '9':
                self.delete_loan_details()
            elif o == '10':
                self.delete_loan()
            elif o == '11':
                return
            else:
                self.view.not_valid_option()
        return

    def create_loan(self):
        self.view.ask('ID usuario: ')
        id_user = input()
        self.view.ask('Fecha de vencimiento: ')
        expdate= input()
        lds_status = 'undelivered'
        today = date.today()
        o_date = today.strftime('%y-%m-%d')
        id_loan = self.model.create_loan(id_user, o_date, expdate, lds_status)
        if type(id_loan) == int:
            isbn = ' '
            while isbn != '':
                self.view.msg('---- Agrega libros al prestamo (deja vacio el id del libro para salir) ---')
                isbn = self.create_loan_details(isbn)
            self.model.update_loan((),(id_user))
        else:
            self.view.error('No se pudo hacer el prestamo')

    def read_a_loan(self):
        self.view.ask('ID prestamo: ')
        id_loan = input()
        loan = self.model.read_a_loan(id_loan)
        if type(loan) == tuple:
            loan_details = self.model.read_loan_details(id_loan)
            if type(loan_details) != list and loan_details != None:
                self.view.error('Error al leer el prestamo')
            else:
                self.view.show_loan_header(' Datos de la orden '+id_loan+' ')
                self.view.show_loan(loan)
                self.view.show_loan_details_header()
                for loan_detail in loan_details:
                    self.view.show_a_loan_details(loan_detail)
                self.view.show_loan_details_footer()
                self.view.show_loan_footer()
                return loan
        else:
            if loan == None:
                self.view.error('El prestamo no existe')
            else:
                self.view.error('Error al leer el prestamo')
        return

    def read_all_loans(self):
        loans = self.model.read_all_loans()
        if type(loans) == list:
            self.view.show_loan_header(' Todos los prestamos ')
            for loan in loans:
                id_loan = loan[0]
                loan_details = self.model.read_loan_details(id_loan)
                if type(loan_details) != list and loan_details != None:
                    self.view.error('PROBLEMA AL LEER LA ORDEN '+id_loan+'. REVISA.')
                else:
                    self.view.show_loan(loan)
                    self.view.show_loan_details_header()
                    for loan_detail in loan_details:
                        self.view.show_a_loan_details(loan_detail)
                    self.view.show_loan_details_footer()
                    self.view.show_loan_midder()
            self.view.show_loan_footer()
        else:
            self.view.error('Error al leer los prestamos')
        return

    def read_loans_loandate(self):
        self.view.ask('Fecha: ')
        ldate = input()
        loans = self.model.read_loans_loandate(ldate)
        if type(loans) == list:
            self.view.show_loan_header(' Prestamos para la fecha '+ldate+' ')
            for loan in loans:
                id_loan = loan[0]
                loan_details = self.model.read_loan_details(id_loan)
                if type(loan_details) != list and loan_details != None:
                    self.view.error('Error al leer el prestamo '+id_loan+'. REVISA.')
                else:
                    self.view.show_loan(loan)
                    self.view.show_loan_details_header()
                    for loan_detail in loan_details:
                        self.view.show_a_loan_details(loan_detail)
                    self.view.show_loan_details_footer()
                    self.view.show_loan_midder()
            self.view.show_loan_footer()
        else:
            self.view.error('Error al leer los prestamo')
        return

    def read_loans_users(self):
        self.view.ask('ID usuario: ')
        id_user = input()
        loans = self.model.read_loans_users(id_user)
        if type(loans) == list:
            self.view.show_loan_header(' Ordenes para el cliente '+id_user+' ')
            for loan in loans:
                id_loan = loan[0]
                loan_details = self.model.read_loan_details(id_loan)
                if type(loan_details) != list and loan_details != None:
                    self.view.error('Error al leer la orden '+id_loan+'. REVISA.')
                else:
                    self.view.show_loan(loan)
                    self.view.show_loan_details_header()
                    for loan_detail in loan_details:
                        self.view.show_a_loan_details(loan_detail)
                    self.view.show_loan_details_footer()
                    self.view.show_loan_midder()
            self.view.show_loan_footer()
        else:
            self.view.error('Error al leer los prestamos.')
        return

    def update_loan(self):
        self.view.ask('ID del prestamo a modificar: ')
        id_loan = input()
        loan = self.model.read_a_loan(id_loan)
        if type(loan) == tuple:
            self.view.show_loan_header(' Datos de la orden '+id_loan+' ')
            self.view.show_loan(loan)
            self.view.show_loan_footer()
        else:
            if loan == None:
                self.view.error('El prestamo no existe')
            else:
                self.view.error('Error al leer el prestamo')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        self.view.ask('ID Usuario: ')
        id_user = input()
        self.view.ask('Estado (UNDELIVERED,DELIVERED,LATE): ')
        lds_status = input()
        self.view.ask('Fecha Prestamo (yyyy/mm/dd): ')
        loan_date = input()
        self.view.ask('Fecha Vencimiento (yyyy/mm/dd): ')
        exp_date = input()
        whole_vals = [id_user, loan_date, exp_date, lds_status]
        fields, vals = self.update_lists(['id_user','loan_date', 'exp_date' , 'lds_status'], whole_vals)
        vals.append(id_loan)
        vals = tuple(vals)
        out = self.model.update_loan(fields, vals)
        if out == True:
            self.view.ok(id_loan, 'actualizo')
        else:
            self.view.error('Error al actualizar el prestamo')
        return 

    def delete_loan(self):
        self.view.ask('Id del prestamo a borrar: ')
        id_loan = input()
        count = self.model.delete_loan(id_loan)
        if count != 0:
            self.view.ok(id_loan, 'borro')
        else:
            if count == 0:
                self.view.error('El prestamo no existe')
            else:
                self.view.error('Error al borrar el prestamo')
        return

    """
    *********************************
    * Controllers for loan details *
    *********************************
    """
    def create_loan_details(self, id_loan):
        self.view.ask('ISBN: ')
        isbn = input()
        if isbn != '':
            book = self.model.read_a_book(isbn)
            if type(book) == tuple:
                self.view.show_book_header(' Datos del libro '+isbn+' ')
                self.view.show_a_book(book)
                self.view.show_book_footer()
                self.view.ask('Fecha Entregado: ')
                deli_date = input()
                out = self.model.create_loan_detail(id_loan, isbn, deli_date)
                if out == True:
                    self.view.ok(book[1]+' '+book[2], 'agrego a la orden')
                else:
                    if out.errno == 1062:
                        self.view.error('El libro ya está en la orden')
                    else:
                        self.view.error('No se pudo agregar el libro.')
            else:
                if book == None:
                    self.view.error('El libro no existe')
                else:
                    self.view.error('error al leer el lirbo.')
        return isbn

    def add_loan_details(self):
        loan = self.read_a_loan()
        if type(loan) == tuple:
            id_loan = loan[0]
            isbn = ' '
            while isbn != '':
                self.view.msg('---- Agrega libros al prestamo (deja vacio el id del libro para salir) ---')
                isbn = self.create_loan_details(id_loan)
            self.model.update_loan((),(id_loan))
        return

    def update_loan_details(self):
        loan = self.read_a_loan()
        if type(loan) == tuple:
            id_loan = loan[0]
            isbn = ' '
            while isbn != '':
                self.view.msg('---- Modifica libros al prestamo (deja vacio el id del libro para salir) ---')
                self.view.ask('ISBN: ')
                isbn = input()
                if isbn != '':
                    loan_detail = self.model.read_a_loans_detail(id_loan, isbn)
                    if type(loan_detail) == tuple:
                        book = self.model.read_a_book(isbn)
                        self.view.ask('Fecha Entregado: ')
                        deli_date = input()
                        fields, whole_vals = self.update_lists(['deli_date'],[deli_date])
                        whole_vals.append(id_loan)
                        whole_vals.append(isbn)
                        self.model.update_loan_details(fields, whole_vals)
                        self.view.ok(isbn, 'actualizo en la orden ')
                    else:
                        if loan_detail == None:
                            self.view.error('El libro no existe en el prestamo')
                        else:
                            self.view.error('Error al actualizar el libro')
            self.model.update_loan((),(id_loan))
        return

    def delete_loan_details(self):
        loan = self.read_a_loan()
        if type(loan) == tuple:
            id_loan = loan[0]
            isbn = ' '
            while isbn != '':
                self.view.msg('---- Borra libros del prestamo (deja vacio el id del libro para salir) ---')
                self.view.ask('ISBN: ')
                isbn = input()
                if isbn != '':
                    loan_detail = self.model.read_a_loans_detail(id_loan, isbn)
                    count = self.model.delete_loan_details(id_loan, isbn)
                    if type(loan_detail) == tuple and count != 0:
                        self.view.ok(isbn, 'borro del prestamo ')
                    else:
                        if loan_detail == None:
                            self.view.error('El libro no existe en el prestamp')
                        else:
                            self.view.error('Error al borrar libro del prestamo')
            self.model.update_loan((),(id_loan))
        return




















