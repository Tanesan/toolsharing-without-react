from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
import json
import ast
from app.services import article_service

articles = Blueprint('articles', __name__)
 

@articles.route('/')
@login_required  # ログインしていないと表示できないようにする
def find_all():
    print("B") # airticle投稿後ページ
    articles = article_service.find_all()
    return render_template('index.html', articles=articles)


@articles.route('/<article_id>')
@login_required  # ログインしていないと表示できないようにする
def find_one(article_id: int):
    print("A")
    article = article_service.find_one(article_id)
    print(article.blocks)
    articleBody = ast.literal_eval(article.blocks)
    # articleBody = json.loads(articleBody)
    print(len(articleBody))
    return render_template('article.html', article=article, articleBody = articleBody, num_range = len(articleBody))



@articles.route('/add', methods=['GET', 'POST'])
@login_required  # ログインしていないと表示できないようにする
def add():
    try:
        if request.method == 'GET':
            return render_template('post.html')
        else:
            # postとputを一つのメソッドでできるようにarticle_idを入れてあるが、
            # 新規作成時はNoneにしておく。二つ目のrequet.formはformから送られてくる情報をそのままserviceに渡す
            # current_userはflask_loginの機能で、現在ログインしているユーザーの情報を取得することができる。
            article = article_service.save(None, current_user.id, request.form["data"])
            #print(request.form)
            #print(request.form["data"])
            #print(article)
            if article is None:
                flash('Articleを追加することができませんでした。')
                return redirect(url_for('articles.add'))
            flash('Articleを追加しました。')
            return redirect(url_for('articles.find_all'))
    except Exception:
        flash('Articleを追加することができませんでした。')
        return redirect(url_for('articles.add'))


@articles.route('/update/<article_id>', methods=['GET', 'POST'])
@login_required  # ログインしていないと表示できないようにする
def update(article_id: int):
    try:
        if request.method == 'GET':
            article = article_service.find_one(article_id)
            return render_template('update.html', article=article)
        else:
            article = article_service.save(article_id, current_user.id, request.form)
            if article is None:
                flash('Articleを修正することができませんでした。')
                return redirect(url_for('articles.update', article_id=article_id))
            flash('Articleを修正しました。')
            return redirect(url_for('articles.find_all'))
    except Exception:
        flash('Articleを修正することができませんでした。')
        return redirect(url_for('articles.update', article_id=article_id))


@articles.route('/delete/<article_id>', methods=['POST'])
@login_required  # ログインしていないと表示できないようにする
def delete(article_id: int):
    try:
        article_service.delete(article_id)
        flash('Articleを削除しました。')
        return redirect(url_for('articles.find_all'))
    except Exception:
        flash('Articleを削除することができませんでした。')
        return redirect(url_for('articles.find_all'))