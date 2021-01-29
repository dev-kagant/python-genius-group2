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
        song_bio='''Not Shy was released as the lead single from the album on August 17, 2020. With total of 5 wins, 1 win on The Show and Music Bank, and 3 in the MCountdown, joining Blackpink as the girl group with most Music Show wins (13 wins) and Triple Crowns (3) in 2020.

"Not Shy" also reached the top-ten in South Korea, Singapore and Malaysia. Itzy also became with Blackpink the first and only girl groups to chart both on Billboard Global 200 and Billboard Global Excl. US Chart peaking at number 124 and 70 respectively.
''',
        lyrics=''' Not shy, not me (ITZY)
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
        song_bio='''"How You Like That" is a song recorded by South Korean girl group Blackpink. It was released on June 26, 2020, through YG and Interscope, as the lead single from the group's first Korean-language studio album, The Album, released on October 2, 2020. 

The track was written by Danny Chung and Teddy Park, with the latter as well as R. Tee and 24 credited as arrangers, and Teddy as producer. "How You Like That" is a pop, hip hop and trap track about "not being daunted by dark situations and to not lose the confidence and strength to stand up again"
        ''',
        lyrics='''BLACKPINK in your area

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
        song_bio='''"Fxxk It" is a song recorded by South Korean boy band Big Bang. It was released digitally on December 12, 2016, by YG Entertainment, as the fifth single from Made (2016). 

The song was written by Teddy and by group members G-Dragon and T.O.P and produced by the first two with R.Tee. "Fxxk It" received positive reviews and was the group's ninth song to peak at number one on South Korea's Gaon Digital Chart and sixth to reached the Top 10 on the Japan Hot 100.
        ''',
        lyrics='''No, I don't wanna go too fast (too fast)
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
        song_bio='''"UGH!" (욱) is a song by RM, Suga and J-Hope (also known as the rap-line) of BTS. 

It was released on February 21, 2020, and appears as the twelfth track in their fourth studio album Map of the Soul: 7.
        ''',
        lyrics='''타닥 또 타오르는 저 불씨
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
        song_bio='''"Black Swan" is the ninth digital single by BTS. It was released on January 17, 2020, as a pre-release single for their fourth studio album Map of the Soul: 7. 

This song also has a Japanese version featured in their fourth Japanese studio album Map of the Soul: 7 ~The Journey~.
        ''',
        lyrics='''Do your thang, do your thang with me now
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
        song_bio='''The War (stylized in all caps) is the fourth studio album by South Korean–Chinese boy band Exo. It was released digitally on July 18, 2017 and physically on July 19, 2017 by SM Entertainment under Genie Music's distribution. 

The album includes a total of nine tracks including the lead single "Ko Ko Bop". The War received the highest number of pre-orders at the time for a K-pop album, with more than 800,000 physical copies. 24 days after being released, it became Exo's fourth consecutive studio album to have sold over a million copies. 

The album was re-released under the title The War: The Power of Music on September 5, 2017. This was the first Exo release not to feature member Lay, who began an indefinite hiatus shortly before the music video for "Ko Ko Bop" was filmed, and the last album to be separately released in both Korean and Chinese language.
        ''',
        lyrics='''똑바로 봐 What's the situation
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
        song_bio='''"I Am the Best" (Korean: 내가 제일 잘 나가; RR: Naega jeil jal naga) is a song recorded by South Korean girl group 2NE1 for their self-titled second EP. 

The song was written and produced by the group's long-time collaborator Teddy Park and was released for digital download as the third single from the EP on June 24, 2011, under YG Entertainment. 

It is an empowerment anthem, combining elements of electro house, electronic and hip hop, complete with instrumentations of synthesizers, middle eastern inspired rifts, and empowering chants.
        ''',
        lyrics='''내가 제일 잘 나가
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
        song_bio='''Cherry Bomb is the third extended play by NCT 127, the Seoul-based sub-unit of the South Korean boy group NCT. It was released by SM Entertainment on June 14, 2017 and distributed by Genie Music. The EP includes a total of seven tracks. The EP was a commercial success peaking at number two on the Gaon Album Chart. It has sold over 127,642 physical copies as of December 2017.
        ''',
        lyrics='''빨리빨리 피해 right
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

    Hero = Song(
        artist="Monsta X",
        title="Hero",
        album="Rush",
        written_by="Joohoney (MONSTA X), I.M (MONSTA X), Rhymer (라이머) & Punch Sound",
        label="Starship Entertainment",
        song_bio='''

        ''',
        lyrics='''하루 종일 널 지켜보면서 
발견한 유일한 문제점 yeah 
너를 귀찮게 만드는 
가식뿐인 늑대 같은 남자들 
아니야 넌 내껀데 
내가 지켜야 할 의무가 있는데 
누가 널 절대 넘볼 수 없게 
내가 지켜줄게 

넌 너무나 아름다워서 난 적이 많아 
마치 공주를 지키는 게임 같아 
걱정하지마 난 너만의 남자 
I can be your hero, I can be your hero 
I can be your hero 

I can be your hero, I can be your man 
I can be your hero, I can be your man 
I can be your hero, I can be your man 
I can be your hero, I can be your man 

I can be your hero 악당들은 뒤로 
나쁜 것들 포대기에 
싸맨 다음 트럭에 실어 
하나같이 다 짐승같아보여 
동물원에 버려 
전부 말들이 많어 널 가지려 
뱉어대는 개소리 (월월월) 
(What?) 만만하게 날 봤다면 
버섯 먹고 크게 자라 
바지 위에 팬티를 입고 망토를 달아 
수트도 가끔 입고 가슴에서 빛이나 
빛이나 우리가 빛이나 
다들 고개를 bow 

마지막 경고할게 
화나면 난리나 나 무섭게 변해 
누가 널 절대 넘볼 수 없게 
내가 지켜줄게 

넌 너무나 아름다워서 난 적이 많아 
마치 공주를 지키는 게임 같아 
걱정하지마 난 너만의 남자 
I can be your hero, I can be your hero 
I can be your hero 

I can be your hero, I can be your man 
I can be your hero, I can be your man 
I can be your hero, I can be your man 
I can be your hero, I can be your man 

Ay 난 너의 악당들을 
모두 하나같이 뱅 뱅 뱅 뱅 
하늘을 슝슝 
그냥 막 하늘을 날아다녀 슈퍼맨 
너의 입꼬리위에 매달려 웃음짓게 
만들어낼게 배트맨 
널 울게 만드는 그 어떤 악당들 
이제는 싹 다 꺼지라 할게요 

I can be your hero 

I can be your hero, I can be your man 
I can be your hero, I can be your man 
I can be your hero, I can be your man 
I can be your hero, I can be your man 
        ''',
        song_url="https://soundcloud.com/sisa-macikova/monsta-x-hero",
        media_url="https://www.youtube.com/watch?v=FZ9lJ5ctd0s",
        song_icon="https://t2.genius.com/unsafe/220x220/https%3A%2F%2Fimages.genius.com%2F7768f98750e4ac97b8864c4fdf41e1cf.600x600x1.jpg",
        song_background_image="https://t2.genius.com/unsafe/1470x280/https%3A%2F%2Fimages.rapgenius.com%2Fad43486e8c15fea53d55d7f3b20b7a0c.1000x666x1.jpg",
        release_date="2015-09-07",
        user_Id= user2.id
    )

    JustRight = Song(
        artist="GOT7",
        title="딱 좋아 (Just Right)",
        album="Just Right",
        written_by="Chizzy, Jay Dmuchowski, C-Minor, Gavin Jones, Steven Battey & Carlos Battey",
        label="KT Music & JYP Entertainment",
        song_bio='''“Just Right” is the title track of GOT7’s third EP of the same name. The track went viral for its inspirational lyrics that convey that one is “just right” as they are. The song also gave way to the _#JustRight_ Project that earned GOT7 the title of “Healing-dols,” inspiring fans and non-fans alike to learn to accept and love themselves.
        ''',
        lyrics=
        ''' [Intro]
Baby, you are just
Just right

[Verse 1]
거울아 거울아 제발 좀 말해주려무나
저울아 너도 말해주려무나
아무것도 바꿀 필요 없이 예쁘다고
지금 그 모습 그대로 완벽하다고
마냥 행복하면 돼 걱정 없이
부족한 점이 뭔지 찾기 없기
거울 대신 그냥 내 눈 빛을 바라봐
저울 대신 내 등 위에 올라타봐 봐

[Pre-Hook]
아무리 널 뜯어봐도
보고 또 보고 또 봐도
니가 말하는 안 예쁜 부분이 어딘지
그게 어딘지 찾을 수가 없어 난

[Hook]
지금처럼 만만만만만 만
있어주면 난난난난난
바랄게 없으니 넌 아무것도
바꾸지 마마마마마
아무 걱정마마마마마마
너의 모든게 다다다다
다 좋으니까 너는 아무것도
바꾸지 마마마마마

[Bridge]
이대로 (지금 이대로) 오 (그냥 이대로)
오 (지금 이대로) 오오오 있으면 돼

[Verse 2]
딱 좋아 너의 모든 게 그러니 네 맘
놓아 아무 걱정하지 마 이 말
백 퍼센트 다 그대로 믿어도 돼
모든 걱정 백 퍼센트 다 지워도 돼

[Pre-Hook]
아무리 널 뜯어봐도
보고 또 보고 또 봐도
니가 말하는 안 예쁜 부분이 어딘지
그게 어딘지 찾을 수가 없어 난

[Hook]
지금처럼 만만만만만 만
있어주면 난난난난난
바랄게 없으니 넌 아무것도
바꾸지 마마마마마
아무 걱정마마마마마마
너의 모든게 다다다다
다 좋으니까 너는 아무것도
바꾸지 마마마마마

[Bridge]
이대로 (지금 이대로) 오 (그냥 이대로)
오 (지금 이대로) 오오오 있으면 돼

[Verse 3]
옥에 티도 티가 나야 찾는 거지 원
눈부시게 빛나 빈틈이 없지 넌
내 눈에 얼마나 예쁜지 I want you
지금 이대로 you’re the only one
옥에 티도 티가 나야 찾는 거지 원
눈부시게 빛나 빈틈이 없지 넌
내 눈에 얼마나 예쁜지 I want you
지금 이대로 you’re the only one

[Hook]
지금처럼 만만만만만 만
있어주면 난난난난난
바랄게 없으니 넌 아무것도
바꾸지 마마마마마
아무 걱정마마마마마마
너의 모든게 다다다다다
다 좋으니까 너는 아무것도
바꾸지 마마마마마
''',
        song_url="https://soundcloud.com/user-91556499/sets/got7-just-right",
        media_url="https://www.youtube.com/watch?v=vrdk3IGcau8",
        song_icon="https://t2.genius.com/unsafe/220x220/https%3A%2F%2Fimages.genius.com%2F089bc1fd53b0cf16b236d7651da1c1f7.1000x1000x1.jpg",
        song_background_image="https://t2.genius.com/unsafe/1470x280/https%3A%2F%2Fimages.genius.com%2Fb9b289c38dcfdefe258eac0b0f983613.1000x670x1.png",
        release_date="2015-07-15",
        user_Id= user2.id
    )

    AgustD = Song(
        artist="Agust D",
        title="Agust D",
        album="Agust D",
        written_by="Agust D",
        label="BigHit Entertainment",
        song_bio='''“Agust D” is the title track for Agust D’s self titled mixtape. The track features intense rap over an old-school-hip-hop-influenced beat, and it samples James Brown’s 1966 hit “It’s a Man’s Man’s Man’s World”.
        ''',
        lyrics='''[Sample]

[Verse 1]
They call me new thang
신병 왔다 짐을 받어
Whole world, concert
꽤 먹히는 Asiana Asia
You could be my new thang
근무태만 형들 과는 달러
유명인의 하극상 damn
쎈 놈만 덤벼
어떤 이는 내가 이 자릴 쉽게 앉았다고 해
Fuck you 난 성공과
거리가 먼 형들 사이 눈엣가시네
솔직히 싸이하누월 쪽팔려
이제 일년에 50만장 팔어
K-pop 이란 카테고리
날 담기에는 사이즈가 달러 whoo
그래 앞서
가고 싶다면 first class 예약해봐
My seat is business
넌 이코노미 평생 내 뒤지 kissing my ass
다음 목표는 Billboard
Brazil to New York
꽤 쉴 틈 없는 내 passport

[Chorus]
A to the G to the U to the STD
I'm d boy because I'm from D
난 미친놈 비트 위의 lunatic
랩으로 홍콩을 보내는
My tongue technology
A to the G to the U to the STD
A to the G to the U to the STD
A to the G to the U to the STD
홍콩을 보내는
My tongue technology

[Verse 2]
난 베끼는 걸 베끼는 놈을 잡아다가
후배든 선배든 제끼는 놈
놈팽이든 내가 wack 이든 fack
이든 역사를 바닥에 새기는 놈
또 재미도 없는 랩퍼들 사이에서
늘 남들보다 더 챙기는 몫
잘나가는 덕에 밥그릇 뺏길
형들의 시기 질투 덕에 생기는 소음
Hey ho 난 좆도 상관 안 해
니가 개 삽질할 때
간단하게 니가 판 무덤에
널 생매장하네
Hey ho 너넨 나 감당 안 돼
약질하는 다수의 랩퍼들
내가 아이돌이란 것에 감사하길

[Verse 3]
Cause I'm busy I'm busy 24/7 쉬긴 뭘 쉬니
이미 시길 놓친 이 끼리 끼리 놀아주길
시기와 치기만 남은
자들의 곡성 뭣이 중헌지를 몰라
Paris to New York, damn
쉴 틈 없는 내 스케줄

[Chorus]
A to the G to the U to the STD
I'm d boy because I'm from D
난 미친놈 비트 위의 루나틱
랩으로 홍콩을 보내는
My tongue technology
A to the G to the U to the STD
A to the G to the U to the STD
A to the G to the U to the STD
홍콩을 보내는
My tongue technology

[Bridge]
I'm sorry 진심이야 미안해
니 밥그릇 뺏은 게 나라서 나 미안해 boy
I'm sorry 분노는 지양해
유일한 자산 건강 잃으면
니 엄마 속상하셔
I'm sorry 직업을 전향해
삽질하는 게 예삿
폼이 아냐 전향해 boy
I'm sorry 진심야 미안해
니 랩퍼가 나 보다 못하는 것에 대해

[Chorus]
A to the G to the U to the STD
I'm d boy because I'm from D
난 미친놈 비트위의 루나틱
랩으로 홍콩을 보내는
My tongue technology
A to the G to the U to the STD
A to the G to the U to the STD
A to the G to the U to the STD
홍콩을 보내는
My tongue technology

[Outro]
A to the G to the U to the STD
I'm d boy because I'm from D
난 미친놈 비트 위의 루나틱
랩으로 홍콩을 보내는
My tongue technology
A to the G to the U to the STD
A to the G to the U to the STD
A to the G to the U to the STD
홍콩을 보내는
My tongue technology
        ''',
        song_url="https://soundcloud.com/user-91556499/sets/got7-just-right",
        media_url="https://www.youtube.com/watch?v=vrdk3IGcau8",
        song_icon="https://t2.genius.com/unsafe/220x220/https%3A%2F%2Fimages.genius.com%2F9563cf7190f5e146573c087144b156e9.500x500x1.jpg",
        song_background_image="https://t2.genius.com/unsafe/1470x280/https%3A%2F%2Fimages.genius.com%2F9563cf7190f5e146573c087144b156e9.500x500x1.jpg",
        release_date="2016-08-15",
        user_Id= user2.id
    )
    
    BadBoy = Song(
        artist="Red Velvet",
        title="Bad Boy",
        album="The Perfect Red Velvet",
        written_by="Moon Hye Yun (문희연) & JQ ",
        label="SM Entertainment",
        song_bio='''Bad Boy is the lead single from Red Velvet’s 2nd album repackage, The Perfect Red Velvet. Both sonically and lyrically, the track represents the group’s “velvet” side.
        ''',
        lyrics='''[Verse 1: Irene, Seulgi]
Who dat who dat who dat boy
수많은 사람 속 눈에 띈
무심한 그 표정 I like that
내 호기심을 자극하지

[Refrain 1: Yeri, Joy]
Oh 시크한 스타일은 덤
입은 옷은 신경 쓴 듯 안 쓴 듯
관심 없는 말투 I like that
외면해 봐도 끌려

[Pre-Chorus: Wendy]
달라 도도한 날 웃게 하잖아
알잖아 요즘 내가 Hot ah ah
날 보는 시선 너도 느껴봐

[Chorus: Joy, All]
홀린 듯 날 따라와
모두 환호해 너도 곧 Ooh ooh (Oh-eh-oh-eh-oh)
아닌 척해도 넌 Ooh ooh (Oh-eh-oh-eh-oh)
한 번 내기를 해볼까

[Post-Chorus: Seulgi, All, Irene]
너무 쉽겐 오지 마
재미없잖아 거기서 Ooh ooh (Oh-eh-oh-eh-oh)
밀고 당겨볼까 Ooh ooh (Oh-eh-oh-eh-oh)
시작할게 Bad boy down

[Hook: All, Wendy]
Whoa whoa
지금부터 Bad boy down
Whoa whoa

[Verse 2: Yeri, Wendy]
잠깐 이리 와봐 너에게만 할 말이 있어
가까이 좀 와 고갤 숙여 키를 낮춰봐
다른 건 신경 쓰지 마
내 목소리에 집중해

[Refrain 2: Irene, Joy, Seulgi]
상황은 좀 달라져
주위를 맴도는 내가 궁금해
너도 알게 될 거야 (뭘까?) 알 거야 (말해)
이미 늦어버렸단 걸

[Pre-Chorus: Seulgi]
맞아 사실 꽤나 자신 있어 난
지는 게임 하진 않아 Ha ah ah
벌써 반쯤은 넘어왔잖아

[Chorus: Joy, All]
홀린 듯 날 따라와
모두 환호해 너도 곧 Ooh ooh (Oh-eh-oh-eh-oh)
아닌 척해도 넌 Ooh ooh (Oh-eh-oh-eh-oh)
한 번 내기를 해볼까

[Post-Chorus: Joy, All]
너무 쉽겐 오지 마
재미없잖아 거기서 Ooh ooh (Oh-eh-oh-eh-oh)
밀고 당겨볼까 Ooh ooh (Oh-eh-oh-eh-oh)
시작할게 Bad boy down

[Bridge: Wendy, Joy, Seulgi, Irene]
혼란스런 맘이겠지 상상조차 못할 거야
헤어나려 노력해도 어떤 작은 틈도 없어
정답은 정해져 있어 자연스럽게 넌 따라와
난 널 선택해 난 널 선택했어 이미

[Chorus: Joy, All]
홀린 듯 날 따라와
모두 환호해 말했지 Ooh ooh (Oh-eh-oh-eh-oh)
결관 항상 같아 Ooh ooh (Oh-eh-oh-eh-oh)
거봐 내가 또 이겼어

[Post-Chorus: Joy, All]
너무 쉽겐 오지 마
재미없잖아 이제 넌 Ooh ooh (Oh-eh-oh-eh-oh)
벗어날 수 없어 Ooh ooh (Oh-eh-oh-eh-oh)
내겐 쉽지 Bad boy down
        ''',
        song_url="https://soundcloud.com/l2share66/red-velvet-bad-boy-all-right-time-to-love-moonlight-melody",
        media_url="https://www.youtube.com/watch?v=J_CFBjAyPWE&feature=emb_title",
        song_icon="https://t2.genius.com/unsafe/220x220/https%3A%2F%2Fimages.genius.com%2Fff0468257a1ee27af89d195c3a6f3d9e.640x640x1.png",
        song_background_image="https://t2.genius.com/unsafe/980x280/https%3A%2F%2Fimages.genius.com%2Fff0468257a1ee27af89d195c3a6f3d9e.640x640x1.png",
        release_date="2018-01-29",
        user_Id= user2.id
    )

    Spoiler = Song(
        artist="Epik High",
        title="Spoiler",
        album="신발장 (Shoebox)",
        written_by="Tablo",
        label="YG Entertainment",
        song_bio='''“Don’t Hate Me”와 같은 시기에 만든 곡이지만 분위기가 맞지 않아 앨범에서 빠졌다고 한다. 이후 타블로의 솔로 2집에 수록할 계획이었으나 결국 에픽 하이의 음악으로 빛을 보게 되었다.
        ''',
        lyrics='''[Chorus: Tablo]
너의 차가운 눈빛과 말투가 spoiler
너의 모든 행동 속에 우리의 끝이 보여
아니라고 말해도 느껴지는 spoiler
끝까지 봐야 할까? 지금 떠나야 할까?
반전이 있을까봐

[Verse 1: Tablo & Mithra Jin]
무슨 생각해? 두 번 묻자 날 봐
또 대답 아닌 대답을 해, "내일 비가 오려나 봐"
다시 창 밖을 보는 너, 요즘 자주 보는 너의 옆모습
넌 한숨을 쉬고 넘쳐 솟는 정적에 잠기는 나
빠져들면 안 되는 망상, I know, 내 직감은 위험해
한 번 발 들이면 deep 해질 놈, 내 예민함은 심해
난 알지 왜 뜻 모를 한 숨이 잦아지는지
떠나가는 마음은 한숨 한숨씩 자릴 비우지

[Verse 2: Mithra Jin]
왠지 예전보다 바쁜 생활
연락이 드문 날들과 마지못해 하는 대화
그 썼다 지우는 말들, 다 복선이겠지
우연인지 몰라도 요즘은 시계를
볼 때마다 등진 분침과 시침
둘이 잠시 보여주는 미래, 전부 cliché
수백 번은 본 듯한 이 뻔한 장면들인데
왜 난 가슴을 졸이는지
우리 시작에 했던 많은 약속들 바빠서 잊은 건지
아님 벌써 잊기 바쁜 건지

[Chorus: Tablo]
너의 차가운 눈빛과 말투가 spoiler
너의 모든 행동 속에 우리의 끝이 보여
아니라고 말해도 느껴지는 spoiler
끝까지 봐야 할까? 지금 떠나야 할까?
반전이 있을까봐, I can't let you go

[Verse 3: Mithra Jin & Tablo]
난 크게 들려, 하지 않은 말도
애써 아닌 척 하지만 난 알고 있어
갈수록 내 숨통을 쥐는 이 망할 촉
어쩌면 내가 내 헛된 fantasy에 널 가둬둔 건지도
맞지 않는 배역에 너 역시 내게 맞춰준 건지도
버릇처럼 사랑한다고 말할 때도 늘 딴 생각
대사와는 다른 표정, 어긋난 자막

[Verse 4: Tablo]
영화 같은 사랑을 하고 싶던 내게 걸맞은 벌인 걸까?
끝내 너의 맘을 물어도 대답은 언제나 열린 결말
그래, 우리 늘 반전에 반전이었고 숨 막히는 장면의 연속
그 뜨거웠던 지옥보다 못한 이 식어버린 감정의 연옥
난 끝이 보여, 상상, 그 영사기를 끄지 못해, 입에 술이 고여
Film 끊길 때 그나마 숨이 놓여
Just cut me out or kill me out, happy ending은 됐어
Don’t let me fade out

[Chorus: Tablo]
너의 차가운 눈빛과 말투가 spoiler
너의 모든 행동 속에 우리의 끝이 보여
아니라고 말해도 느껴지는 spoiler
끝까지 봐야 할까? 지금 떠나야 할까?
반전이 있을까봐, I can't let you go

[Bridge: Tablo & Mithra Jin]
어쩌면 너와 난 첫 frame부터 결말이 예정된
미친 Charade
어쩌면 너와 난 첫 scene부터 마지막을 향해 행진
This is our last parade

[Chorus: Tablo]
너의 차가운 눈빛과 말투가 spoiler
너의 모든 행동 속에 우리의 끝이 보여
아니라고 말해도 느껴지는 spoiler
끝까지 봐야 할까? 지금 떠나야 할까?
반전이 있을까봐, I can't let you go

[Outro: Tablo]
끝이 보이지만 baby don’t let go
단 한 장면이라도 놓칠까봐 girl I can’t let go
I can't let you go
끝이 보이지만 baby don’t let go
단 한 장면이라도 놓칠까 봐 girl I can’t let go
The end?
        ''',
        song_url="https://soundcloud.com/chopplanet18/epik-high-spoiler",
        media_url="https://www.youtube.com/watch?v=M8GUlNNXBVg&feature=emb_title",
        song_icon="https://t2.genius.com/unsafe/220x220/https%3A%2F%2Fimages.genius.com%2F810c37065c3b8daaa11895069c0aa916.600x600x1.png",
        song_background_image="https://t2.genius.com/unsafe/800x191/https%3A%2F%2Fimages.genius.com%2F810c37065c3b8daaa11895069c0aa916.600x600x1.png",
        release_date="2014-10-21",
        user_Id= user2.id
    )

    BloodSweatAndTears = Song(
        artist="BTS",
        title="피 땀 눈물 (Blood Sweat & Tears) ",
        album="WINGS",
        written_by=" ”hitman” Bang, SUGA (BTS), Kim Do Hoon (김도훈), j-hope, RM & Pdogg",
        label="BigHit Entertainment",
        song_bio='''“Blood Sweat & Tears” is the title track of South Korean boy band BTS' second studio album, WINGS. The music video for this track was released on October 10, 12 PM KST, 4 days after the music video teaser was released by BigHit Entertainment. The mv was viewed 3 million times on YouTube over the course of 12 hours, and 6.3 million times over 24 hours. Blood Sweat & Tears also broke records by being the fastest K-Pop boy band music video to be viewed 20 million times.
        ''',
        lyrics='''방탄소년단의 피 땀 눈물 가사

[Hook: Jimin, Jungkook]
내 피 땀 눈물 내 마지막 춤을 다 가져가, 가
내 피 땀 눈물 내 차가운 숨을 다 가져가, 가
내 피 땀 눈물

[Verse 1: Suga, RM, J-Hope]
내 피 땀 눈물도
내 몸 마음 영혼도
너의 것인 걸 잘 알고 있어
이건 나를 벌받게 할 주문
Peaches and cream, sweeter than sweet
Chocolate cheeks and chocolate wings
But 너의 날개는 악마의 것
너의 그 sweet 앞엔 bitter bitter
Kiss me 아파도 돼 어서 날 조여줘
더 이상 아플 수도 없게
Baby 취해도 돼 이제 널 들이켜
목 깊숙이 너란 위스키

[Chorus: V, Jungkook, J-Hope]
내 피 땀 눈물 내 마지막 춤을
다 가져가, 가
내 피 땀 눈물 내 차가운 숨을
다 가져가, 가
원해 많이 많이 많이 많이
원해 많이 많이 많이 많이
원해 많이 많이, 많이 많이
원해 많이 많이, 많이 많이
원해 많이 많이, 많이 많이
원해 많이 많이, 많이 많이

[Verse 2: J-Hope, Suga]
아파도 돼 날 묶어줘 내가 도망칠 수 없게 (쉿)
꽉 쥐고 날 흔들어줘 내가 정신 못 차리게
Kiss me on the lips, lips
둘만의 비밀 너란 감옥에 중독돼 깊이
니가 아닌 다른 사람 섬기지 못해
알면서도 삼켜버린 독이 든 성배

[Chorus: V, Jimin, J-Hope]
내 피 땀 눈물 내 마지막 춤을
다 가져가, 가
내 피 땀 눈물 내 차가운 숨을
다 가져가, 가
원해 많이 많이, 많이 많이
원해 많이 많이, 많이 많이
원해 많이 많이 많이 많이
원해 많이 많이 많이 많이

[Bridge: V, Jungkook, Jin]
나를 부드럽게 죽여줘
너의 손길로 눈 감겨줘
어차피 거부할 수조차 없어
더는 도망갈 수조차 없어
니가 너무 달콤해 너무 달콤해 너무 달콤해서

[Interlude: Narration]
He too was a tempter; he, too, was a link to the second, the evil world with which I no longer wanted to have anything to do

[Hook: Jimin]
내 피 땀 눈물
내 피 땀 눈물
        ''',
        song_url="https://soundcloud.com/captain_law-kun/bts-blood-sweat-and-tears-mv1-hour-loop-1",
        media_url="https://youtu.be/hmE9f-TEutc",
        song_icon="https://t2.genius.com/unsafe/220x220/https%3A%2F%2Fimages.genius.com%2F0a8d560bb0f258ab739e710bbd7ac3e4.500x500x1.jpg",
        song_background_image="https://t2.genius.com/unsafe/1500x280/https%3A%2F%2Fimages.genius.com%2Fd504c44c6c99f130795dc22fdbda78d5.500x200x1.png",
        release_date="2016-10-10",
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
    db.session.add(JustRight)
    db.session.add(Hero)
    db.session.add(AgustD)
    db.session.add(BadBoy)
    db.session.add(Spoiler)
    db.session.add(BloodSweatAndTears)

    db.session.commit()


def undo_songs():
    db.session.execute('TRUNCATE songs CASCADE;')
    db.session.commit()
