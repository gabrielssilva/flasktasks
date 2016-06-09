import unittest
from flasktasks import db
from flasktasks.tests.flasktasks_testcase import FlaskTasksTestCase
from flasktasks.models import Color, Tag, Mission, Status


class MissionsTest(FlaskTasksTestCase):
    def setUp(self):
        super().setUp()
        self.valid_tag = Tag('valid tag', Color.BLUE)
        db.session.add(self.valid_tag)
        db.session.commit()

    def test_missions_page(self):
        first_mission = Mission('mission a', 'description', self.valid_tag.id)
        second_mission = Mission('mission b', 'description', self.valid_tag.id)
        db.session.add(first_mission)
        db.session.add(second_mission)
        db.session.commit()

        response = self.app.get('/missions')
        assert b'mission a' in response.data
        assert b'mission b' in response.data

    def test_new_mission_form(self):
        response = self.app.get('/missions/new')
        assert b'New Mission' in response.data

    def test_mission_creation(self):
        data = { 'title':'some mission', 'description':'a useful description',
                 'tag_id':self.valid_tag.id }
        response = self.app.post('/missions/new', data=data)
        assert response.status_code == 302

        response = self.app.get('/missions')
        assert b'some mission' in response.data

if __name__ == '__main__':
    unittest.main()
