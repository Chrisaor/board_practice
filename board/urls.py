from rest_framework.routers import SimpleRouter

from board.views import BoardViewSet

router = SimpleRouter()
router.register('board', viewset=BoardViewSet.as_view(), base_name='board')
