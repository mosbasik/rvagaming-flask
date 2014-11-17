from app import db

class Steam_User(db.Model):
    steam_user_key = db.Column(db.Integer, primary_key=True)
    site_user_key = db.Column(db.Integer)
    steam_id = db.Column(db.String(40))
    steam_32 = db.Column(db.String(40))
    steam_64 = db.Column(db.String(40))
    nickname = db.String(80)


    def __repr__(self):
        return '<User %r>' % (self.nickname)


    @staticmethod
    def get_or_create(steam_64):
        rv = User.query.filter_by(steam_id=steam_id).first()
        if rv is None:
            rv = User()
            rv.steam_id = steam_id
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
