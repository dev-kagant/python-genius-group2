from app.models import db, Comment


# Adds a demo user, you can add other users here if you want
def seed_comments():

    comment_1_1 = Comment(
        user_comment='Not shy is a bop.',
        username='Demo',
        user_Id=1,
        song_Id=1
    )

    comment_1_2 = Comment(
        user_comment='I wasn\'t a fan but this song changed my mind.',
        username='Aaron Horton',
        user_Id=2,
        song_Id=1
    )

    comment_1_3 = Comment(
        user_comment='Are we gonna ignore that every comeback they get \
            prettier and prettier?!',
        username='Julia Adkins',
        user_Id=4,
        song_Id=1
    )

    comment_2_1 = Comment(
        user_comment='YG: How many wigs do you want? Blackpink: Yes.',
        username='Douglas Klein',
        user_Id=3,
        song_Id=2
    )

    comment_2_2 = Comment(
        user_comment='This isn\'t even the title track of the album.',
        username='Celia Hansen',
        user_Id=5,
        song_Id=2
    )

    comment_3_1 = Comment(
        user_comment='FXXK IT is a timeless song, it always sounds so fresh.',
        username='Celia Hansen',
        user_Id=5,
        song_Id=3
    )

    comment_3_2 = Comment(
        user_comment='Who says color pink makes a man unmanly?',
        username='Aaron Horton',
        user_Id=2,
        song_Id=3
    )

    comment_3_3 = Comment(
        user_comment='Fun fact: \
            Gdragon made the first ever lightstick in kpop so that bigbang \
            could spot their fans in crowds. And now almost every group has \
            a lightstick, if that\'s not some KING shit IDK what is.',
        username='Douglas Klein',
        user_Id=3,
        song_Id=3
    )

    comment_3_4 = Comment(
        user_comment='They are not perfect hell no \n \
            They are legends',
        username='Demo',
        user_Id=1,
        song_Id=3
    )

    comment_4_1 = Comment(
        user_comment='I am not responsible for who I punch while listening \
            to this song',
        username='Aaron Horton',
        user_Id=2,
        song_Id=4
    )

    comment_4_2 = Comment(
        user_comment='This song makes me wanna teach my cat how to bark.',
        username='Julia Adkins',
        user_Id=4,
        song_Id=4
    )

    comment_5_1 = Comment(
        user_comment='I just got into bts two weeks ago but wow this is \
            a masterpiece',
        username='Julia Adkins',
        user_Id=4,
        song_Id=5
    )

    comment_5_2 = Comment(
        user_comment='SAVE ME 500M \n \
            FAKE LOVE 700M \n \
            BOY WITH LUV 800M  \n \
            DNA 1BILLON',
        username='Celia Hansen',
        user_Id=5,
        song_Id=5
    )

    comment_5_3 = Comment(
        user_comment='This song ties with Fake Love.. Do you agree?',
        username='Douglas Klein',
        user_Id=3,
        song_Id=5
    )

    comment_6_1 = Comment(
        user_comment='How come the eve doesnt have an MV its one of \
            their best song',
        username='Douglas Klein',
        user_Id=3,
        song_Id=6
    )

    comment_6_2 = Comment(
        user_comment='D.O - What\'s the situation.. \n \
            Me- I can\'t choose my bias in EXO..',
        username='Julia Adkins',
        user_Id=4,
        song_Id=6
    )

    comment_6_3 = Comment(
        user_comment='Baekhyun a~',
        username='Demo',
        user_Id=1,
        song_Id=6
    )

    comment_6_4 = Comment(
        user_comment='SM don\'t be shy, give our boys a comeback',
        username='Aaron Horton',
        user_Id=2,
        song_Id=6
    )

    comment_7_1 = Comment(
        user_comment='Those who doesn\'t know this song shouldn\'t \
        be called KPOPPERS. That\'s a fact.',
        username='Douglas Klein',
        user_Id=3,
        song_Id=7
    )

    comment_8_1 = Comment(
        user_comment='Let’s just... ignore our online assignments and \
            watch this instead.',
        username='Julia Adkins',
        user_Id=4,
        song_Id=8
    )

    comment_8_2 = Comment(
        user_comment='Taeyong is your bias even if he is not your bias',
        username='Celia Hansen',
        user_Id=5,
        song_Id=8
    )

    comment_8_3 = Comment(
        user_comment='please SM \n \
            johnny, yuta, and winwin deserves more line and screentime',
        username='Aaron Horton',
        user_Id=2,
        song_Id=8
    )

    comment_9_1 = Comment(
        user_comment='Fun fact : you searched this coz you\'re still addicted',
        username='Julia Adkins',
        user_Id=4,
        song_Id=9
    )

    comment_9_2 = Comment(
        user_comment='Jackson Wang confirmed today: we left JYP, but we \
            still GOT7',
        username='Demo',
        user_Id=1,
        song_Id=9
    )

    comment_10_1 = Comment(
        user_comment='This song never gets old. Why is that? Because \
            Monsta X songs are all iconic. Fight me.',
        username='Aaron Horton',
        user_Id=2,
        song_Id=10
    )

    comment_10_2 = Comment(
        user_comment='내 사촌은 당신을 광기까지 사랑합니다. 저는 모든 K-Pop을 \
            사랑하고 당신에게 좋은 삶을 기원합니다❤☺️',
        username='Douglas Klein',
        user_Id=3,
        song_Id=10
    )

    comment_11_1 = Comment(
        user_comment='He isn’t lying when he said that \
            “this k-pop category ain’t enough size for me”',
        username='Celia Hansen',
        user_Id=5,
        song_Id=11
    )

    comment_12_1 = Comment(
        user_comment='bad boy is the standard for girl crush songs, facts',
        username='Demo',
        user_Id=1,
        song_Id=12
    )

    comment_12_2 = Comment(
        user_comment='Power Up: sings about babananababananananana, \
            not a single banana in the music video. \n \
            Bad Boy: sings about a bad boy, not a single \
            boy in the music video',
        username='Julia Adkins',
        user_Id=4,
        song_Id=12
    )

    comment_13_1 = Comment(
        user_comment='JISOO HAVE MORE SCREEN TIME HERE RATHER THAN IN \
            BLACKPINK MV LOLLLLLL',
        username='Douglas Klein',
        user_Id=3,
        song_Id=13
    )

    comment_13_2 = Comment(
        user_comment='99% talking about jisoo👑 \n \
            \n \
            Me: “wHerE aRe tHe SuBtiTles?”',
        username='Julia Adkins',
        user_Id=4,
        song_Id=13
    )

    comment_13_3 = Comment(
        user_comment='Honestly, this song deserves much more views',
        username='Demo',
        user_Id=1,
        song_Id=13
    )

    comment_14_1 = Comment(
        user_comment='This song is the king of BTS songs.',
        username='Demo',
        user_Id=1,
        song_Id=14
    )

    comment_14_2 = Comment(
        user_comment='I will never be able to get over \
            Blood, Sweat and Tears.',
        username='Douglas Klein',
        user_Id=3,
        song_Id=14
    )

    comment_14_3 = Comment(
        user_comment='"yesterday is history" \n \
            "tomorrow is a mystery" \n \
            "today is a gift" \n \
            "thats why it called the presents"',
        username='Celia Hansen',
        user_Id=5,
        song_Id=14
    )

    db.session.add(comment_1_1)
    db.session.add(comment_1_2)
    db.session.add(comment_1_3)
    db.session.add(comment_2_1)
    db.session.add(comment_2_2)
    db.session.add(comment_3_1)
    db.session.add(comment_3_2)
    db.session.add(comment_3_3)
    db.session.add(comment_4_1)
    db.session.add(comment_4_2)
    db.session.add(comment_5_1)
    db.session.add(comment_5_2)
    db.session.add(comment_5_3)
    db.session.add(comment_6_1)
    db.session.add(comment_6_2)
    db.session.add(comment_6_3)
    db.session.add(comment_6_4)
    db.session.add(comment_7_1)
    db.session.add(comment_8_1)
    db.session.add(comment_8_2)
    db.session.add(comment_8_3)
    db.session.add(comment_9_1)
    db.session.add(comment_9_2)
    db.session.add(comment_10_1)
    db.session.add(comment_10_2)
    db.session.add(comment_11_1)
    db.session.add(comment_12_1)
    db.session.add(comment_12_2)
    db.session.add(comment_13_1)
    db.session.add(comment_13_2)
    db.session.add(comment_13_3)
    db.session.add(comment_14_1)
    db.session.add(comment_14_2)
    db.session.add(comment_14_3)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_comments():
    db.session.execute('TRUNCATE comments CASCADE;')
    db.session.commit()
