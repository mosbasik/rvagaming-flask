class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    steam_id = db.Column(db.String(40))
    nickname = db.String(80)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

    @taticmethod
    def get_or_create(steam_id):
        rv = User.query.filter_by(steam_id=steam_id).first()
        if rv is None:
            rv = User()
            rv.steam_id = steam_id
            db.session.add(rv)
        return rv
