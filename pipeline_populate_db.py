from datetime import datetime, timezone
from news.models import News

news_instance = News(
    title="Breaking News: Django Updates Stoke",
    content="Django has released a new update with exciting features.",
    image_url="img/image_test.png", # news/static/img/...
    date_published=datetime.now(timezone.utc),
    author="Jane Doe",
    tags=["Django", "Updates"],
    category="Technology",
    source="uol.com"
)

news_instance.save_to_db()

print("News item saved successfully!")
