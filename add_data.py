import sqlite3

def add_project(title, description, image_url):
    with sqlite3.connect('portfolio.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO projects (title, description, image_url) VALUES (?, ?, ?)",
                  (title, description, image_url))
        conn.commit()

def add_blog_post(title, content, date):
    with sqlite3.connect('portfolio.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO blog (title, content, date) VALUES (?, ?, ?)",
                  (title, content, date))
        conn.commit()

# Test ma'lumotlari
if __name__ == "__main__":
    # Loyhalar qo'shish
    add_project("Loyiha 1", "Bu mening birinchi loyiham.", "https://via.placeholder.com/150")
    add_project("Loyiha 2", "Ikkinchi loyiha tasviri.", "https://via.placeholder.com/150")

    # Blog postlari qo'shish
    add_blog_post("Birinchi post", "Bu mening birinchi blog postim mazmuni.", "2025-05-02")
    add_blog_post("Ikkinchi post", "Ikkinchi post mazmuni.", "2025-05-03")

    print("Ma'lumotlar muvaffaqiyatli qo'shildi!")