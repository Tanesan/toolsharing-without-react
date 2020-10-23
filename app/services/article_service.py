from app import db
 
from app.article_config import Article
import json
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import desc

article = Article()
def find_all() -> Article:
    return Article.query.order_by(desc(article.create_time)).all()
 
def find_trend() -> Article:
    return Article.query.order_by(desc(article.view)).all()


def find_one(article_id: int) -> Article:
    if article_id is None:
        raise Exception
    return Article.query.filter_by(id=article_id).first()
 
 
def save(article_id: int, user_id: int, data: {}) -> Article:
    try:
        if article_id is None:
            data = json.loads(data)
            view = 0
            print(data)
            article = Article.from_args(
                data,
                user_id,
                view
            )
            print(article)
            db.session.add(article)
        else:
            print(data+"bbbb")
            article = find_one(article_id)
            article.title = data["title"]
            article.create_time = data["create_time"]
            article.blocks = data["blocks"]
            article.user_id = user_id
            article.view = 0
        db.session.commit()
        return article
    except SQLAlchemyError:
        raise Exception
 
 
def delete(article_id: int) -> bool:
    if article_id is None:
        raise Exception
    try:
        article = find_one(article_id)
        db.session.delete(article)
        db.session.commit()
        return True
    except SQLAlchemyError:
        raise Exception