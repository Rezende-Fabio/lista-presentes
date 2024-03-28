from flask_login import LoginManager


def init_app(app):
    login_manager = LoginManager()
    login_manager.login_view = 'errosBlue.unauthorizedRoute'
    login_manager.login_message = False
    login_manager.init_app(app)
    
    from ..models.Usuario import Usuario
    @login_manager.user_loader
    def load_user(id):
        return Usuario.query.filter(Usuario.id==id).first()