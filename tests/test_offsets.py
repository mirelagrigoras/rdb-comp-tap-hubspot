import unittest
import logging
import singer
import rdb_comp_tap_hubspot
import singer.bookmarks
from .utils import *

LOGGER = singer.get_logger()

def set_offset_with_exception(state, tap_stream_id, offset_key, offset_value):
    LOGGER.info("set_offset_with_exception: {}".format(utils.caught_state))
    utils.caught_state = singer.bookmarks.set_offset(state, tap_stream_id, offset_key, offset_value)
    raise Exception("simulated")

class Offsets(unittest.TestCase):
    def setUp(self):
        utils.verify_environment_vars()
        utils.seed_rdb_comp_tap_hubspot_config()
        singer.write_bookmark = utils.our_write_bookmark
        singer.write_state    = utils.our_write_state
        singer.write_record   = utils.our_write_record
        singer.write_schema   = utils.our_write_schema
        singer.set_offset     = set_offset_with_exception

    #NB> test accounts must have > 1 companies for this to work
    def sync_companies(self):
        simulated_exception = None
        STATE = utils.get_clear_state()
        catalog = {'stream_alias' : 'hubspot_companies'}

        #change count = 1
        rdb_comp_tap_hubspot.default_company_params['limit'] = 1

        try:
            STATE = rdb_comp_tap_hubspot.sync_companies(STATE, catalog)
        except Exception as ex:
            simulated_exception = ex
            # logging.exception('strange')

        self.assertIsNot(simulated_exception, None)


        self.assertEqual(set(utils.caught_records.keys()), {'companies', 'hubspot_contacts_by_company'})

        #should only emit 1 company record because of the limit
        self.assertEqual(len(utils.caught_records['companies']), 1)
        self.assertGreater(len(utils.caught_records['hubspot_contacts_by_company']), 0)

        #offset should be set in state
        LOGGER.info("utils.caught_state: {}".format(utils.caught_state))
        self.assertNotEqual(utils.caught_state['bookmarks']['companies']['offset'], {})

        #no bookmark though
        self.assertEqual(utils.caught_state['bookmarks']['companies']['hs_lastmodifieddate'], None)

        #change count back to 250
        rdb_comp_tap_hubspot.default_company_params['limit'] = 250

        #call do_sync and verify:
        #    1)sync_companies is called first
        #    2)previous retrieved record is not retrieved again
