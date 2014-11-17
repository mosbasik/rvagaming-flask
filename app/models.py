from app import db


class Site_User(db.Model):
    site_user_key = db.Column(db.Integer, primary_key=True)
    
    def __repr__(self):
        return '<Site User %r>' % (self.site_user_key)


class Steam_User(db.Model):
    steam_user_key = db.Column(db.Integer, primary_key=True)
    site_user_key = db.Column(db.Integer)
    steam_32      = db.Column(db.Integer)
    steam_64      = db.Column(db.Integer)
    nickname      = db.Column(db.String(80))
    is_main       = db.Column(db.Integer)

    def __repr__(self):
        return '<Steam User %r>' % (self.nickname)

    @staticmethod
    def get_or_create(steam_64):
        rv = User.query.filter_by(steam_64=steam_64).first()
        if rv is None:
            rv = User()
            rv.steam_64 = steam_64
            db.session.add(rv)
        return rv

    @staticmethod
    def get_steam_32(steam_64):
        '''
        Given the integer representation of a 64-bit steam id, returns the integer
        representation of a 32-bit steam id, as described in
        https://developer.valvesoftware.com/wiki/SteamID
        '''
        full_binary = "{0:b}".format(steam_64)
        padding_zeros = (64 - len(full_binary))*"0"
        full_binary = padding_zeros + full_binary
        steam_32_binary = full_binary[-32:]
        steam_32 = int(steam_32_binary, 2)
        return steam_32

    @staticmethod
    def split_id(steam_64):
        '''
        Given the integer representation of a 64-bit steam id, returns a tuple
        containing (steam_32, instance, acctype, universe), as described in
        https://developer.valvesoftware.com/wiki/SteamID
        '''
        full_binary = "{0:b}".format(steam_64)
        pad = (64 - len(full_binary))*"0"
        full_binary = pad + full_binary
        # print '\nfull binary.  original: ' + str(steam_64) + " bin length: " + str(len(full_binary))
        # print full_binary
        steam_32_binary = full_binary[-32:]
        steam_32 = int(steam_32_binary, 2)
        # print '\nint 32 binary.  original: ' + str(steam_32) + " bin length: " + str(len(steam_32_binary))
        # print (64-32)*" " + str(steam_32_binary)
        instance_binary = full_binary[-(32+20):32]
        instance = int(instance_binary)
        # print '\ninstance.  original: ' + str(instance) + " bin length: " + str(len(instance_binary))
        # print (64-32-20)*" " + str(instance_binary)
        acctype_binary = full_binary[-(32+20+4):32-20]
        acctype = int(acctype_binary)
        # print '\nacctype.  original: ' + str(acctype) + " bin length: " + str(len(acctype_binary))
        # print (64-32-20-4)*" " + str(acctype_binary)
        universe_binary = full_binary[-(32+20+4+8):32-20-4]
        universe = int(universe_binary)
        # print '\nuniverse.  original: ' + str(universe) + " bin length: " + str(len(universe_binary))
        # print (64-32-20-4-8)*" " + str(universe_binary)
        return (steam_32, instance, acctype, universe)


class Facebook_User(db.Model):
    facebook_user_key = db.Column(db.Integer, primary_key=True)
    site_user_key = db.Column(db.Integer)
    facebook_id   = db.Column(db.Integer)
    facebook_name = db.Column(db.String(80))
    facebook_link = db.Column(db.String(150))

    def __repr__(self):
        return '<Facebook User %r>' % (self.facebook_name)


class Match(db.Model):
    match_key = db.Column(db.Integer, primary_key=True)
    date      = db.Column(db.Integer)
    duration  = db.Column(db.Integer)
    region    = db.Column(db.Integer)
    mode      = db.Column(db.Integer)
    type      = db.Column(db.Integer)

    def __repr__(self):
        return '<Match ID %r>' % (self.match_key)


class Hero(db.Model):
    hero_key = db.Column(db.Integer, primary_key=True)
    hero_name = db.Column(db.String(80))

    def __repr__(self):
        return '<Hero %r>' % (self.hero_name)


class Team(db.Model):
    team_key  = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(80))

    def __repr__(self):
        return '<Team %r>' % (self.team_name)

