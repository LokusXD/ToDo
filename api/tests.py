from django.test import TestCase
from api.models import Task
import datetime
from api.views import RotateArray, KthLargestElement, LongestIncreasingPath
# Create your tests here.

class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(title = "xd",  description = "xd XdXDxdxd xddxxdxdxd", due_date = datetime.datetime(2024, 5, 28))
        
    def test_task(self):
        task = Task.objects.get(title = "xd")
        self.assertEqual(task.title, "xd")

