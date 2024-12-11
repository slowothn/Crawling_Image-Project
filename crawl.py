import os
import requests
from bs4 import BeautifulSoup

def create_folder(folder_name):
    """폴더 생성 함수"""
    folder_path = os.path.abspath(folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def download_image(image_url, folder_path, file_name):
    """이미지 다운로드 함수"""
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"저장됨 : {file_name}")
        else:
            print(f"다운로드에 실패했어요: {file_name}")
    except Exception as e:
        print(f"Error downloading {file_name}: {e}")

def crawl_images(url, folder_name):
    """이미지 크롤링 함수"""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # img 태그의 src 속성 가져오기
        images = soup.find_all('img')
        
        folder_path = create_folder(folder_name)
        print(f"해당 경로에 저장됩니다: {folder_path}")
        
        if not images:
            print("이 페이지에서 이미지를 찾지 못 했어요.")
            return

        for index, img in enumerate(images):
            img_url = img.get('src')
            if not img_url:
                continue
            
            # 이미지 URL이 절대 경로인지 확인
            if not img_url.startswith('http'):
                img_url = url + img_url
            
            # 파일 이름 지정
            file_name = f"image_{index + 1}.jpg"
            
            # 이미지 다운로드
            download_image(img_url, folder_path, file_name)

        print("이미지 다운로드를 완료했습니다.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        # 사용자로부터 URL과 폴더 이름 입력받기
        target_url = input("이미지를 다운받을 url을 입력 후 Enter: ").strip()
        save_folder = input("저장할 폴더 이름을 입력 후 Enter(입력하지 않으면 download_images로 이름이 자동 지정돼요): ").strip()

        # 폴더 이름 기본값 설정
        if not save_folder:
            save_folder = "downloaded_images"
        
        # 이미지 크롤링 수행
        crawl_images(target_url, save_folder)

    except Exception as main_e:
        print(f"Unexpected error: {main_e}")
