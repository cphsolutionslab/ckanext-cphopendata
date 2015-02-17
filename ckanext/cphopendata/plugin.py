import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


def latest_datasets():
    '''Return a sorted list of the latest datasets.'''

    datasets = toolkit.get_action('package_search')(
        data_dict={'rows': 10, 'sort': 'metadata_created desc' })

    return datasets['results']


def most_popular_datasets():
    '''Return a sorted list of the most popular datasets.'''

    datasets = toolkit.get_action('package_search')(
        data_dict={'rows': 10, 'sort': 'views_recent desc' })

    return datasets['results']


class CPHOpenDataPlugin(plugins.SingletonPlugin):
    '''cph.opendata.dk theme plugin.

    '''
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'cphopendata')

    def get_helpers(self):
        return {'cphopendata_latest_datasets': latest_datasets,
                'cphopendata_most_popular_datasets': most_popular_datasets}

