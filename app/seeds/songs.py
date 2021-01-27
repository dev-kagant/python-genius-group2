from app.models import db
from app.models.song import Song
from app.models.user import User


def seed_songs():
    user2 = User.query.filter_by(username='Demo').first()

    itzy = Song(
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

    blackpink = Song(
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
        song_url='https://soundcloud.com/blackpinkofficial/how-you-like-that',
        media_url='https://www.youtube.com/watch?v=ioNng23DkIM',
        song_icon='https://6.viki.io/image/fc999f167ea74e06916604a994e438b0.jpeg?s=900x600&e=t',
        song_background_image='https://cdn.shopify.com/s/files/1/0273/8923/1139/collections/blackpink-banner-ice-cream-1600x400.jpg?v=1601367701',
        release_date='2020-7-17',
        user_Id= user2.id)

    BigBang = Song(
        artist="BIGBANG",
        title="FXXK IT",
        album="Made",
        written_by="Teddy, G-Dragon, T.O.P",
        label="YG",
        song_bio='''
            "Fxxk It" is a song recorded by
            South Korean boy band Big Bang.
            It was released digitally on
            December 12, 2016, by YG Entertainment,
            as the fifth single from Made (2016).
            The song was written by Teddy and by
            group members G-Dragon and T.O.P and
            produced by the first two with R.Tee.
            "Fxxk It" received positive reviews and
            was the group's ninth song to peak at
            number one on South Korea's Gaon Digital
            Chart and sixth to reached the Top 10
            on the Japan Hot 100.
        ''',
        lyrics='''
            No, I don't wanna go too fast (too fast)
            No, 'cause nothing really lasts, yeah
            I think I need some time
            But I can't get you off my mind
            No, no, no, no

            Oh, 일단 시작부터 제일 센 걸로 부탁해 바텐더
            연속해 들이키고 나니 모두 다 예뻐
            보여 침이 고여 these ladies so loyal
            그러다 널 처음 봤어
            Geez girl, love me tender

            난 씩씩하게 말을 걸어
            넌 저기 시시한 여자와는 달리 틱틱 거려
            칙칙하던 분위기에 한 줄기 빛
            설렘 정도가 지나쳐 마치 사춘기

            훔치는 너의 눈빛에
            입술은 바짝 마르지
            오랜만에 느껴보는 이런 떨림
            이러지도 저러지도 못해 나
            이 밤이 다 가기 전에
            난 널 내 품 안에 원해
            Real love? I think I wanna just
            고민고민 하지마 hey

            에라 모르겠다 I love y'all
            에라 모르겠다 I love y'all
            에라 모르겠다 I love y'all
            Girl, I wanna get down
            에라 모르겠다 (down)
            에라 모르겠다 (down)
            에라 모르겠다 (down, down, down)
            Girl, I wanna get down

            설렘을 찾고 싶어 마르고 닳도록
            난 여러 명의 포로
            도망치네 이곳 빠삐용
            나 지긋지긋 희끗희끗 흰머리가 나
            양아치 이제 끝
            바람둥이 한 가닥

            나라는 남자를 모르던 좀 그런 네가 좋았지
            몰래 난 원래 모든 girl 싫증 잘 느끼는 벌레
            나이를 먹어도 사랑은 단 1도 모르겠어

            뒤처리를 못해
            피눈물 없는 로맨스 장단 없는 game
            너는 오락가락하고
            멜로디가 다른 알토와 소프라노
            어차피 우리는 끊어질 거야
            딱 잘라 말할게
            타락해버린 꿈에 Eldorado

            훔치는 너의 눈빛에
            입술은 바짝 마르지
            오랜만에 느껴보는 이런 떨림
            이러지도 저러지도 못해 나
            이 밤이 다 가기 전에
            난 널 내 품 안에 원해
            Real love? I think I wanna just
            고민고민 하지마 hey

            에라 모르겠다 I love y'all
            에라 모르겠다 I love y'all
            에라 모르겠다 I love y'all
            Girl, I wanna get down
            에라 모르겠다 (down, down)
            에라 모르겠다 (down, down)
            에라 모르겠다 (down, down)
            Girl, I wanna get down

            You and me
            같이 차를 타고 ride
            술 취했으니 눈 좀 붙여 잠깐만
            어디 가서 쉴까 baby 난 손만 잡고 자
            속은 뻔해 honey, honey
            But I want it and you know it

            에라 모르겠다 I love y'all
            에라 모르겠다 I love y'all
            에라 모르겠다 에라 모르겠다
            에라 모르겠다
            에라 모르겠다
            에라 모르겠다
            Girl, I wanna get down
            Girl, I wanna get down
            Girl, I wanna get down

            에라 모르겠다 I love y'all
            에라 모르겠다 I love y'all
            에라 모르겠다 I love y'all
            Girl, I wanna get down
            에라 모르겠다 (down, down)
            에라 모르겠다 (down, down)
            에라 모르겠다 (down, down)
            Girl, I wanna get down
        ''',
        song_url="https://soundcloud.com/schwd/fxxk-it-bigbang",
        media_url="https://www.youtube.com/watch?v=iIPH8LFYFRk",
        song_icon="https://pm1.narvii.com/6304/5628eeec5856de161794652586cc1c88c1c310b0_hq.jpg",
        song_background_image="https://bigbangisforever.files.wordpress.com/2012/12/cropped-banner_.jpg",
        release_date="2016-12-12",
        user_Id= user2.id
    )

    Ugh = Song(
        artist="BTS",
        title="Ugh!",
        album="Map of the Soul: 7",
        written_by="Supreme Boi, Suga, RM, Hiss Noise, J-Hope, Icecream Drum",
        label="Big Hit Entertainment",
        song_bio='''
            "UGH!" (욱) is a song by RM, Suga and J-Hope
            (also known as the rap-line) of BTS. It was
            released on February 21, 2020, and appears
            as the twelfth track in their fourth studio
            album Map of the Soul: 7.
        ''',
        lyrics='''
            타닥 또 타오르는 저 불씨
            기름에 닿기 전에 먼저 집어삼키네
            필시 휩쓸려가겠지 예 예 음
            오늘의 선수 (선수) 입장하시네 건수를 yeah (건수)
            물기 시작하면 둥둥둥 동네북이 돼 둥둥둥 (둥둥)
            툭툭 건드네 괜시리 툭툭 yeah (툭툭)
            반응이 없음 걍 담궈버리지 푹푹 yeah (푹푹)
            진실도 거짓이 돼
            거짓도 진실이 돼
            이곳에선 모두가 도덕적 사고와
            판단이 완벽한 사람이 돼 웃기시네

            분노? 물론 필요하지
            타오를 땐 이유가 있으
            어쩌면 우리의 역사지
            그게 세상을 바꾸기도 하지
            But 이건 분노 아닌 분뇨
            뭐가 분노인지 you know?
            분노인 척하며 죽여 진짜 분노
            질려버린 수도 없이 많은 people
            넌 나만 죽이는 게 아니야 (아니야)
            똥 밟는 게 익숙해 우리야 (우리야)
            무감각해진 저 사람들 봐 (사람들 봐)
            분뇨, 무관심 너넨 팀이야 eh

            나는 욱해 욱해
            나는 욱해 욱해
            나는 악의에 가득 찬 분노에 분노해
            나는 악의에 가득 찬 분노에 분노해 (yeh yeh)

            나는 욱해 욱해
            나는 욱해 욱해
            나는 꺼져야만 했던 분노에 분노해
            나는 꺼져야만 했던 그 분노에 분노해 (yeh yeh)

            그래 욱 욱 욱 욱 욱해라 욱 욱
            재가 될 때까지 그래 욱해라 욱
            그래 욱 욱 욱 욱 욱해라 욱 욱
            부러질 때까지 그래 욱해라 욱

            나는 욱해 (욱해) 욱해 yeah
            나는 욱해 (욱해) 욱해 yeah
            나는 악의에 가득 찬 분노에 분노해
            나는 꺼져야만 했던 그 분노에 분노해 hey
            이 세상 (hi) 분노가 지배함 (hi hi)
            분노가 없음 다 못 사나 봐 (hi hi)
            분노하고 또 분노하고 분노하고 (hi hi)
            그리 미쳐가고 (hi) 욱 욱 욱 욱
            분노하는 이유도 다 수만 가지
            선의와 악의도 다 매한가지
            분노할 수 있다만 남의 삶에
            피해가 있는 건 I don't like
            그건 stop ay
            누구의 행동에 (eh) 누구는 아파해
            누구의 언행에 (eh) 누구는 암담해 (eh)
            누구의 찰나에 누구 순간이 돼
            누구의 분노에 누구 목숨이 돼 썩을 퉤

            나는 욱해 (욱해) 욱해 yeah
            나는 욱해 (욱해) 욱해 yeah
            나는 악의에 가득 찬 분노에 분노해
            나는 꺼져야만 했던 그 분노에 분노해 (skrrt)

            아 대체 욕 좀 먹는 게 왜 (게 왜)
            잘 벌잖아 또 징징대 왜 (대 왜)
            그 정돈 감수해야지 에헴
            에헴 에헴 에헴 에헴 니네 에헴
            에헴 에헴 에헴
            나 시켰어봐 다 참아
            니네 에헴 니네 에헴 에헴 에헴 에헴
            나 시켰어봐 그냥 에헴 비헴 에헴

            그래 욱 (욱) 욱 (욱) 욱해라 욱 (욱)
            재가 될 때까지 그래 욱해라 욱 (욱)
            그래 욱 (욱) 욱 (욱) 욱해라 욱 (욱)
            부러질 때까지 그래 욱해라 욱 (욱)

            나는 욱해 (욱해) 욱해
            나는 욱해 (욱해) 욱해
            나는 악의에 가득 찬 분노에 분노해
            나는 꺼져야만 했던 그 분노에 분노해 hey hey, let's go
        ''',
        song_url="https://soundcloud.com/l2share97/ugh",
        media_url="https://www.youtube.com/watch?v=N4Xm7SIqEQ4",
        song_icon="https://mir-s3-cdn-cf.behance.net/projects/404/e1b257106253665.5f8c0600505ee.jpg",
        song_background_image="https://i.pinimg.com/originals/73/05/b9/7305b9ed0679581860282254eac3361b.jpg",
        release_date="2020-02-21",
        user_Id= user2.id
    )

    BlackSwan = Song(
        artist="BTS",
        title="Black Swan",
        album="Map of the Soul: 7",
        written_by="Pdogg, RM, August Rigo, Vince Nantes, Clyde Kelly",
        label="Bit Hit Entertainment",
        song_bio='''
            "Black Swan" is the ninth digital single
            by BTS. It was released on January 17, 2020,
            as a pre-release single for their fourth
            studio album Map of the Soul: 7.
            This song also has a Japanese version
            featured in their fourth Japanese studio
            album Map of the Soul: 7 ~The Journey~.
        ''',
        lyrics='''
            Do your thang, do your thang with me now
            Do your thang, do your thang with me now
            What's my thang? What's my thang? Tell me now
            Tell me now, yeah, yeah, yeah, yeah

            Ayy 심장이 뛰지 않는대
            더는 음악을 들을 때 tryna pull up
            시간이 멈춘 듯해
            Oh, that would be my first death I've been always afraid of
            이게 나를 더 못 울린다면
            내 가슴을 더 떨리게 못 한다면
            어쩜 이렇게 한 번 죽겠지 아마
            But what if that moment's right now, right now?

            귓가엔 느린 심장 소리만 bump, bump, bump
            벗어날래도 그 입속으로 jump, jump, jump
            어떤 노래도 와닿지 못해 소리 없는 소릴 질러

            모든 빛이 침묵하는 바다 yeah, yeah, yeah
            길 잃은 내 발목을 또 잡아 yeah, yeah, yeah
            어떤 소리도 들리지 않아 yeah, yeah, yeah
            Killin' me now, killin' me now, do you hear me? Yeah

            홀린 듯 천천히 가라앉아 nah, nah, nah
            몸부림쳐봐도 사방이 바닥 nah, nah
            모든 순간들이 영원이 돼 yeah, yeah, yeah
            Film it now, film it now, do you hear me? Yeah

            Do your thang, do your thang with me now
            Do your thang, do your thang with me now
            What's my thang? What's my thang? Tell me now
            Tell me now, yeah, yeah, yeah, yeah

            Deeper, yeah, I think I'm goin' deeper
            자꾸 초점을 잃어 이젠 놓아줘 싫어
            차라리 내 발로 갈게 내가 뛰어들어갈게
            가장 깊은 곳에서 나는 날 봤어
            천천히 난 눈을 떠 여긴 나의 작업실 내 스튜디오
            거센 파도 깜깜하게 나를 스쳐도
            절대 끌려가지 않을 거야 다시 또
            Inside, I saw myself, myself

            귓가엔 빠른 심장 소리만 bump, bump, bump
            두 눈을 뜨고 나의 숲으로 jump, jump, jump
            그 무엇도 날 삼킬 수 없어 힘껏 나는 소리 질러

            모든 빛이 침묵하는 바다 yeah, yeah, yeah
            길 잃은 내 발목을 또 잡아 yeah, yeah, yeah
            어떤 소리도 들리지 않아 yeah, yeah, yeah
            Killin' me now, killin' me now, do you hear me? Yeah
            홀린 듯 천천히 가라앉아 nah, nah, nah
            몸부림쳐봐도 사방이 바닥 nah, nah
            모든 순간들이 영원이 돼 yeah, yeah, yeah
            Film it now, film it now, do you hear me? Yeah

            Do your thang, do your thang with me now
            Do your thang, do your thang with me now
            What's my thang? What's my thang? Tell me now
            Tell me now, yeah, yeah, yeah, yeah
        ''',
        song_url="https://soundcloud.com/cutiust/bts-black-swan-orchestra-ver",
        media_url="https://www.youtube.com/watch?v=0lapF4DQPKQ",
        song_icon="https://www.mtvpersian.net/main/uploads/covers/main1/BTS%20-%20Black%20Swan.jpg",
        song_background_image="https://i.pinimg.com/736x/e3/ed/bd/e3edbdde5bae41ffdc7f01a939b8e94a.jpg",
        release_date="2020-01-17",
        user_Id= user2.id
    )

    EXO = Song(
        artist="EXO",
        title="The Eve",
        album="The War",
        written_by="Hwang Yoo-bin",
        label="SM",
        song_bio='''
            The War (stylized in all caps) is the
            fourth studio album by South Korean–Chinese
            boy band Exo. It was released digitally on
            July 18, 2017 and physically on July 19, 2017
            by SM Entertainment under Genie Music's
            distribution. The album includes a total
            of nine tracks including the lead single
            "Ko Ko Bop". The War received the highest
            number of pre-orders at the time for a K-pop
            album, with more than 800,000 physical copies.
            24 days after being released, it became Exo's
            fourth consecutive studio album to have sold
            over a million copies.[2] The album was re-released
            under the title The War: The Power of Music on
            September 5, 2017.[3] This was the first Exo
            release not to feature member Lay, who began an
            indefinite hiatus shortly before the music video
            for "Ko Ko Bop" was filmed,[4] and the last album
            to be separately released in both Korean and
            Chinese language.
        ''',
        lyrics='''
            똑바로 봐 What's the situation
            당황한 너의 시선 너머
            끝내 무너지는 성벽
            차츰 밝아오는 새벽 Yeah uh

            끝없이 이어지고 있어
            무딘 칼날 끝에 잘라내지 못해
            계속 반복되는 문제 Yeah
            미처 풀지 못한 숙제

            높은 벽 앞에 스러지던
            작고 약한 바람 소리가
            뒤엉켜 폭풍처럼 몰아치는
            소릴 들어봐

            깨고 부딪쳐야 해
            우릴 볼 수 있도록
            크게 소리쳐야 해
            멀리 번져가도록
            여린 빛들이 번져가
            긴 어둠을 다 몰아낸 순간
            다시 깨어나야 해
            새로워진 아침에

            오만한 시선들로 날 봐
            이미 다른 출발선 위에 앉아
            까마득한 거리 Yeah
            닿지 않을 듯한 외침

            짓밟힌 채로 자라나던
            간절한 수많은 꿈들이
            보란 듯 담장 너머 피워낸
            풍경을 바라봐

            깨고 부딪쳐야 해
            우릴 볼 수 있도록
            크게 소리쳐야 해
            멀리 번져가도록
            여린 빛들이 번져가
            긴 어둠을 다 몰아낸 순간
            다시 깨어나야 해
            새로워진 아침에

            왜곡되는 진실 가르쳐진 거짓
            변화의 목소리 파도가 일어
            전부 집어삼킬 바다를 만든 건 It's you

            깨고 부딪쳐야 해
            우릴 볼 수 있도록
            크게 소리쳐야 해
            멀리 번져가도록
            여린 빛들이 번져가
            긴 어둠을 다 몰아낸 순간
            다시 깨어나야 해
            새로워진 아침에
        ''',
        song_url="https://soundcloud.com/thipsuda-wu/exo-the-eve-1",
        media_url="https://www.youtube.com/watch?v=b6ycw7p9-bE",
        song_icon="https://upload.wikimedia.org/wikipedia/en/c/c7/ThewarEXO.jpeg",
        song_background_image="https://exoforeverone.weebly.com/uploads/4/0/8/5/40853551/557924_orig.jpg",
        release_date="2017-07-18",
        user_Id= user2.id
    )

    BEST = Song(
        artist="2NE1",
        title="I Am the Best",
        album="2NE1",
        written_by="Teddy Park",
        label="YG",
        song_bio='''
            "I Am the Best" (Korean: 내가 제일 잘 나가;
            RR: Naega jeil jal naga) is a song recorded
            by South Korean girl group 2NE1 for their
            self-titled second EP. The song was written
            and produced by the group's long-time collaborator
            Teddy Park and was released for digital download
            as the third single from the EP on June 24, 2011,
            under YG Entertainment. It is an empowerment
            anthem, combining elements of electro house,
            electronic and hip hop, complete with
            instrumentations of synthesizers, middle
            eastern inspired rifts, and empowering chants.
        ''',
        lyrics='''
            내가 제일 잘 나가
            내가 제일 잘 나가
            내가 제일 잘 나가
            내가 제일 잘 나가
            내가 제일 잘 나가
            Bam Ratatata Tatatatata
            Bam Ratatata Tatatatata
            Bam Ratatata Tatatatata
            Bam Ratatata Tatatatata
            Oh my god

            누가 봐도 내가 좀 죽여주잖아
            둘째가라면 이 몸이 서럽잖아
            넌 뒤를 따라오지만 난 앞만 보고 질주해
            네가 앉은 테이블 위를 뛰어다녀 I don't care

            건드리면 감당 못해 I'm hot hot hot hot fire
            뒤집어지기 전에 제발 누가 날 좀 말려
            옷장을 열어 가장 상큼한 옷을 걸치고
            거울에 비친 내 얼굴을 꼼꼼히 살피고

            지금은 8시 약속시간은 8시반
            도도한 걸음으로 나선 이 밤

            내가 제일 잘 나가

            내가 제일 잘 나가
            내가 제일 잘 나가
            내가 제일 잘 나가
            제일 잘 나가
            내가 봐도 내가 좀 끝내주잖아
            네가 나라도 이 몸이 부럽잖아
            남자들은 날 돌아보고 여자들은 따라해

            내가 앉은 이 자리를 매일 넘봐 피곤해
            선수인척 폼만 잡는 어리버리한 Playa
            넌 바람 빠진 타이어처럼 보기 좋게 차여
            어떤 비교도 난 거부해 이건 겸손한 얘기
            가치를 논하자면 나는 Billion dollar baby

            뭘 쫌 아는 사람들은 다 알아서 알아봐
            아무나 잡고 물어봐 누가 제일 잘 나가
            내가 제일 잘 나가
            내가 제일 잘 나가

            내가 제일 잘 나가
            내가 제일 잘 나가
            제일 잘 나가
            누가 네가 나보다 더 잘 나가

            No no no no
            Na na na na
            누가 네가 나보다 더 잘 나가
            No no no no

            Na na na na
            누가 네가 나보다 더 잘 나가
            No no no no
            Na na na na
            누가 네가 나보다 더 잘 나가
            No no no no
            Na na na na
            Bam Ratatata Tatatatata
            Bam Ratatata Tatatatata
            Bam Ratatata Tatatatata
            Bam Ratatata Tatatatata
            Oh my god
        ''',
        song_url="https://soundcloud.com/cocokiitie/2ne1-i-am-the-best",
        media_url="https://www.youtube.com/watch?v=j7_lSP8Vc3o",
        song_icon="https://simplyromanji.files.wordpress.com/2012/03/2ne1.jpg",
        song_background_image="https://www.f-covers.com/cover/2ne1-facebook-cover-timeline-banner-for-fb.jpg",
        release_date="2011-06-24",
        user_Id= user2.id
    )

    CherryBomb = Song(
        artist="NCT 127",
        title="Cherry Bomb",
        album="Cherry Bomb",
        written_by="Taeyong, Mark, Deepflow, Lim Jung-hyo, Oh Min-joo",
        label="SM",
        song_bio='''
            Cherry Bomb is the third extended play by NCT 127,
            the Seoul-based sub-unit of the South Korean boy
            group NCT. It was released by SM Entertainment on
            June 14, 2017 and distributed by Genie Music.
            The EP includes a total of seven tracks.[1][2]

            The EP was a commercial success peaking at number
            two on the Gaon Album Chart. It has sold over
            127,642 physical copies as of December 2017.
        ''',
        lyrics='''
            빨리빨리 피해 right
            Cherry bomb feel it yum
            빨리빨리 피해 right
            Cherry bomb feel it yum
            빨리빨리 피해 right
            Cherry bomb feel it yum
            빨리빨리 피해 right
            Cherry bomb feel it yum
            I'm the biggest hit
            I'm the biggest hit on this stage
            I'm the biggest hit
            I'm the biggest hit on this stage
            I'm the biggest hit
            I'm the biggest hit on this stage
            I'm the biggest hit
            I'm the biggest hit on this stage

            시간이 됐지 반드시
            I'ma do my thing
            대기실 앞은 바글거려 다들 눈 못 떼
            모두 따라와 yo hands up in the air
            We back get away
            이제 막 터질거야 everywhere

            나를 삼켜봐 그리곤 느낀
            Stomach 꽤 오래 절여진 cherry bomb
            언제 언제 터질지 몰라
            Popping your head like 킹스맨 chip
            No fireman 이건 fireworks
            Cherries in the sky high

            I'm the biggest hit
            I'm the biggest hit on this stage
            I'm the biggest hit
            I'm the biggest hit on this stage

            If you are happy and you know it, clap your hands yo (in this beat)
            If you are happy and you know it, clap your hands (in this beat)

            빨리빨리 피해 right
            Cherry bomb feel it yum
            빨리빨리 피해 right
            Cherry bomb feel it yum
            빨리빨리 피해 right
            Cherry bomb feel it yum
            빨리빨리 피해 right
            Cherry bomb

            I'm the biggest hit
            I'm the biggest hit

            모두 다 쉿
            터지기 직전의 스릴
            It tastes like a cherry bomb
            쉽게 보다가는 큰일 나
            이미 넌 빠져들어 가
            팽창하는 지금 폭발 직전인 기분
            죽이네 do do that
            노랠 불러야지 na na na
            꽂힌 안전핀들 다 뽑아냈지
            다 깜짝 놀라겠지 모두가 we gonna make it

            I'm the biggest hit
            I'm the biggest hit on this stage
            I'm the biggest hit
            I'm the biggest hit on this stage

            If you are happy and you know it, clap your hands yo (in this beat)
            If you are happy and you know it, clap your hands (in this beat)

            빨리빨리 피해 right
            Cherry bomb feel it yum
            빨리빨리 피해 right
            Cherry bomb feel it yum
            빨리빨리 피해 right
            Cherry bomb feel it yum
            빨리빨리 피해 right

            끝이 어디인지 어디까지 갈 수 있는지 (yeah, yeah)
            이제 시작해 just the half of it
            뒷걸음질 치는 모습 it's over
            떠들기 바쁜 세상 속에 갇혀 헤매고 싶지는 않아
            단 한번의 불꽃으로 내 전불 태워
            I'm the biggest hit
            I'm the biggest hit, yeah

            Uh, hard rock scalp
            Head shot pop
            No talk 어딜가나 숙이는 삶
            주변 탐색하는 자들께 박수
            Ay 너네 덕에 분명히 정신을 차렸네
            쫓기는 거 싫어서 이젠 앞에서 말해
            허리는 너 앞에서 안 굽힐게
            Keep watching 맨날 보기를 바래
            Hater hater talk talk
            뭘 먹어도 너네껀 소화 잘돼 take a fist or stone or a gunshot
            독해져버린 Nine 받아봐 cherry bomb

            I'm the biggest hit
            I'm the biggest hit on this stage
            I'm the biggest hit
            I'm the biggest hit on this stage

            Yeah
            If you are happy and you know it, clap your hands yo (in this beat)
            If you are happy and you know it, clap your hands
            If you are happy and you know it, clap your hands yeah

            빨리빨리 피해 right
            Cherry bomb feel it yum
            빨리빨리 피해 right
            Cherry bomb feel it yum
            빨리빨리 피해 right
            Cherry bomb feel it yum
            빨리빨리 피해 right
            Cherry bomb feel it yum

            Na na na na na na
            I'm the biggest hit
            I'm the biggest hit on this stage
            Na na na na na na
            I'm the biggest hit
            I'm the biggest hit on this stage

            Na na na na na na
            어서 빨리 피해 right cherry bomb
            Na na na na na na
            어서 빨리 피해 right cherry bomb

            I'm the biggest hit
            I'm the biggest hit on this stage
        ''',
        song_url="https://soundcloud.com/user-734278856/nct-127-cherry-bomb-the-3rd-mini-album-full-album",
        media_url="https://www.youtube.com/watch?v=WkuHLzMMTZM",
        song_icon="https://upload.wikimedia.org/wikipedia/en/thumb/a/a7/Cherrybomb-nct.jpg/220px-Cherrybomb-nct.jpg",
        song_background_image="https://i.pinimg.com/originals/27/ef/50/27ef5092b55498f05973f12e6a4130aa.jpg",
        release_date="2017-06-14",
        user_Id= user2.id
    )

    # BigBang = Song(
    #     artist="",
    #     title="",
    #     album="",
    #     written_by="",
    #     label="",
    #     song_bio='''

    #     ''',
    #     lyrics='''

    #     ''',
    #     song_url="",
    #     media_url="",
    #     song_icon="",
    #     song_background_image="",
    #     release_date="",
    #     user_Id= user2.id
    # )

    db.session.add(itzy)
    db.session.add(blackpink)
    db.session.add(BigBang)
    db.session.add(Ugh)
    db.session.add(BlackSwan)
    db.session.add(EXO)
    db.session.add(BEST)
    db.session.add(CherryBomb)

    db.session.commit()


def undo_songs():
    db.session.execute('TRUNCATE songs CASCADE;')
    db.session.commit()
