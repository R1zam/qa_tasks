class QueryExecutor:
    def execute_query(self, cursor, query):
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def print_result(self):
        pass
