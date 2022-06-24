from dependency_injector import providers, containers
from app.dataAccessLayer.DbConnection import DbConnection
from app.dataAccessLayer.FetchAndSaveDataLayer import FetchAndSaveDataLayer
from app.service.FetchAndSaveService import FetchAndSaveService


class DataLayer(containers.DeclarativeContainer):
    dbConnection=providers.Factory(DbConnection)
    fetchAndSaveDataLayer = providers.Factory(FetchAndSaveDataLayer, \
                                            dbConnection=dbConnection)

class ServiceLayer(containers.DeclarativeContainer):
    fetchAndSaveService = providers.Factory(FetchAndSaveService, \
                                        fetchAndSaveDataLayer = \
                                        DataLayer.fetchAndSaveDataLayer)