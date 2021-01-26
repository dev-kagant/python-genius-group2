from app.models import db
from app.models.user import Song, User


def seed_songs():
    user2 = User.query.filter_by(username='Demo').first()

    demoSong = Song(
        artist='Itzy',
        title='Not Shy',
        album='Not Shy',
        written_by='J.Y. Park',
        label='JYP',
        lyrics='Not shy, not me, Not shy, not me',
        song_url='https://soundcloud.com/wiktoria-filipowska-879194668/itzy-not-shy',
        media_url='https://www.youtube.com/watch?v=wTowEKjDGkU',
        song_icon='https://lab.fm/wp-content/uploads/2020/08/081820-ITZY-Not-Shy-JYP-YouTube.jpg',
        song_background_image='https://upload.wikimedia.org/wikipedia/en/9/9a/Itzy_-_Not_Shy.jpg',
        release_date='2020-8-17',
        user_Id= user2.id)

    demoSong2 = Song(
        artist='BlackPink',
        title='How You Like That',
        album='The Album',
        written_by='Teddy Park, Danny Chung, R. Tee',
        label='YG',
        lyrics='Ho-how you like that?, You gon like that, that-that-that-that, that-that-that-that, How you like that? (Bada-bing, bada-boom-boom-boom), How you like that, that-that-that-that, that-that-that-that?',
        song_url='https://soundcloud.com/laila-blox/blackpink-how-you-like-that-2',
        media_url='https://www.youtube.com/watch?v=ioNng23DkIM',
        song_icon='https://6.viki.io/image/fc999f167ea74e06916604a994e438b0.jpeg?s=900x600&e=t',
        song_background_image='https://upload.wikimedia.org/wikipedia/en/e/eb/Blackpink_-_How_You_Like_That.png',
        release_date='2020-7-17',
        user_Id= user2.id)

    db.session.add(demoSong)
    db.session.add(demoSong2)

    db.session.commit()


def undo_songs():
    db.session.execute('TRUNCATE songs CASCADE;')
    db.session.commit()
