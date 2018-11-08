# -*- coding: utf-8 -*-

from functools import lru_cache

import geocoder
from six import string_types


class GeocoderPipeline(object):

    def __init__(self, settings) -> None:
        super().__init__()

        self.provider = getattr(geocoder, settings['GEOCODER_PROVIDER'])
        self.kwargs = settings.get('GEOCODER_KWARGS', {})

        self.address_field = settings.get('GEOCODER_ADDRESS_FIELD', 'address')
        self.result_field = settings.get('GEOCODER_RESULT_FIELD', 'location')
        self.result_format = settings.get('GEOCODER_RESULT_FORMAT', 'string')

    @classmethod
    def from_crawler(cls, crawler):
        if 'GEOCODER_PROVIDER' not in crawler.settings:
            raise ValueError('GEOCODER_PROVIDER is not defined')

        return cls(crawler.settings)

    @lru_cache(maxsize=1024)
    def get_location(self, address):
        result = self.provider(address, **self.kwargs)
        if result.ok:
            if self.result_format == 'string':
                return '%s,%s' % (result.lat, result.lng)
            if self.result_format == 'array':
                return [result.lat, result.lng]
            if self.result_format == 'object':
                return {'lat': result.lat, 'lng': result.lng}
            else:
                raise ValueError('Unknown result format: %s' % self.result_format)

    def process_item(self, item, spider):
        address = item[self.address_field]
        if isinstance(address, string_types):
            item[self.result_field] = self.get_location(address)

        return item

