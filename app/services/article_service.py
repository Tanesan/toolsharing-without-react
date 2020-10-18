from app import db
 
from app.article_config import Article
import json
from sqlalchemy.exc import SQLAlchemyError
 
 
def find_all() -> [Article]:
    return Article.query.all()
 
 
def find_one(article_id: int) -> Article:
    if article_id is None:
        raise Exception
    return Article.query.filter_by(id=article_id).first()
 
 
def save(article_id: int, user_id: int, data: {}) -> Article:
    try:
        if article_id is None:
            data = json.loads(data)
            article = Article.from_args(
                data,
                user_id
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