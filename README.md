# Django News

It's an example of how to use Django for a webpage of news.

## Dependencies

```bash
pip install -r requeriments.txt
```

## Configuration

```bash
export KLEIN_CONFIG=./path/your-config.yml
```

## Running MongoDB on Docker-compsoe

In Case you want to test the database locally, you can simplely execute the command below to create a mongodb container to test the application.
```bash
docker-compose up --build
```

P.S. Use the file config_example.yml as example to create your own config.yml, the information in the config.yml might not be in the repository.

## Starting with Django

- 1-) Creating project:
```bash
django-admin startproject django_news
cd django_news
```
- 2-) Creating application of news:
```bash
django-admin startapp noticias
```


## Populating DB with News 

This part can be an web scraper generating information with OpenAI API.

```bash
python pipeline_populate_db.py
```