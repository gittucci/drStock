from pydantic import BaseSettings, Field
import logging
from logging.handlers import RotatingFileHandler

# LOGGER - - - - - - - - - - - - - - - - - - - -

# Configuração avançada do Logger
logger = logging.getLogger(__name__)

# Definindo o nível do logger
logger.setLevel(logging.INFO)  # Pode ser DEBUG, INFO, WARNING, ERROR, CRITICAL

# Formatando a saída do log
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

# Console Handler para exibir os logs no console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# File Handler para salvar os logs em um arquivo com rotação
file_handler = RotatingFileHandler(
    "logs/api_logs.log", maxBytes=10 * 1024 * 1024, backupCount=3
)  # Max 10MB por arquivo, mantendo até 3 backups
file_handler.setFormatter(formatter)

# Adicionando handlers ao logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Exemplo de log
logger.info("Logger configurado com sucesso!")