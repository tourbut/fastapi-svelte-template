# FastAPI & Svelte 웹 서비스 템플릿

## 개요

이 템플릿은 FastAPI와 Sveltekit을 사용하여 웹 서비스를 구축하기 위한 시작점을 제공합니다. 템플릿은 Docker를 이용한 컨테이너화, PostgreSQL을 데이터베이스로, Gunicorn을 Python WSGI HTTP 서버로, Nginx를 리버스 프록시 서버로 사용합니다.

## 사용 기술

- **Docker**: 애플리케이션과 그 종속성을 패키징하기 위한 컨테이너화 플랫폼
- **PostgreSQL**: 관계형 데이터베이스 관리 시스템
- **Gunicorn**: FastAPI를 실행하기 위한 Python WSGI HTTP 서버
- **Nginx**: 웹 서버 및 리버스 프록시 서버
- **FastAPI**: Python 3.11을 사용하여 API를 구축하기 위한 현대적이고 고성능의 웹 프레임워크
- **Sveltekit**: Svelte를 사용하여 고성능 웹 애플리케이션을 구축하기 위한 프레임워크

## 시작하기

### 사전 요구 사항

로컬 개발 환경에 다음이 설치되어 있는지 확인하세요:

- Docker
- Docker Compose

### 설치

1. **저장소 클론**

   ```sh
   git clone https://github.com/yourusername/fastapi-svelte-template.git
   cd fastapi-svelte-template

2. Prod.env 수정

3. 구동
    ```sh
    . docker_compose.sh
    ```

