from app.models import db, Annotation


# Adds a demo user, you can add other users here if you want
def seed_annotations():

    notShy = Annotation(
        lyrics='Not shy, not me',
        annotation='Not Shy - Annotation feature demo',
        start=41,
        end=56,
        user_Id=1,
        song_Id=1
    )

    notShy2 = Annotation(
        lyrics='기다려 왜? 기다려서 뭐해? 내가 내 맘을 왜 (왜) 말하면 안 돼 yeah',
        annotation='Not Shy - Annotation feature demo',
        start=97,
        end=139,
        user_Id=1,
        song_Id=1
    )

    howYouLikeThat = Annotation(
        lyrics='저 높이 두 손을 뻗어 봐도',
        annotation='How You Like That - Annotation feature demo',
        start=60,
        end=75,
        user_Id=1,
        song_Id=2
    )

    fxxkIt = Annotation(
        lyrics='cause nothing really lasts',
        annotation='Fxxk It - Annotation feature demo',
        start=46,
        end=72,
        user_Id=1,
        song_Id=3
    )

    ugh = Annotation(
        lyrics='오늘의 선수 (선수) 입장하시네 건수를 yeah (건수)',
        annotation='Ugh! - Annotation feature demo',
        start=50,
        end=81,
        user_Id=1,
        song_Id=4
    )

    blackSwan = Annotation(
        lyrics='Oh, that would be my first death I\'ve been always afraid of',
        annotation='Black Swan - Annotation feature demo',
        start=216,
        end=275,
        user_Id=1,
        song_Id=5
    )

    blackSwan = Annotation(
        lyrics='Oh, that would be my first death I\'ve been always afraid of',
        annotation='Black Swan - Annotation feature demo',
        start=216,
        end=275,
        user_Id=1,
        song_Id=5
    )

    theEve = Annotation(
        lyrics='끝내 무너지는 성벽',
        annotation='The Eve - Annotation feature demo',
        start=40,
        end=50,
        user_Id=1,
        song_Id=6
    )

    iAmTheBest = Annotation(
        lyrics='네가 앉은 테이블 위를 뛰어다녀 I don\'t care',
        annotation='I Am the Best - Annotation feature demo',
        start=218,
        end=248,
        user_Id=1,
        song_Id=7
    )

    cherryBomb = Annotation(
        lyrics='Cherry bomb feel it yum',
        annotation='Cherry Bomb - Annotation feature demo',
        start=14,
        end=37,
        user_Id=1,
        song_Id=8
    )

    justRight = Annotation(
        lyrics='거울아 거울아 제발 좀 말해주려무나',
        annotation='Just Right - Annotation feature demo',
        start=50,
        end=69,
        user_Id=1,
        song_Id=9
    )

    hero = Annotation(
        lyrics='가식뿐인 늑대 같은 남자들',
        annotation='Hero - Annotation feature demo',
        start=45,
        end=59,
        user_Id=1,
        song_Id=10
    )

    agustD = Annotation(
        lyrics='어떤 이는 내가 이 자릴 쉽게 앉았다고 해',
        annotation='Agust D - Annotation feature demo',
        start=156,
        end=179,
        user_Id=1,
        song_Id=11
    )

    badBoy = Annotation(
        lyrics='내 호기심을 자극하지',
        annotation='Bad Boy - Annotation feature demo',
        start=88,
        end=99,
        user_Id=1,
        song_Id=12
    )

    spoiler = Annotation(
        lyrics='아니라고 말해도 느껴지는 spoiler',
        annotation='Spoiler - Annotation feature demo',
        start=61,
        end=82,
        user_Id=1,
        song_Id=13
    )

    bloodSweatTears = Annotation(
        lyrics='Peaches and cream, sweeter than sweet Chocolate cheeks and chocolate wings',
        annotation='Blood Sweat & Tears - Annotation feature demo',
        start=186,
        end=260,
        user_Id=1,
        song_Id=14
    )

    db.session.add(notShy)
    db.session.add(notShy2)
    db.session.add(howYouLikeThat)
    db.session.add(fxxkIt)
    db.session.add(ugh)
    db.session.add(blackSwan)
    db.session.add(theEve)
    db.session.add(iAmTheBest)
    db.session.add(cherryBomb)
    db.session.add(justRight)
    db.session.add(hero)
    db.session.add(agustD)
    db.session.add(badBoy)
    db.session.add(spoiler)
    db.session.add(bloodSweatTears)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_annotations():
    db.session.execute('TRUNCATE annotations CASCADE;')
    db.session.commit()
