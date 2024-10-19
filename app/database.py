from pymongo import MongoClient

# Configuración de la conexión a MongoDB
MONGODB_URI = "mongodb://localhost:27017/btg_fondos"
client = MongoClient(MONGODB_URI)
db = client["btg_fondos"]

# Colecciones de la base de datos
funds_collection = db["funds"]
transactions_collection = db["transactions"]