from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from articles import services


class ArticleListView(APIView):
    def get(self, request: Request, format=None) -> Response:
        article = services.get_articles(status='publish')

        serializer = services.get_serializer(instance=article, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ArticleTagsListView(APIView):
    def get(self, request: Request, tags=None, format=None) -> Response:
        print(tags)
        article = services.get_articles(tags=tags, status='publish')

        serializer = services.get_serializer(instance=article, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ArticleDetailView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: Request, pk=None, format=None) -> Response:
        article = services.get_article_by_id(id=pk)

        if article.author.id != request.user.id and article.status != 'publish':
            return Response(data={"detail": "No Article matches the given query."}, status=status.HTTP_404_NOT_FOUND)

        serializer = services.get_serializer(instance=article)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, pk, format=None) -> Response:
        article = services.get_article_id(id=pk)

        if article[0].author.id != request.user.id:
            return Response(data={'message': 'You are unauthorized to delete the requested article'},
                            status=status.HTTP_401_UNAUTHORIZED)

        serializer = services.post_article_serializer(instance=article, many=True)
        request_serializer = services.post_article_serializer(data=request.data, partial=True)

        if request_serializer.is_valid(raise_exception=True):
            serializer.data[0].update(request_serializer.validated_data)

            print(request.data)
            print(request_serializer.validated_data)
            print(serializer.data)
            services.update_article_model(id=pk, **serializer.data[0])

            return Response(serializer.data[0], status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None) -> Response:
        article = services.get_article_by_id(id=pk)

        if article.author.id != request.user.id:
            return Response(data={'message': 'You are unauthorized to delete the requested article'},
                            status=status.HTTP_401_UNAUTHORIZED)

        services.delete_article_model(id=pk)

        return Response(data={'message': 'Article deleted successfully'}, status=status.HTTP_200_OK)


class ArticleCreateView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: Request, format=None) -> Response:
        serializer = services.post_article_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            _, created = services.create_article_model(author=request.user.id, **serializer.validated_data)

            if not created:
                return Response(data={"detail": "Error create the article"}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)