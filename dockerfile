# Dockerfile
FROM python:3.10

# 작업 디렉토리 설정
WORKDIR /usr/src/app

# 의존성 파일 복사
COPY requirements.txt ./

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# Gunicorn 실행 명령 
RUN pip install gunicorn

# 포트 설정
EXPOSE 8000

# Gunicorn 실행
CMD ["gunicorn", "django_project.wsgi:application", "--bind", "0.0.0.0:8000"]