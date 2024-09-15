from datetime import datetime, timezone
from news.models import News

news_instance = News(
    title="Breaking News: Django Updates Stoke",
    summary = "New site of news",
    # List of paragraphs (use single quotes, as some paragraphs have double quotes to repeat what was said)
    content=[
        'Last week we had 12 pull requests merged into Django by 10 different contributors - including 4 first-time contributors! Congratulations to SirenityK, Mariatta, Wassef Ben Ahmed and github-user-en for having their first commits merged into Django - welcome on board!',
        'Through decree 112/2023 published on Tuesday in the Official Gazette, the Argentine government has officially withdrawn LATAM Brazil’s (under the name TAM Linhas Aéreas) permission to operate the route linking Sao Paulo to the Falkland Islands (Islas Malvinas) with a stopover in Cordoba.',
        '"At present, the priority of the National Executive Power regarding the national policy of air connection with the Malvinas Islands (Province of Tierra del Fuego, Antarctica and South Atlantic Islands – Argentine Republic) is the resumption of direct scheduled flights from the Argentine mainland,” the decree states, adding that the 602/19 decree that granted the permit to LATAM Brazil specified that air services “would be kept under review'
    ],
    image_url="img/image_test.png", # news/static/img/...
    date_published=datetime.now(timezone.utc),
    author="Jane Doe",
    tags=["Django", "Updates"],
    category="Technology",
    source="uol.com",
    views = 0
)

news_instance.save_to_db()

print("News item saved successfully!")
