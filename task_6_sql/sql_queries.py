class Query:
    QUERIES = {1: """select pr.name , t.name , min(end_time - start_time) min_working_time
            from 
	            union_reporting.test t left join
		        union_reporting.project pr on t.project_id = pr.id
            group by t.name
            order by 1,2""",

               2: """select pr.name , count(distinct(t.name)) test_count
            from 
	            union_reporting.test t left join
		        union_reporting.project pr on t.project_id = pr.id
            group by pr.name
            order by 1,2""",

               3: """select pr.name,t.name,t.start_time date
                from 
	            union_reporting.test t left join
		        union_reporting.project pr on t.project_id = pr.id
                where t.start_time >= '2015-11-07'
                group by 2
                order by 1,2""",

               4: """select t.browser,count(t.browser) browsers
            from 
	          union_reporting.test t left join
		      union_reporting.project pr on t.project_id = pr.id
            where t.browser = 'chrome'
            union
            select t.browser,count(t.browser) browsers
            from 
                union_reporting.test t left join
                union_reporting.project pr on t.project_id = pr.id
            where t.browser = 'firefox'"""}

    def get_query(self, query_number):
        if query_number in range(1, 5):
            return self.QUERIES.get(query_number)
        else:
            raise ValueError("query number should be in range 1-4")
