class View:
    """
    ****************************
    * A view for a library DB *
    ****************************
    """

    def start(self):
        print('****************************************')
        print('**** BIENVENIDO A LA LIBRERÍA CHOLA ****')
        print('Un lindo lugar para descubrir y aprender')
        print('****************************************')

    def end(self):
        print('****************************************')
        print('****        HASTA LA PRÓXIMA        ****')
        print('****************************************')

    def main_menu(self):
        print('****************************************')
        print('****  xd     Menu Principal  xd     ****')
        print('****************************************')
        print('1. Codigos postales')
        print('2. Libros')
        print('3. Usuarios')
        print('4. Prestamos')
        print('5. Salir')

    def option(self, last):
        print('Selecciona una opcionn (1-'+last+'): ', end = '')
    
    def not_valid_option(self):
        print('Opcion no permitida\nVuelve a intentarlo')

    def ask(self, output):
        print(output, end = '')
    
    def msg(self, output):
        print(output)
    
    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    def error(self, err):
        print(' ¡ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    """
    ********************
    * Vistas para CP's *
    ********************
    """

    def zips_menu(self):
        print('****************************************')
        print('****   xd  Menu Codigo Postal  xd   ****')
        print('****************************************')
        print('1. Agregar Codigo Postal')
        print('2. Mostrar Codigo Postal')
        print('3. Mostrar todos los Codigos Postales')
        print('4. Mostrar Codigos Postales de una ciudad')
        print('5. Actualizar Codigo Postal')
        print('6. Borrar Codigo Postal')
        print('7. Regresar')
    
    def show_a_zip(self, record):
        print(f'{record[0]:<6}|{record[1]:<50}|{record[2]:<40}')

    def show_zip_header(self, header):
        print(header.center(100,'*'))
        print('CP'.ljust(6)+'|'+'Ciudad'.ljust(50)+'|'+'Estado'.ljust(40))
        print('-'*100)
    
    def show_zip_midder(self):
        print('-'*100)

    def show_zip_footer(self):
        print('*'*100)

    """
    **********************
    * Vistas para Libros *
    **********************
    """

    def books_menu(self):
        print('****************************************')
        print('****    xd     Menu Libros    xd    ****')
        print('****************************************')
        print('1. Agregar libro')
        print('2. Mostrar libro')
        print('3. Mostrar todos los libros')
        print('4. Mostrar libros de un autor')
        print('5. Mostrar libros con cierto numero de páginas')
        print('6. Actualizar libro')
        print('7. Borrar libro')
        print('8. Regresar')

    def show_a_book(self, record):
        print('ISBN: ', record[0])
        print('Titulo: ', record[1])
        print('Autor: ', record[2])
        print('Editorial: ', record[3])
        print('Edición: ', record[4])
        print('Fecha de publicación: ', record[5])
        print('Categoría: ', record[6])
        print('Descripcion: ', record[7])
        print('Idioma: ', record[8])
        print('Número de páginas: ', record[9])
        print('Estanteria: ', record[10])
        print('Cantidad disponible: ', record[11])
    
    def show_book_header(self, header):
        print(header.center(100,'*'))
        print('-'*100)
    
    def show_book_midder(self):
        print('-'*100)

    def show_book_footer(self):
        print('*'*100)

    """
    ************************
    * Vistas para Usuarios *
    ************************
    """

    def users_menu(self):
        print('****************************************')
        print('****    xd     Menu Libros    xd    ****')
        print('****************************************')
        print('1. Agregar usuario')
        print('2. Mostrar usuario')
        print('3. Mostrar todos los usuarios')
        print('4. Mostrar usuarios de un codigo postal')
        print('5. Actualizar usuario')
        print('6. Borrar usuario')
        print('7. Regresar')

    def show_a_user(self, record):
        print('ID: ', record[0])
        print('Nombre(s): ', record[1])
        print('Apellido Paterno: ', record[2])
        print('Apellido Materno: ', record[3])
        print('Correo: ', record[4])
        print('Telefono: ', record[5])
        print('Calle: ', record[6])
        print('No. Exterior: ', record[7])
        print('No. Interior: ', record[8])
        print('Colonia: ', record[9])
        print('Código Postal: ', record[10])

    def show_a_user_brief(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1]+' '+record[2]+' '+record[3])
        print('Correo: ', record[4])
        print('Telefono: ', record[5])
        print('Direccion: ', record[6]+' '+record[7]+' '+record[8]+' '+record[9]+' '+record[10])
        
    def show_user_header(self, header):
        print(header.center(100,'*'))
        print('-'*100)
    
    def show_user_midder(self):
        print('-'*100)

    def show_user_footer(self):
        print('*'*100)

    
    """
    *************************
    * Vistas para Préstamos *
    *************************
    """ 

    def loans_menu(self):
        print('****************************************')
        print('****   xd    Menu Prestamos   xd    ****')
        print('****************************************')
        print('1. Realizar prestamo')
        print('2. Mostrar prestamos')
        print('3. Mostrar todos los prestamos')
        print('4. Mostrar prestamos de una fecha')
        print('5. Mostrar prestamos de un usuario')
        print('6. Actualizar datos de un prestamo')
        print('7. Agregar libros a un prestamo')
        print('8. Modificar libros de un prestamo')
        print('9. Borrar libros de un prestamo')
        print('10. Borrar prestamo')
        print('11. Regresar')

    def show_loan(self, record):
        print('ID: ', record[0])
        print('Fecha del prestamo: ', record[2])
        print('Vencimiento del prestamo: ', record[3])
        print('Estado del préstamo:', record[4])
        print('Datos del usuario '.center(81,'*'))
        self.show_a_user_brief(record[5:])

    def show_loan_header(self, header):
        print(header.center(81,'+'))
    
    def show_loan_midder(self):
        print('/'*81)

    def show_loan_footer(self):
        print('+'*81)

    """
    *************************************
    * Vistas para Detalles de Préstamos *
    *************************************
    """ 

    def show