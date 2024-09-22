from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics
import heapq

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskList(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
class TaskDetail(APIView):
    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response(status=404)

class TaskUpdate(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'     
                   
class TaskDelete(APIView):
    def delete(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            task.delete()
            return Response(status=204)
        except Task.DoesNotExist:
            return Response(status=404)
        
class NearestTask(APIView):
    def get(self, request):
        tasks = Task.objects.filter(due_date__isnull=False).order_by('due_date')
        if tasks.exists():
            serializer = TaskSerializer(tasks.first())
            return Response(serializer.data)
        return Response(status=404)


class RotateArray(APIView):
    def post(self, request):
        nums = request.data.get('nums')
        k = request.data.get('k')
        k = k % len(nums)
        result = nums[-k:] + nums[:-k]
        return Response({'result': result})
    
class KthLargestElement(APIView):
    def post(self, request):
        nums = request.data.get('nums')
        k = request.data.get('k')
        return Response({'result': heapq.nlargest(k, nums)[-1]})
    
class LongestIncreasingPath(APIView):
    def post(self, request):
        matrix = request.data.get('matrix')
        if not matrix:
            return Response({'result': 0})

        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        memo = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if memo[i][j] > 0:
                return memo[i][j]
            val = matrix[i][j]
            max_len = 1
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > val:
                    max_len = max(max_len, 1 + dfs(x, y))
            memo[i][j] = max_len
            return max_len

        max_len = 0
        for i in range(m):
            for j in range(n):
                max_len = max(max_len, dfs(i, j))

        return Response({'result': max_len})

