from elasticsearch_dsl import Q


def chain_search(search_obj,
                 query=None,
                 query_type_or_q='match',
                 source_kwargs=None,
                 sort_args=None,
                 sub_searching_attr='',
                 sub_query=None,
                 init_res_num=300):

    if query is None:
        query = {}
    if sort_args is None:
        sort_args = {}
    if source_kwargs is None:
        source_kwargs = {}
    if sub_query is None:
        sub_query = {}

    main_search = search_obj.query(query_type_or_q, **query). \
                             source(**source_kwargs). \
                             sort(sort_args)

    if init_res_num:
        main_search = main_search[:init_res_num]

    if sub_searching_attr:
        main_search = main_search.execute()
        sub_search_res = []
        for hit in main_search.hits:
            ss_attr_value = getattr(hit, sub_searching_attr)
            if (not sub_query) and ss_attr_value.isdigit():
                cur_sub_query = {'filter': Q('term', **{sub_searching_attr: ss_attr_value})}
            else:
                cur_sub_query = sub_query

            if cur_sub_query:
                sub_search_res += chain_search(query=cur_sub_query,
                                               search_obj=search_obj,
                                               query_type_or_q='constant_score',
                                               init_res_num=None)

        return sub_search_res

    else:
        return main_search
