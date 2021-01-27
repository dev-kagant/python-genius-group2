from app.models import db
from app.models.song import Song
from app.models.user import User


def seed_songs():
    user2 = User.query.filter_by(username='Demo').first()

    demoSong = Song(
        artist='Itzy',
        title='Not Shy',
        album='Not Shy',
        written_by='J.Y. Park',
        label='JYP',
        song_bio='''
                    Not Shy was released as the lead single
                    from the album on August 17, 2020.
                    With total of 5 wins, 1 win on The Show
                    and Music Bank, and 3 in the MCountdown,
                    joining Blackpink as the girl group with
                    most Music Show wins (13 wins) and Triple
                    Crowns (3) in 2020. "Not Shy" also reached
                    the top-ten in South Korea, Singapore and
                    Malaysia. Itzy also became with Blackpink
                    the first and only girl groups to chart both
                    on Billboard Global 200 and Billboard Global
                    Excl. US Chart peaking at number 124 and 70
                    respectively.
                ''',
        lyrics= '''
                Not shy, not me (ITZY)
                난 다 원해 다다 (Yeah)
                Not shy, not me

                난 빨리빨리 원하는 걸 말해
                못 가지면 어때 괜히
                망설이다 시간만 가니
                Yeah 다 말할래 'cause I like it, 'cause I like it, like it
                기다려 왜? 기다려서 뭐해?
                내가 내 맘을 왜 (왜) 말하면 안 돼 yeah
                그냥 탁 그냥 탁탁탁탁탁
                Not shy to say I want you

                Hey there, hey there
                우리는 great pair, great pair
                네 맘이 뭔지 모르지만 ah 내 생각이
                맞아 그러니까 ah yeah yeah
                내 맘은 내 거 그러니까
                좋아한다고 자유니까
                네 맘은 네 거 맞으니까
                말해봐 다 어서 다 'cause I'm not shy

                Not shy, not me (ITZY)
                난 다 원해 다다 (Not shy)
                Not shy, not me
                Give me 다 다다다 다다 다다
                Not shy, not me (ITZY)
                난 다 원해 다다 (Not shy)
                Not shy, not me
                너를 원해 뭐 어때 'cause I'm not shy

                넌 빨리빨리 대답할 필욘 없어
                어차피 내 거니까 woo
                날 보고 있기만 하면 돼
                Yeah you will like it, 'cause you like it, 'cause you like it, like it
                내가 미워 아니라면 비워
                다른 건 다 지워 내가 네 only one, yeah
                그냥 싹 지워 싹싹싹싹싹
                Not shy to say I want you

                Hey there, hey there
                우리는 great pair, great pair
                네 맘이 뭔지 모르지만 ah 내 생각이
                맞아 그러니까 ah yeah yeah
                내 맘은 내 거 그러니까
                좋아한다고 자유니까
                네 맘은 네 거 맞으니까
                말해봐 다 어서 다 'cause I'm not shy

                Not shy, not me (ITZY)
                난 다 원해 다다 (Not shy)
                Not shy, not me
                Give me 다 다다다 다다 다다
                Not shy, not me (ITZY)
                난 다 원해 다다 (Not shy)
                Not shy, not me
                너를 원해 뭐 어때 'cause I'm not shy

                후회하긴 싫으니까
                엔딩 상관없으니까
                Go go go 모두 쏟아내
                No yes no 뭐든지 어때
                Yeah 이러면 저러면 어때
                어차피 안 될 거 빼고 다 돼
                Let's just be who we are
                Do what we do 네 맘대로 해
                Let the beat drop

                Not shy, not me (ITZY)
                난 다 원해 다다 (Not shy)
                Not shy, not me
                말해봐 다 어서 다 'cause I'm not shy

                Not shy, not me (ITZY)
                난 다 원해 다다 (Not shy)
                Not shy, not me
                Give me 다 다다다 다다 다다
                Not shy, not me (ITZY)
                난 다 원해 다다 (Not shy)
                Not shy, not me
                너를 원해 뭐 어때 'cause I'm not shy
                Not shy, not me
                ''',
        song_url='https://soundcloud.com/wiktoria-filipowska-879194668/itzy-not-shy',
        media_url='https://www.youtube.com/watch?v=wTowEKjDGkU',
        song_icon='https://www.catchopcd.net/8554-large_default/itzy-not-shy-album.jpg',
        song_background_image='https://cdn.smehost.net/dailyrindblogcom-orchardprod/wp-content/uploads/2020/08/ITZY_Banner-scaled.jpg',
        release_date='2020-8-17',
        user_Id= user2.id)

    demoSong2 = Song(
        artist='BlackPink',
        title='How You Like That',
        album='The Album',
        written_by='Teddy Park, Danny Chung, R. Tee',
        label='YG',
        song_bio='''
            "How You Like That" is a song recorded by
            South Korean girl group Blackpink.
            It was released on June 26, 2020,
            through YG and Interscope,
            as the lead single from the group's
            first Korean-language studio album,
            The Album, released on October 2, 2020.
            The track was written by Danny Chung and
            Teddy Park, with the latter as well as
            R. Tee and 24 credited as arrangers,
            and Teddy as producer.
            "How You Like That" is a pop, hip hop and
            trap track about "not being daunted by
            dark situations and to not lose the
            confidence and strength to stand up again"
        ''',
        lyrics='''
            BLACKPINK in your area

            보란 듯이 무너졌어
            바닥을 뚫고 저 지하까지
            옷 끝자락 잡겠다고
            저 높이 두 손을 뻗어 봐도

            다시 캄캄한 이곳에 light up the sky
            네 두 눈을 보며 I'll kiss you goodbye
            실컷 비웃어라 꼴 좋으니까
            이제 너희 하나 둘 셋

            Ho-how you like that?
            You gon' like that, that-that-that-that, that-that-that-that
            How you like that? (Bada-bing, bada-boom-boom-boom)
            How you like that, that-that-that-that, that-that-that-that?

            Now look at you, now look at me, look at you, now look at me
            Look at you, now look at me, how you like that?
            Now look at you, now look at me, look at you, now look at me
            Look at you, now look at me, how you like that?

            Your girl need it all and that's a 100 백 개 중에 백 내 몫을 원해
            Karma come and get some 딱하지만 어쩔 수 없잖아
            What's up? I'm right back 방아쇠를 cock back
            Plain Jane get hijacked, don't like me?
            Then tell me how you like that, like that

            더 캄캄한 이곳에 shine like the stars
            그 미소를 띠며 I'll kiss you goodbye
            실컷 비웃어라 꼴 좋으니까
            이제 너희 하나 둘 셋

            Ho- how you like that?
            You gon' like that, that-that-that-that, that-that-that-that
            How you like that? (Bada-bing, bada-boom-boom-boom)
            How you like that, that-that-that-that, that-that-that-that?

            Now look at you, now look at me, look at you, now look at me
            Look at you, now look at me, how you like that?
            Now look at you, now look at me, look at you, now look at me
            Look at you, now look at me, how you like that?

            날개 잃은 채로 추락했던 날
            어두운 나날 속에 갇혀 있던 날
            그 때쯤에 넌 날 끝내야 했어
            Look up in the sky, it's a bird, it's a plane

            Yeah-eah-eah-eah
            Bring out your boss, bitch
            Yeah-eah-eah-eah
            BLACKPINK
            뚜뚜뚜뚜두두, 뚜뚜뚜뚜두두 (how you like that?)
            뚜뚜뚜뚜두두, 뚜뚜뚜뚜두두두 (you gon' like that)
            뚜뚜뚜뚜두두, 뚜뚜뚜뚜두두 (how you like that?)
            뚜뚜뚜뚜두두, 뚜뚜뚜뚜두두두
        ''',
        song_url='https://soundcloud.com/laila-blox/blackpink-how-you-like-that-2',
        media_url='https://www.youtube.com/watch?v=ioNng23DkIM',
        song_icon='https://6.viki.io/image/fc999f167ea74e06916604a994e438b0.jpeg?s=900x600&e=t',
        song_background_image='https://cdn.shopify.com/s/files/1/0273/8923/1139/collections/blackpink-banner-ice-cream-1600x400.jpg?v=1601367701',
        release_date='2020-7-17',
        user_Id= user2.id)

    db.session.add(demoSong)
    db.session.add(demoSong2)

    db.session.commit()


def undo_songs():
    db.session.execute('TRUNCATE songs CASCADE;')
    db.session.commit()
