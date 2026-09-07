import os

# Não existe settings.py de fábrica no FastAPI — este arquivo é o
# equivalente que você mesmo cria, lendo variáveis de ambiente.


class Settings:
    port: int = int(os.getenv("PORT", "3000"))


settings = Settings()
