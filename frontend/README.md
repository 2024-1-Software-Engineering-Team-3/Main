# SKKULearn frontend

## Reference
[1] https://github.com/flutter/flutter "flutter"

## OS별 프로젝트 실행 방법

### Windows

아래 커멘트를 사용해 프로젝트 디렉토리로 이동한 후 실행하세요.
```
cd /frontend
flutter run
```

Windows 사용자가 Chrome과 Edge 브라우저를 설치했다면 아래와 같은 리스트를 확인할 수 있습니다.
```
More than one device connected; please specify a device with the '-d <deviceId>' flag, or use '-d all' to act on all devices.

Windows (desktop) • windows • windows-x64    • Microsoft Windows [Version 10.0.22631.xxxx]
Chrome (web)      • chrome  • web-javascript • Google Chrome 125.0.xxxx.xxx
Edge (web)        • edge    • web-javascript • Microsoft Edge 125.0.xxxx.xx
```

원하는 장치를 선택하여 아래와 같이 실행할 수 있습니다.
```
flutter run -d windows
flutter run -d chrome
flutter run -d edge
```
### Linux
아래 커멘트를 사용해 프로젝트 디렉토리로 이동한 후 실행하세요.
```
cd /frontend
flutter run
```

Linux 사용자가 Chrome 브라우저를 설치했다면 아래와 같은 리스트를 확인할 수 있습니다.
```
More than one device connected; please specify a device with the '-d <deviceId>' flag, or use '-d all' to act on all devices.

Linux (desktop) • linux  • linux-x64      • Ubuntu 20.04.6 LTS 5.15.xxx.x-microsoft-standard-WSL2
Chrome (web)    • chrome • web-javascript • Google Chrome 125.0.xxxx.xxx
```

원하는 장치를 선택하여 아래와 같이 실행할 수 있습니다.
```
flutter run -d linux
flutter run -d chrome
```

### macOS
아래 커멘트를 사용해 프로젝트 디렉토리로 이동한 후 실행하세요.
```
cd /frontend
flutter run
```

macOS 사용자가 Edge 브라우저를 설치했다면 아래와 같은 리스트를 확인할 수 있습니다.
```
More than one device connected; please specify a device with the '-d <deviceId>' flag, or use '-d all' to act on all devices.


macOS (desktop) • macos • darwin-arm64   • macOS 13.3
Edge (web)      • edge  • web-javascript • Microsoft Edge 125.0.xxxx.xx
```

원하는 장치를 선택하여 아래와 같이 실행할 수 있습니다.
```
flutter run -d macos
flutter run -d edge
```

## 코드 설명(디렉토리별 설명)
### 프로젝트 구조
```
frontend/
|
├── lib/
|   ├── main.dart
|   └─── src/
|        ├── app.dart
|        ├── pages/
|        |   ├── login/
|        |   |   ├── login_page.dart
|        |   |   └── register_page.dart
|        |   ├── mypage/
|        |   |   └── my_page.dart
|        |   ├── recruiting/
|        |   |   ├── recruiting_page.dart
|        |   |   └── create_team_page.dart
|        |   ├── qna/
|        |   |   ├── qna_page.dart
|        |   |   ├── create_question_page.dart
|        |   |   ├── qna_detail_page.dart
|        |   |   └── other_user_page.dart
|        |   ├── sharing/
|        |   |   ├── sharing_page.dart
|        |   |   ├── create_sharing_page.dart
|        |   |   └── sharing_detail_page.dart
|        ├── controller/
|        |   ├── bottom_nav_controller.dart
|        |   └── user_controller.dart
|        ├── models/
|        |   ├── recruiting_post.dart
|        |   ├── qna_post.dart
|        |   └── sharing_post.dart
|        ├── components/
|        |   ├── myteam_post_widget.dart
|        |   ├── recruiting_post_widget.dart
|        |   ├── qna_post_widget.dart
|        |   ├── sharing_post_widget.dart
|        |   ├── favorite_star_button.dart
|        |   ├── image_data.dart
|        |   └── message_popup.dart
|        └── binding/
|            └── init_bindings.dart

```
### 디렉토리 및 파일 설명
**lib/**
- **main.dart**: 애플리케이션의 진입점 파일입니다.

**src/**
- **app.dart**: 애플리케이션의 주요 설정과 라우팅을 담당합니다.

**src/pages/**
- **login/**
    - **login_page.dart**: 로그인 페이지 화면입니다.
    - **register_page.dart**: 회원가입 페이지 화면입니다.
- **mypage/**
    - **my_page.dart**: 마이 페이지 화면입니다.
- **recruiting/**
    - **recruiting_page.dart**: 팀 모집 페이지 화면입니다.
    - **create_team_page.dart**: 팀 생성 페이지 화면입니다.
- **qna/**
    - **qna_page.dart**: Q&A 메인 페이지 화면입니다.
    - **create_question_page.dart**: 질문 작성 페이지 화면입니다.
    - **qna_detail_page.dart**: Q&A 상세 페이지 화면입니다.
    - **other_user_page.dart**: 다른 사용자 정보 페이지 화면입니다.
- **sharing/**
    - **sharing_page.dart**: 공유 게시판 메인 페이지 화면입니다.
    - **create_sharing_page.dart**: 공유 게시물 작성 페이지 화면입니다.
    - **sharing_detail_page.dart**: 공유 게시물 상세 페이지 화면입니다.

**src/controller/**
- **bottom_nav_controller.dart**: 하단 네비게이션 바의 상태 관리를 담당합니다.
- **user_controller.dart**: 사용자 관련 상태 관리를 담당합니다.

**src/models/**
- **recruiting_post.dart**: 팀 모집 게시물 모델입니다.
- **qna_post.dart**: Q&A 게시물 모델입니다.
- **sharing_post.dart**: 공유 게시물 모델입니다.

**src/components/**
- **myteam_post_widget.dart**: 팀 게시물 위젯입니다.
- **recruiting_post_widget.dart**: 팀 모집 게시물 위젯입니다.
- **qna_post_widget.dart**: Q&A 게시물 위젯입니다.
- **sharing_post_widget.dart**: 공유 게시물 위젯입니다.
- **favorite_star_button.dart**: 즐겨찾기 버튼 위젯입니다.
- **image_data.dart**: 이미지 데이터 위젯입니다.
- **message_popup.dart**: 메시지 팝업 위젯입니다.

**src/binding/**
- **init_bindings.dart**: 초기 바인딩 설정을 담당합니다.

