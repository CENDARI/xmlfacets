from __future__ import unicode_literals
from django.conf import settings
from haystack.backends.elasticsearch_backend import ElasticsearchSearchBackend, ElasticsearchSearchEngine, ElasticsearchSearchQuery
from haystack.exceptions import MoreLikeThisError, FacetingError

#import pprint

class ConfigurableElasticsearchSearchBackend(ElasticsearchSearchBackend):

    def __init__(self, connection_alias, **connection_options):
        super(ConfigurableElasticsearchSearchBackend, self).__init__(
                                connection_alias, **connection_options)

    def build_search_kwargs(self, query_string, sort_by=None, start_offset=0, end_offset=None,
                            fields='', highlight=False, facets=None,
                            date_facets=None, query_facets=None,
                            narrow_queries=None, spelling_query=None,
                            within=None, dwithin=None, distance_point=None,
                            models=None, limit_to_registered_models=None,
                            result_class=None):
        kwargs = {}
        if facets is not None:
            for facet_fieldname, extra_options in facets.items():
                if 'precision' in extra_options:
                    del facets[facet_fieldname]
                    kwargs['aggregations'] = {
                        'low': {
                            'geohash_grid': {
                                'field': facet_fieldname,
                                'precision': extra_options['precision']
                            }
                        }
                    }
                    break

        search_kwargs = super(ConfigurableElasticsearchSearchBackend, self).build_search_kwargs(
            query_string, sort_by, start_offset, end_offset,
            fields, highlight, facets,
            date_facets, query_facets,
            narrow_queries, spelling_query,
            within, dwithin, distance_point,
            models, limit_to_registered_models,
            result_class)
        search_kwargs.update(kwargs)
#        pprint.pprint(search_kwargs)
        return search_kwargs

    def _process_results(self, raw_results, highlight=False,
                         result_class=None, distance_point=None,
                         geo_sort=False):
#        if 'aggregations' in raw_results:
#            pprint.pprint(raw_results['aggregations'])
        results = super(ConfigurableElasticsearchSearchBackend, self)._process_results(raw_results, highlight, result_class, distance_point, geo_sort)
        return results

class ConfigurableElasticsearchSearchQuery(ElasticsearchSearchQuery):
    def add_field_aggregations(self, field, precision):
        if precision < 1 or precision > 12:
            raise FacetingError("The precision ('%d') must be in [1,12]" % (precision))
        aggregations = {
            'aggregations': {
                'low': {
                    'geohash_grid': {
                        'field': 'location',
                        'precision': 3
                    }
                }
            }
        }
        search_kwargs.update(aggregations)


class ConfigurableElasticsearchSearchEngine(ElasticsearchSearchEngine):
    backend = ConfigurableElasticsearchSearchBackend
    query = ConfigurableElasticsearchSearchQuery
