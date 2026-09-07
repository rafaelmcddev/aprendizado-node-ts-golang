import os


# Sem settings.py de fábrica: você mesmo cria essa classe/config
# e injeta na aplicação em create_app().
class Config:
    PORT = int(os.getenv("PORT", 3000))
