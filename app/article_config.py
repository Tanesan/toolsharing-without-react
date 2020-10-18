from app import db
import json
 
# モデルに関する設定
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))
    create_time = db.Column(db.Integer)
    blocks = db.Column(db.String(1000000000))
    # Userに所有されている状態
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', name='user_id__article_id_fk'))
 
    @classmethod
    def from_args(cls, data, user_id: int):
        instance = cls()
        instance.title = str(data["title"])
        instance.create_time = int(data["time"])
        instance.blocks = str(data["blocks"])
        instance.user_id = int(user_id)
        print("A")
        return instance