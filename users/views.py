from rest_framework import viewsets, generics

from users.models import User
from users.serilzers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    '''
    Метод get_queryset позволяет фильтровать записи модели в зависимости от прав доступа.
    Если пользователь является суперпользователем, то он имеет доступ ко всем записям модели.
    В противном случае он может работать только со своим профилем.
    '''

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return self.queryset
        return self.queryset.filter(user=user)

    '''
    Метод perform_create вызывается при создании новой записи модели и позволяет автоматически заполнить поле user
    значением текущего пользователя.
    '''

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    '''
    Метод get_object позволяет получить запись модели, которую нужно отредактировать.
    В данном случае мы получаем запись по полю user,
    чтобы пользователь мог редактировать только свой профиль.
    '''

    def get_object(self):
        return self.queryset.get(user=self.request.user)
