from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.views import searchAuthors,SingleAuthor,SinglePublication



class TestView:


	def test_search_authors(self):

		path = reverse('searchAuthors')
		request = RequestFactory().get(path)

		response = searchAuthors(request)
		assert response.status_code == 200

	def test_single_author(self):

		path = reverse('SingleAuthor',kwargs = {'authorName':'Andrew Ng'})
		request = RequestFactory().get(path)

		response = SingleAuthor(request,'Andrew Ng')
		assert response.status_code == 200


	def test_single_publication(self):

		path = reverse('SinglePublication',kwargs = {'authorName':'Andrew Ng','pubind':0})
		request = RequestFactory().get(path)

		response = SinglePublication(request,'Andrew Ng',0)
		assert response.status_code == 200
