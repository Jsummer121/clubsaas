from rest_framework.generics import ListAPIView

# 自定义响应格式

class JsonResponse(ListAPIView):
    def list(self, request, *args, **kwargs):
        queryset = Snippet.objects.all()
        response = {
            'code': 0,
            'data': [],
            'msg': 'success',
            'total': ''
        }
        serializer = SnippetSerializer(queryset, many=True)
        response['data'] = serializer.data
        response['total'] = len(serializer.data)
        return Response(response)
