from sql_connector import SQLConnector
from sql_queries import Query
from queries_executor import QueryExecutor
from csv_logger import CSVLogger
from utils.config_utils import Config
from utils.test_utils import TestData


def main():
    connection_data = Config("config_data.json")
    connection = SQLConnector(**connection_data.data)
    cursor = connection.connection()
    test_data = TestData("test_data.json")
    query = Query().get_query(test_data.get_data("query_number"))
    executor = QueryExecutor()
    result = executor.execute_query(cursor, query)
    logger = CSVLogger()
    logger.create_log(result)


if __name__ == "__main__":
    main()
