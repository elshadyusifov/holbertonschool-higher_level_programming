import requests
import csv

def fetch_and_print_posts():
    """
    Bu funksiya JSONPlaceholder API-dən post-ları alır və başlıqları konsola çap edir.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Status kodunu göstər
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()  # JSON formatında cavabı oxu
        for post in posts:
            print(post['title'])  # Hər postun başlığını çap et
    else:
        print("Sorğu uğursuz oldu.")


def fetch_and_save_posts():
    """
    Bu funksiya JSONPlaceholder API-dən post-ları alır və onları posts.csv faylına yazır.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Yalnız id, title və body sahələrini seç
        formatted_posts = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        # CSV faylına yaz
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()  # Başlıqları yaz
            writer.writerows(formatted_posts)  # Məlumatları yaz
        print("Postlar uğurla posts.csv faylına yazıldı.")
    else:
        print("Sorğu uğursuz oldu.")
