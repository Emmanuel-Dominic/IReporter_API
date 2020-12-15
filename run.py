from api.app import app

# app.config.from_object("api.models.config.app_config['development']")
app.config.from_object("api.models.config.DevelopmentConfig")

if __name__ == '__main__':
    app.run()
