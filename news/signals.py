from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Category, News
from faker import Faker
import random

# Get the User model
User = get_user_model()

# List of default news image paths
default_news_images = [
    'thumbnail/default/abcd.jpg',
    'thumbnail/default/efgh.jpg',
    'thumbnail/default/ijkl.jpg',
    'thumbnail/default/mnop.jpg',
    'thumbnail/default/qrst.jpg',
    # Add more image paths as needed
]

# Default categories with descriptions and thumbnail paths
default_categories = {
    "International": {
        "desc": "Global news covering international events, politics, and significant incidents from around the world.",
        "thumbnail": "thumbnails/international.jpg",
    },
    "Sports": {
        "desc": "Coverage of major sports events, results, athlete news, and analysis of games and tournaments.",
        "thumbnail": "thumbnails/sports.jpg",
    },
    "Tech": {
        "desc": "Updates on tech companies, new product launches, innovations, startups, and cybersecurity.",
        "thumbnail": "thumbnails/tech.jpg",
    },
    "Business & Finance": {
        "desc": "News related to the stock market, economy, corporate world, financial policies, and business trends.",
        "thumbnail": "thumbnails/business_finance.jpg",
    },
    "Travel": {
        "desc": "News about destinations, travel tips, industry trends, and tourism updates.",
        "thumbnail": "thumbnails/travel.jpg",
    },
    "Politics": {
        "desc": "National and international political developments, government policies, elections, and more.",
        "thumbnail": "thumbnails/politics.jpg",
    },
    "Health": {
        "desc": "News on medical advancements, public health issues, fitness trends, and wellness tips.",
        "thumbnail": "thumbnails/health.jpg",
    },
    "Entertainment": {
        "desc": "Celebrity news, movies, TV shows, music, fashion, and pop culture events.",
        "thumbnail": "thumbnails/entertainment.jpg",
    },
    "Science": {
        "desc": "Discoveries, research, space exploration, and innovations in various scientific fields.",
        "thumbnail": "thumbnails/science.jpg",
    },
    "Lifestyle": {
        "desc": "Topics like food, fashion, home decor, personal development, and human interest stories.",
        "thumbnail": "thumbnails/lifestyle.jpg",
    },
    "Crime & Law": {
        "desc": "Coverage of criminal incidents, investigations, trials, and changes in the legal system.",
        "thumbnail": "thumbnails/crime_law.jpg",
    },
    "Education": {
        "desc": "Updates on educational reforms, policies, academic research, and learning resources.",
        "thumbnail": "thumbnails/education.jpg",
    },
    "Weather": {
        "desc": "Forecasts, climate news, and updates on natural disasters or extreme weather conditions.",
        "thumbnail": "thumbnails/weather.jpg",
    }
}

def create_category(title, desc, thumbnail):
    """
    Create a new category if it doesn't already exist.

    Args:
        title (str): The title of the category.
        desc (str): A description of the category.
        thumbnail (str): Path to the thumbnail image for the category.
    """
    category, created = Category.objects.get_or_create(
        title=title,
        defaults={'desc': desc, 'thumbnail': thumbnail}
    )
    return category

def generate_sample_news(category, author):
    """
    Generate and add sample news articles for a given category.

    Args:
        category (Category): The category for which to generate news articles.
        author (User): The author of the news articles.
    """
    fake = Faker()
    for _ in range(10):
        title = fake.sentence(nb_words=6)
        desc = fake.text(max_nb_chars=250)
        content = fake.paragraph(nb_sentences=5)
        thumbnail = random.choice(default_news_images)  # Randomly select a thumbnail image
        slug = slugify(title)

        # Create news article if it doesn't already exist
        News.objects.get_or_create(
            title=title,
            desc=desc,
            slug=slug,
            thumbnail=thumbnail,
            is_active=True,
            author=author,
            content=content,
            views=random.randint(0, 1000),
            category=category,
        )

@receiver(post_migrate)
def create_default_categories_and_news(sender, **kwargs):
    """
    Signal receiver that creates default categories and sample news after migration.

    Args:
        sender: The model class that triggered the signal.
        **kwargs: Additional keyword arguments.
    """
    author = User.objects.first()  # Ensure at least one user exists for authoring news

    if author:
        for title, details in default_categories.items():
            category = create_category(title, details['desc'], details['thumbnail'])
            generate_sample_news(category, author)

