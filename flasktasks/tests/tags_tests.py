import unittest
from flasktasks.tests.flasktasks_testcase import FlaskTasksTestCase
from flasktasks.models import Color, Tag


class TagsTest(FlaskTasksTestCase):
    def test_display_new_tag_form(self):
        response = self.app.get('/tags/new')
        assert b'New Tag' in response.data

    def test_new_tag_creation(self):
        data = { 'name': 'new tag', 'color_id': Color.RED.value }
        response = self.app.post('/tags/new', data=data)
        
        tag = Tag.query.filter_by(name='new tag').first()
        assert response.status_code == 302
        assert tag is not None

    def test_new_tag_creation_error_with_invalid_color(self):
        data = { 'name': 'new tag', 'color_id': -1 }
        response = self.app.post('/tags/new', data=data)

        tags = Tag.query.all()
        assert response.status_code == 400
        assert tags == []

if __name__ == '__main__':
    unittest.main()
