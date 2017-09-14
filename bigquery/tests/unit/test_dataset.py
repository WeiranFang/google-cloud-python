# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import mock


class TestAccessEntry(unittest.TestCase):

    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.dataset import AccessEntry

        return AccessEntry

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_defaults(self):
        entry = self._make_one('OWNER', 'userByEmail', 'phred@example.com')
        self.assertEqual(entry.role, 'OWNER')
        self.assertEqual(entry.entity_type, 'userByEmail')
        self.assertEqual(entry.entity_id, 'phred@example.com')

    def test_ctor_bad_entity_type(self):
        with self.assertRaises(ValueError):
            self._make_one(None, 'unknown', None)

    def test_ctor_view_with_role(self):
        role = 'READER'
        entity_type = 'view'
        with self.assertRaises(ValueError):
            self._make_one(role, entity_type, None)

    def test_ctor_view_success(self):
        role = None
        entity_type = 'view'
        entity_id = object()
        entry = self._make_one(role, entity_type, entity_id)
        self.assertEqual(entry.role, role)
        self.assertEqual(entry.entity_type, entity_type)
        self.assertEqual(entry.entity_id, entity_id)

    def test_ctor_nonview_without_role(self):
        role = None
        entity_type = 'userByEmail'
        with self.assertRaises(ValueError):
            self._make_one(role, entity_type, None)

    def test___eq___role_mismatch(self):
        entry = self._make_one('OWNER', 'userByEmail', 'phred@example.com')
        other = self._make_one('WRITER', 'userByEmail', 'phred@example.com')
        self.assertNotEqual(entry, other)

    def test___eq___entity_type_mismatch(self):
        entry = self._make_one('OWNER', 'userByEmail', 'phred@example.com')
        other = self._make_one('OWNER', 'groupByEmail', 'phred@example.com')
        self.assertNotEqual(entry, other)

    def test___eq___entity_id_mismatch(self):
        entry = self._make_one('OWNER', 'userByEmail', 'phred@example.com')
        other = self._make_one('OWNER', 'userByEmail', 'bharney@example.com')
        self.assertNotEqual(entry, other)

    def test___eq___hit(self):
        entry = self._make_one('OWNER', 'userByEmail', 'phred@example.com')
        other = self._make_one('OWNER', 'userByEmail', 'phred@example.com')
        self.assertEqual(entry, other)

    def test__eq___type_mismatch(self):
        entry = self._make_one('OWNER', 'userByEmail', 'silly@example.com')
        self.assertNotEqual(entry, object())
        self.assertEqual(entry, mock.ANY)


class TestDatasetReference(unittest.TestCase):

    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.dataset import DatasetReference

        return DatasetReference

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_defaults(self):
        dataset_ref = self._make_one('some-project-1', 'dataset_1')
        self.assertEqual(dataset_ref.project_id, 'some-project-1')
        self.assertEqual(dataset_ref.dataset_id, 'dataset_1')

    def test_table(self):
        dataset_ref = self._make_one('some-project-1', 'dataset_1')
        table_ref = dataset_ref.table('table_1')
        self.assertIs(table_ref.dataset, dataset_ref)
        self.assertEqual(table_ref.table_id, 'table_1')


class TestDataset(unittest.TestCase):
    PROJECT = 'project'
    DS_ID = 'dataset-id'

    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.dataset import Dataset

        return Dataset

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def _setUpConstants(self):
        import datetime
        from google.cloud._helpers import UTC

        self.WHEN_TS = 1437767599.006
        self.WHEN = datetime.datetime.utcfromtimestamp(self.WHEN_TS).replace(
            tzinfo=UTC)
        self.ETAG = 'ETAG'
        self.DS_FULL_ID = '%s:%s' % (self.PROJECT, self.DS_ID)
        self.RESOURCE_URL = 'http://example.com/path/to/resource'

    def _makeResource(self):
        self._setUpConstants()
        USER_EMAIL = 'phred@example.com'
        GROUP_EMAIL = 'group-name@lists.example.com'
        return {
            'creationTime': self.WHEN_TS * 1000,
            'datasetReference':
                {'projectId': self.PROJECT, 'datasetId': self.DS_ID},
            'etag': self.ETAG,
            'id': self.DS_FULL_ID,
            'lastModifiedTime': self.WHEN_TS * 1000,
            'location': 'US',
            'selfLink': self.RESOURCE_URL,
            'access': [
                {'role': 'OWNER', 'userByEmail': USER_EMAIL},
                {'role': 'OWNER', 'groupByEmail': GROUP_EMAIL},
                {'role': 'WRITER', 'specialGroup': 'projectWriters'},
                {'role': 'READER', 'specialGroup': 'projectReaders'}],
        }

    def _verify_access_entry(self, access_entries, resource):
        r_entries = []
        for r_entry in resource['access']:
            role = r_entry.pop('role')
            for entity_type, entity_id in sorted(r_entry.items()):
                r_entries.append({
                    'role': role,
                    'entity_type': entity_type,
                    'entity_id': entity_id})

        self.assertEqual(len(access_entries), len(r_entries))
        for a_entry, r_entry in zip(access_entries, r_entries):
            self.assertEqual(a_entry.role, r_entry['role'])
            self.assertEqual(a_entry.entity_type, r_entry['entity_type'])
            self.assertEqual(a_entry.entity_id, r_entry['entity_id'])

    def _verify_readonly_resource_properties(self, dataset, resource):

        self.assertEqual(dataset.dataset_id, self.DS_ID)

        if 'creationTime' in resource:
            self.assertEqual(dataset.created, self.WHEN)
        else:
            self.assertIsNone(dataset.created)
        if 'etag' in resource:
            self.assertEqual(dataset.etag, self.ETAG)
        else:
            self.assertIsNone(dataset.etag)
        if 'lastModifiedTime' in resource:
            self.assertEqual(dataset.modified, self.WHEN)
        else:
            self.assertIsNone(dataset.modified)
        if 'selfLink' in resource:
            self.assertEqual(dataset.self_link, self.RESOURCE_URL)
        else:
            self.assertIsNone(dataset.self_link)

    def _verify_resource_properties(self, dataset, resource):

        self._verify_readonly_resource_properties(dataset, resource)

        if 'defaultTableExpirationMs' in resource:
            self.assertEqual(dataset.default_table_expiration_ms,
                             int(resource.get('defaultTableExpirationMs')))
        else:
            self.assertIsNone(dataset.default_table_expiration_ms)
        self.assertEqual(dataset.description, resource.get('description'))
        self.assertEqual(dataset.friendly_name, resource.get('friendlyName'))
        self.assertEqual(dataset.location, resource.get('location'))

        if 'access' in resource:
            self._verify_access_entry(dataset.access_entries, resource)
        else:
            self.assertEqual(dataset.access_entries, [])

    def test_ctor_defaults(self):
        client = _Client(self.PROJECT)
        dataset = self._make_one(self.DS_ID, client)
        self.assertEqual(dataset.dataset_id, self.DS_ID)
        self.assertIs(dataset._client, client)
        self.assertEqual(dataset.project, client.project)
        self.assertEqual(
            dataset.path,
            '/projects/%s/datasets/%s' % (self.PROJECT, self.DS_ID))
        self.assertEqual(dataset.access_entries, [])

        self.assertIsNone(dataset.created)
        self.assertIsNone(dataset.full_dataset_id)
        self.assertIsNone(dataset.etag)
        self.assertIsNone(dataset.modified)
        self.assertIsNone(dataset.self_link)

        self.assertIsNone(dataset.default_table_expiration_ms)
        self.assertIsNone(dataset.description)
        self.assertIsNone(dataset.friendly_name)
        self.assertIsNone(dataset.location)

    def test_ctor_explicit(self):
        from google.cloud.bigquery.dataset import AccessEntry

        phred = AccessEntry('OWNER', 'userByEmail', 'phred@example.com')
        bharney = AccessEntry('OWNER', 'userByEmail', 'bharney@example.com')
        entries = [phred, bharney]
        OTHER_PROJECT = 'foo-bar-123'
        client = _Client(self.PROJECT)
        dataset = self._make_one(self.DS_ID, client,
                                 access_entries=entries,
                                 project=OTHER_PROJECT)
        self.assertEqual(dataset.dataset_id, self.DS_ID)
        self.assertIs(dataset._client, client)
        self.assertEqual(dataset.project, OTHER_PROJECT)
        self.assertEqual(
            dataset.path,
            '/projects/%s/datasets/%s' % (OTHER_PROJECT, self.DS_ID))
        self.assertEqual(dataset.access_entries, entries)

        self.assertIsNone(dataset.created)
        self.assertIsNone(dataset.full_dataset_id)
        self.assertIsNone(dataset.etag)
        self.assertIsNone(dataset.modified)
        self.assertIsNone(dataset.self_link)

        self.assertIsNone(dataset.default_table_expiration_ms)
        self.assertIsNone(dataset.description)
        self.assertIsNone(dataset.friendly_name)
        self.assertIsNone(dataset.location)

    def test_access_entries_setter_non_list(self):
        client = _Client(self.PROJECT)
        dataset = self._make_one(self.DS_ID, client)
        with self.assertRaises(TypeError):
            dataset.access_entries = object()

    def test_access_entries_setter_invalid_field(self):
        from google.cloud.bigquery.dataset import AccessEntry

        client = _Client(self.PROJECT)
        dataset = self._make_one(self.DS_ID, client)
        phred = AccessEntry('OWNER', 'userByEmail', 'phred@example.com')
        with self.assertRaises(ValueError):
            dataset.access_entries = [phred, object()]

    def test_access_entries_setter(self):
        from google.cloud.bigquery.dataset import AccessEntry

        client = _Client(self.PROJECT)
        dataset = self._make_one(self.DS_ID, client)
        phred = AccessEntry('OWNER', 'userByEmail', 'phred@example.com')
        bharney = AccessEntry('OWNER', 'userByEmail', 'bharney@example.com')
        dataset.access_entries = [phred, bharney]
        self.assertEqual(dataset.access_entries, [phred, bharney])

    def test_default_table_expiration_ms_setter_bad_value(self):
        client = _Client(self.PROJECT)
        dataset = self._make_one(self.DS_ID, client)
        with self.assertRaises(ValueError):
            dataset.default_table_expiration_ms = 'bogus'

    def test_default_table_expiration_ms_setter(self):
        client = _Client(self.PROJECT)
        dataset = self._make_one(self.DS_ID, client)
        dataset.default_table_expiration_ms = 12345
        self.assertEqual(dataset.default_table_expiration_ms, 12345)

    def test_description_setter_bad_value(self):
        client = _Client(self.PROJECT)
        dataset = self._make_one(self.DS_ID, client)
        with self.assertRaises(ValueError):
            dataset.description = 12345

    def test_description_setter(self):
        client = _Client(self.PROJECT)
        dataset = self._make_one(self.DS_ID, client)
        dataset.description = 'DESCRIPTION'
        self.assertEqual(dataset.description, 'DESCRIPTION')

    def test_friendly_name_setter_bad_value(self):
        client = _Client(self.PROJECT)
        dataset = self._make_one(self.DS_ID, client)
        with self.assertRaises(ValueError):
            dataset.friendly_name = 12345

    def test_friendly_name_setter(self):
        client = _Client(self.PROJECT)
        dataset = self._make_one(self.DS_ID, client)
        dataset.friendly_name = 'FRIENDLY'
        self.assertEqual(dataset.friendly_name, 'FRIENDLY')

    def test_location_setter_bad_value(self):
        client = _Client(self.PROJECT)
        dataset = self._make_one(self.DS_ID, client)
        with self.assertRaises(ValueError):
            dataset.location = 12345

    def test_location_setter(self):
        client = _Client(self.PROJECT)
        dataset = self._make_one(self.DS_ID, client)
        dataset.location = 'LOCATION'
        self.assertEqual(dataset.location, 'LOCATION')

    def test_from_api_repr_missing_identity(self):
        self._setUpConstants()
        client = _Client(self.PROJECT)
        RESOURCE = {}
        klass = self._get_target_class()
        with self.assertRaises(KeyError):
            klass.from_api_repr(RESOURCE, client=client)

    def test_from_api_repr_bare(self):
        self._setUpConstants()
        client = _Client(self.PROJECT)
        RESOURCE = {
            'id': '%s:%s' % (self.PROJECT, self.DS_ID),
            'datasetReference': {
                'projectId': self.PROJECT,
                'datasetId': self.DS_ID,
            }
        }
        klass = self._get_target_class()
        dataset = klass.from_api_repr(RESOURCE, client=client)
        self.assertIs(dataset._client, client)
        self._verify_resource_properties(dataset, RESOURCE)

    def test_from_api_repr_w_properties(self):
        client = _Client(self.PROJECT)
        RESOURCE = self._makeResource()
        klass = self._get_target_class()
        dataset = klass.from_api_repr(RESOURCE, client=client)
        self.assertIs(dataset._client, client)
        self._verify_resource_properties(dataset, RESOURCE)

    def test__parse_access_entries_w_unknown_entity_type(self):
        ACCESS = [
            {'role': 'READER', 'unknown': 'UNKNOWN'},
        ]
        client = _Client(self.PROJECT)
        dataset = self._make_one(self.DS_ID, client=client)
        with self.assertRaises(ValueError):
            dataset._parse_access_entries(ACCESS)

    def test__parse_access_entries_w_extra_keys(self):
        USER_EMAIL = 'phred@example.com'
        ACCESS = [
            {
                'role': 'READER',
                'specialGroup': 'projectReaders',
                'userByEmail': USER_EMAIL,
            },
        ]
        client = _Client(self.PROJECT)
        dataset = self._make_one(self.DS_ID, client=client)
        with self.assertRaises(ValueError):
            dataset._parse_access_entries(ACCESS)

    def test_create_w_bound_client(self):
        PATH = 'projects/%s/datasets' % self.PROJECT
        RESOURCE = self._makeResource()
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        dataset = self._make_one(self.DS_ID, client=client)

        dataset.create()

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req['method'], 'POST')
        self.assertEqual(req['path'], '/%s' % PATH)
        SENT = {
            'datasetReference':
                {'projectId': self.PROJECT, 'datasetId': self.DS_ID},
        }
        self.assertEqual(req['data'], SENT)
        self._verify_resource_properties(dataset, RESOURCE)

    def test_create_w_alternate_client(self):
        from google.cloud.bigquery.dataset import AccessEntry

        PATH = 'projects/%s/datasets' % self.PROJECT
        USER_EMAIL = 'phred@example.com'
        GROUP_EMAIL = 'group-name@lists.example.com'
        DESCRIPTION = 'DESCRIPTION'
        TITLE = 'TITLE'
        RESOURCE = self._makeResource()
        RESOURCE['description'] = DESCRIPTION
        RESOURCE['friendlyName'] = TITLE
        conn1 = _Connection()
        CLIENT1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection(RESOURCE)
        CLIENT2 = _Client(project=self.PROJECT, connection=conn2)
        dataset = self._make_one(self.DS_ID, client=CLIENT1)
        dataset.friendly_name = TITLE
        dataset.description = DESCRIPTION
        VIEW = {
            'projectId': 'my-proj',
            'datasetId': 'starry-skies',
            'tableId': 'northern-hemisphere',
        }
        dataset.access_entries = [
            AccessEntry('OWNER', 'userByEmail', USER_EMAIL),
            AccessEntry('OWNER', 'groupByEmail', GROUP_EMAIL),
            AccessEntry('READER', 'domain', 'foo.com'),
            AccessEntry('READER', 'specialGroup', 'projectReaders'),
            AccessEntry('WRITER', 'specialGroup', 'projectWriters'),
            AccessEntry(None, 'view', VIEW),
        ]

        dataset.create(client=CLIENT2)

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req['method'], 'POST')
        self.assertEqual(req['path'], '/%s' % PATH)
        SENT = {
            'datasetReference': {
                'projectId': self.PROJECT,
                'datasetId': self.DS_ID,
            },
            'description': DESCRIPTION,
            'friendlyName': TITLE,
            'access': [
                {'role': 'OWNER', 'userByEmail': USER_EMAIL},
                {'role': 'OWNER', 'groupByEmail': GROUP_EMAIL},
                {'role': 'READER', 'domain': 'foo.com'},
                {'role': 'READER', 'specialGroup': 'projectReaders'},
                {'role': 'WRITER', 'specialGroup': 'projectWriters'},
                {'view': VIEW},
            ],
        }
        self.assertEqual(req['data'], SENT)
        self._verify_resource_properties(dataset, RESOURCE)

    def test_create_w_missing_output_properties(self):
        # In the wild, the resource returned from 'dataset.create' sometimes
        # lacks 'creationTime' / 'lastModifiedTime'
        PATH = 'projects/%s/datasets' % (self.PROJECT,)
        RESOURCE = self._makeResource()
        del RESOURCE['creationTime']
        del RESOURCE['lastModifiedTime']
        self.WHEN = None
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        dataset = self._make_one(self.DS_ID, client=client)

        dataset.create()

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req['method'], 'POST')
        self.assertEqual(req['path'], '/%s' % PATH)
        SENT = {
            'datasetReference':
                {'projectId': self.PROJECT, 'datasetId': self.DS_ID},
        }
        self.assertEqual(req['data'], SENT)
        self._verify_resource_properties(dataset, RESOURCE)

    def test_exists_miss_w_bound_client(self):
        PATH = 'projects/%s/datasets/%s' % (self.PROJECT, self.DS_ID)
        conn = _Connection()
        client = _Client(project=self.PROJECT, connection=conn)
        dataset = self._make_one(self.DS_ID, client=client)

        self.assertFalse(dataset.exists())

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req['method'], 'GET')
        self.assertEqual(req['path'], '/%s' % PATH)
        self.assertEqual(req['query_params'], {'fields': 'id'})

    def test_exists_hit_w_alternate_client(self):
        PATH = 'projects/%s/datasets/%s' % (self.PROJECT, self.DS_ID)
        conn1 = _Connection()
        CLIENT1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection({})
        CLIENT2 = _Client(project=self.PROJECT, connection=conn2)
        dataset = self._make_one(self.DS_ID, client=CLIENT1)

        self.assertTrue(dataset.exists(client=CLIENT2))

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req['method'], 'GET')
        self.assertEqual(req['path'], '/%s' % PATH)
        self.assertEqual(req['query_params'], {'fields': 'id'})

    def test_reload_w_bound_client(self):
        PATH = 'projects/%s/datasets/%s' % (self.PROJECT, self.DS_ID)
        RESOURCE = self._makeResource()
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        dataset = self._make_one(self.DS_ID, client=client)

        dataset.reload()

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req['method'], 'GET')
        self.assertEqual(req['path'], '/%s' % PATH)
        self._verify_resource_properties(dataset, RESOURCE)

    def test_reload_w_alternate_client(self):
        PATH = 'projects/%s/datasets/%s' % (self.PROJECT, self.DS_ID)
        RESOURCE = self._makeResource()
        conn1 = _Connection()
        CLIENT1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection(RESOURCE)
        CLIENT2 = _Client(project=self.PROJECT, connection=conn2)
        dataset = self._make_one(self.DS_ID, client=CLIENT1)

        dataset.reload(client=CLIENT2)

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req['method'], 'GET')
        self.assertEqual(req['path'], '/%s' % PATH)
        self._verify_resource_properties(dataset, RESOURCE)

    def test_patch_w_invalid_expiration(self):
        RESOURCE = self._makeResource()
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        dataset = self._make_one(self.DS_ID, client=client)

        with self.assertRaises(ValueError):
            dataset.patch(default_table_expiration_ms='BOGUS')

    def test_patch_w_bound_client(self):
        PATH = 'projects/%s/datasets/%s' % (self.PROJECT, self.DS_ID)
        DESCRIPTION = 'DESCRIPTION'
        TITLE = 'TITLE'
        RESOURCE = self._makeResource()
        RESOURCE['description'] = DESCRIPTION
        RESOURCE['friendlyName'] = TITLE
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        dataset = self._make_one(self.DS_ID, client=client)

        dataset.patch(description=DESCRIPTION, friendly_name=TITLE)

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req['method'], 'PATCH')
        SENT = {
            'description': DESCRIPTION,
            'friendlyName': TITLE,
        }
        self.assertEqual(req['data'], SENT)
        self.assertEqual(req['path'], '/%s' % PATH)
        self._verify_resource_properties(dataset, RESOURCE)

    def test_patch_w_alternate_client(self):
        PATH = 'projects/%s/datasets/%s' % (self.PROJECT, self.DS_ID)
        DEF_TABLE_EXP = 12345
        LOCATION = 'EU'
        RESOURCE = self._makeResource()
        RESOURCE['defaultTableExpirationMs'] = str(DEF_TABLE_EXP)
        RESOURCE['location'] = LOCATION
        conn1 = _Connection()
        CLIENT1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection(RESOURCE)
        CLIENT2 = _Client(project=self.PROJECT, connection=conn2)
        dataset = self._make_one(self.DS_ID, client=CLIENT1)

        dataset.patch(client=CLIENT2,
                      default_table_expiration_ms=DEF_TABLE_EXP,
                      location=LOCATION)

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req['method'], 'PATCH')
        self.assertEqual(req['path'], '/%s' % PATH)
        SENT = {
            'defaultTableExpirationMs': DEF_TABLE_EXP,
            'location': LOCATION,
        }
        self.assertEqual(req['data'], SENT)
        self._verify_resource_properties(dataset, RESOURCE)

    def test_update_w_bound_client(self):
        PATH = 'projects/%s/datasets/%s' % (self.PROJECT, self.DS_ID)
        DESCRIPTION = 'DESCRIPTION'
        TITLE = 'TITLE'
        RESOURCE = self._makeResource()
        RESOURCE['description'] = DESCRIPTION
        RESOURCE['friendlyName'] = TITLE
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        dataset = self._make_one(self.DS_ID, client=client)
        dataset.description = DESCRIPTION
        dataset.friendly_name = TITLE

        dataset.update()

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req['method'], 'PUT')
        SENT = {
            'datasetReference':
                {'projectId': self.PROJECT, 'datasetId': self.DS_ID},
            'description': DESCRIPTION,
            'friendlyName': TITLE,
        }
        self.assertEqual(req['data'], SENT)
        self.assertEqual(req['path'], '/%s' % PATH)
        self._verify_resource_properties(dataset, RESOURCE)

    def test_update_w_alternate_client(self):
        PATH = 'projects/%s/datasets/%s' % (self.PROJECT, self.DS_ID)
        DEF_TABLE_EXP = 12345
        LOCATION = 'EU'
        RESOURCE = self._makeResource()
        RESOURCE['defaultTableExpirationMs'] = 12345
        RESOURCE['location'] = LOCATION
        conn1 = _Connection()
        CLIENT1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection(RESOURCE)
        CLIENT2 = _Client(project=self.PROJECT, connection=conn2)
        dataset = self._make_one(self.DS_ID, client=CLIENT1)
        dataset.default_table_expiration_ms = DEF_TABLE_EXP
        dataset.location = LOCATION

        dataset.update(client=CLIENT2)

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req['method'], 'PUT')
        self.assertEqual(req['path'], '/%s' % PATH)
        SENT = {
            'datasetReference':
                {'projectId': self.PROJECT, 'datasetId': self.DS_ID},
            'defaultTableExpirationMs': 12345,
            'location': 'EU',
        }
        self.assertEqual(req['data'], SENT)
        self._verify_resource_properties(dataset, RESOURCE)

    def test_delete_w_bound_client(self):
        PATH = 'projects/%s/datasets/%s' % (self.PROJECT, self.DS_ID)
        conn = _Connection({})
        client = _Client(project=self.PROJECT, connection=conn)
        dataset = self._make_one(self.DS_ID, client=client)

        dataset.delete()

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req['method'], 'DELETE')
        self.assertEqual(req['path'], '/%s' % PATH)

    def test_delete_w_alternate_client(self):
        PATH = 'projects/%s/datasets/%s' % (self.PROJECT, self.DS_ID)
        conn1 = _Connection()
        CLIENT1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection({})
        CLIENT2 = _Client(project=self.PROJECT, connection=conn2)
        dataset = self._make_one(self.DS_ID, client=CLIENT1)

        dataset.delete(client=CLIENT2)

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req['method'], 'DELETE')
        self.assertEqual(req['path'], '/%s' % PATH)

    def test_list_tables_empty(self):
        import six

        conn = _Connection({})
        client = _Client(project=self.PROJECT, connection=conn)
        dataset = self._make_one(self.DS_ID, client=client)

        iterator = dataset.list_tables()
        self.assertIs(iterator.dataset, dataset)
        page = six.next(iterator.pages)
        tables = list(page)
        token = iterator.next_page_token

        self.assertEqual(tables, [])
        self.assertIsNone(token)
        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req['method'], 'GET')
        PATH = 'projects/%s/datasets/%s/tables' % (self.PROJECT, self.DS_ID)
        self.assertEqual(req['path'], '/%s' % PATH)

    def test_list_tables_defaults(self):
        import six
        from google.cloud.bigquery.table import Table

        TABLE_1 = 'table_one'
        TABLE_2 = 'table_two'
        PATH = 'projects/%s/datasets/%s/tables' % (self.PROJECT, self.DS_ID)
        TOKEN = 'TOKEN'
        DATA = {
            'nextPageToken': TOKEN,
            'tables': [
                {'kind': 'bigquery#table',
                 'id': '%s:%s.%s' % (self.PROJECT, self.DS_ID, TABLE_1),
                 'tableReference': {'tableId': TABLE_1,
                                    'datasetId': self.DS_ID,
                                    'projectId': self.PROJECT},
                 'type': 'TABLE'},
                {'kind': 'bigquery#table',
                 'id': '%s:%s.%s' % (self.PROJECT, self.DS_ID, TABLE_2),
                 'tableReference': {'tableId': TABLE_2,
                                    'datasetId': self.DS_ID,
                                    'projectId': self.PROJECT},
                 'type': 'TABLE'},
            ]
        }

        conn = _Connection(DATA)
        client = _Client(project=self.PROJECT, connection=conn)
        dataset = self._make_one(self.DS_ID, client=client)

        iterator = dataset.list_tables()
        self.assertIs(iterator.dataset, dataset)
        page = six.next(iterator.pages)
        tables = list(page)
        token = iterator.next_page_token

        self.assertEqual(len(tables), len(DATA['tables']))
        for found, expected in zip(tables, DATA['tables']):
            self.assertIsInstance(found, Table)
            self.assertEqual(found.full_table_id, expected['id'])
            self.assertEqual(found.table_type, expected['type'])
        self.assertEqual(token, TOKEN)

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req['method'], 'GET')
        self.assertEqual(req['path'], '/%s' % PATH)

    def test_list_tables_explicit(self):
        import six
        from google.cloud.bigquery.table import Table

        TABLE_1 = 'table_one'
        TABLE_2 = 'table_two'
        PATH = 'projects/%s/datasets/%s/tables' % (self.PROJECT, self.DS_ID)
        TOKEN = 'TOKEN'
        DATA = {
            'tables': [
                {'kind': 'bigquery#dataset',
                 'id': '%s:%s.%s' % (self.PROJECT, self.DS_ID, TABLE_1),
                 'tableReference': {'tableId': TABLE_1,
                                    'datasetId': self.DS_ID,
                                    'projectId': self.PROJECT},
                 'type': 'TABLE'},
                {'kind': 'bigquery#dataset',
                 'id': '%s:%s.%s' % (self.PROJECT, self.DS_ID, TABLE_2),
                 'tableReference': {'tableId': TABLE_2,
                                    'datasetId': self.DS_ID,
                                    'projectId': self.PROJECT},
                 'type': 'TABLE'},
            ]
        }

        conn = _Connection(DATA)
        client = _Client(project=self.PROJECT, connection=conn)
        dataset = self._make_one(self.DS_ID, client=client)

        iterator = dataset.list_tables(max_results=3, page_token=TOKEN)
        self.assertIs(iterator.dataset, dataset)
        page = six.next(iterator.pages)
        tables = list(page)
        token = iterator.next_page_token

        self.assertEqual(len(tables), len(DATA['tables']))
        for found, expected in zip(tables, DATA['tables']):
            self.assertIsInstance(found, Table)
            self.assertEqual(found.full_table_id, expected['id'])
            self.assertEqual(found.table_type, expected['type'])
        self.assertIsNone(token)

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req['method'], 'GET')
        self.assertEqual(req['path'], '/%s' % PATH)
        self.assertEqual(req['query_params'],
                         {'maxResults': 3, 'pageToken': TOKEN})

    def test_table_wo_schema(self):
        from google.cloud.bigquery.table import Table

        conn = _Connection({})
        client = _Client(project=self.PROJECT, connection=conn)
        dataset = self._make_one(self.DS_ID, client=client)
        table = dataset.table('table_id')
        self.assertIsInstance(table, Table)
        self.assertEqual(table.table_id, 'table_id')
        self.assertIs(table._dataset, dataset)
        self.assertEqual(table.schema, [])

    def test_table_w_schema(self):
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        conn = _Connection({})
        client = _Client(project=self.PROJECT, connection=conn)
        dataset = self._make_one(self.DS_ID, client=client)
        full_name = SchemaField('full_name', 'STRING', mode='REQUIRED')
        age = SchemaField('age', 'INTEGER', mode='REQUIRED')
        table = dataset.table('table_id', schema=[full_name, age])
        self.assertIsInstance(table, Table)
        self.assertEqual(table.table_id, 'table_id')
        self.assertIs(table._dataset, dataset)
        self.assertEqual(table.schema, [full_name, age])


class _Client(object):

    def __init__(self, project='project', connection=None):
        self.project = project
        self._connection = connection


class _Connection(object):

    def __init__(self, *responses):
        self._responses = responses
        self._requested = []

    def api_request(self, **kw):
        from google.cloud.exceptions import NotFound

        self._requested.append(kw)

        try:
            response, self._responses = self._responses[0], self._responses[1:]
        except IndexError:
            raise NotFound('miss')
        else:
            return response
