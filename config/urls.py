from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # chat/urls에 있는 모든 URL 패턴에 일괄적으로
    #  chat/ 라는 prefix 주소를 부여하겠다.
    path("chat/", include("chat.urls")),
]

# 유저가 업로드한 파일을 서빙하는 View 설정 (View <- 장고 개발서버에서 제공)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
