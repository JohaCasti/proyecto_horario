# inicializa nuestra app
from projecto import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()