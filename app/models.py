from app import db


class Site_User(db.Model):
    site_user_key = db.Column(db.Integer, primary_key=True)
    steam_accounts = db.relationship('Steam_User', backref='owner', lazy='dynamic')
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.site_user_key)
        except NameError:
            return str(self.site_user_key)
     
    def __repr__(self):
        return '<Site User %r>' % (self.site_user_key)


class Steam_User(db.Model):
    steam_64      = db.Column(db.Integer, primary_key=True)
    site_user_key = db.Column(db.Integer, db.ForeignKey('site__user.site_user_key'))
    steam_32      = db.Column(db.Integer)
    nickname      = db.Column(db.String(80))
    is_main       = db.Column(db.Integer)

    def __repr__(self):
        return '<Steam User %r>' % (self.nickname)

    @staticmethod
    def get_or_create(steam_64):
        rv = Steam_User.query.filter_by(steam_64=steam_64).first()
        if rv is None:
            rv = User()
            rv.steam_64 = steam_64
            rv.steam_32 = get_steam_32(steam_64)
            db.session.add(rv)
        return rv
   
    import urllib2 
    @staticmethod
    def get_steam_user_info(steam_64):
        options = {
            'key': app.config['STEAM_API_KEY'],
            'steam_64s': steam_64
        }
        url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0001/?%s' % url_encode(options)
        rv = json.load(urllib2.urlopen(url))
        return rv['response']['players']['player'][0] or {}

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
    outcome   = db.Column(db.String(10))

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


class Region(db.Model):
    region_key  = db.Column(db.Integer, primary_key=True)
    region_name = db.Column(db.String(40))

    def __repr__(self):
        return '<Region %r>' % (self.region_name)


class Mode(db.Model):
    mode_key  = db.Column(db.Integer, primary_key=True)
    mode_name = db.Column(db.String(40))

    def __repr__(self):
        return '<Mode %r>' % (self.mode_name)


class Type(db.Model):
    type_key  = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(40))

    def __repr__(self):
        return '<Type %r>' % (self.type_name)
