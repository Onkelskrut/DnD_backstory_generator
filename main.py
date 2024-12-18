import telebot
from random import *
from telebot import types
from bot_token import TOKEN


# отдельное спасибо Константину Волегову, за помощь =)

bot = telebot.TeleBot(TOKEN)


race_list = ["аасимар", "багбир", "гит", "гифф", "гном", "гоблин", "голиаф", "дварф", "драконорожденный",
             "кенку", "людоящер", "минотавр", "орк", "полуорк", "полурослик", "полуэльф",
             "табакси", "тифлинг", "тритон", "фирболг", "хобгоблин", "человек", "эльф", "юань-ти"]

profession_list = ["ресировщик животных", "дресировщик монстров", "арборист", "уборщик урожая", "пасечник ("
                   "пчеловод)", "заводчик", "пастух", "доярка", "сокольничий", "фермер", "рыбак", "флорист", "фуражир",
                   "лесник", "ловчий", "егерь", "конюх", "псарь", "объезчик", "охотник", "лесоруб",
                   " мастер над лошадями", "мастер над гончими", "мельник", "шахтер", "следопыт", "плюмер",
                   "геолог", "рейнджер", "колотильщик", "винодел", "смотритель зоопарка", "архитектор", "кирпичник",
                   "каменщик", "плотник", "разнорабочий", "бригадир", "стекольщик", "штукатур", "дорогоукладчик",
                   "акробат", "актер", "аранжировщик", "атлет", "уличный музыкант", "музыкант", "знаменитость", "повар",
                   "дерижер/хориограф", "колун", "комедиант", "смотритель", "костюмер", "танцор", "эквилибрист",
                   "канатоходец", "дизайнер моды", "гладиатор", "шут", "жанглер" "иллюзионист", "просветитель",
                   "портретист", "менестрель/бард", "модель", "музыкан", "художник", "писатель", "композитор", "поэт",
                   "скульптор",  "певец", "скальд", "каскадер", "тату мастер", "художественный руководитель",
                   "бухгалтер", "коллекционер животных/монстров", "коллекционер", "владелец бизнеса", "коллектор",
                   "торговец алкоголем", "оценщик", "аукционист", "банкир", "управляющий баней",
                   "снабженец", "бакалейщик", "глава гильдии", "трактирщик", "землемер",  "торговец", "обменник",
                   "ростовщик" "скупщик", "коробейник", "владелец плантациями", "смотритель имения", "спекулянт",
                   "комиссионный торговец", "лавочник", "расклейщик рекламы", "курьер", "герольд", "гонец",
                   "переводчик", "городской глашатай",  "чеканщик", "бронник", "кузнец", "оружейник", "переплетчик",
                   "боттлер", "лукодел", "пивовар", "метельщик" "свечник", "картограф", "каретник", "бондарь",
                   "ножовщик", "красильщик", "вышивальщица", "гравер", "коновал", "мебельщик", "скорняк", "стеклодув",
                   "перчаточник",  "ювелир", "кожевник", "слесарь", "струнник", "ткач", "портной", "оптик", "гончар",
                   "горшечник", "реставратор", "канатник", "ковродел", "седлер", "мыловар", "дубильщик", "таксидермист",
                   "тинкер", "кукольник", "часовщик", "резчик по дереву",  "убийца", "бандит", "взломщик",
                   "шарлатан/мошенник", "игрок на боях", "криминальный авторитет", "карманник", "наркоторговец",
                   "нарко барон", "вымогатель", "скупщик краденного", "фальшивомонетчик", "беглец", "разбойник",
                   "похититель", "пират", "налетчик/рейдер", "браконьер", "отравитель", "контрабандист", "вор",
                   "олдермен/член муниципалитета", "канцлер", "шеф", "защитник природы" "барон", "граф/ярл/эрл",
                   "герцог", "придворный/придворная дама", "дипломат", "король", "император", "судья", "стражник",
                   "рыцарь", "юрист", "мастер-над-монетой", "мастер-над-пирами", "министр/советник",
                   "дворянин/аристократ", "нотариус", "оратор/спикер", "паж", "принц/принцесса",  "сенатор",
                    "шериф", "мастер-над-шпионами", "управляющий", "сквайр/оруженосец", "сборщик налогов", "подопечный лорда"]

character_traits = ["добрый", "честный", "смелый", "трудолюбивый", "уверенный", "дружелюбный", "открытый",
                    "отзывчивый", "пунктуальный", "инициативный", "Заботливый", "Целеустремлённый", "Решительный",
                    "Настойчивый", "Ответственный", "Надёжный", "Терпеливый", "Спокойный", "Оптимистичный",
                    "Жизнерадостный", "Общительный", "Вежливый", "Тактичный", "Внимательный", "Сочувствующий",
                    "Понимающий", "Эмпатичный", "Организованный", "Дисциплинированный", "Аккуратный", "Креативный",
                    "Изобретательный", "Любознательный", "Гибкий", "Адаптивный", "Лидерский", "Независимый",
                    "Самостоятельный", "Амбициозный", "Предприимчивый", "Энергичный", "Выносливый",
                    "Стрессоустойчивый", "Смещливый", "Тревожный", "Загадочный", "Пугливый", "Миролюбивый"]

phobias = ["боится воды", "боязнь открытого пространства", "страх замкнутого пространства",
           "боязнь высоты", "cтрах темноты", "боязнь полётов",
           "страх смерти", "страх толпы", "боязнь одиночества",
           "боязнь старости", "боязнь грязи", "арахнофобия",
           "стесняется девушек", "боязнь потерять свои вещи", "боязнь крыс"]

features = ["являющийся последним представителем древнего рода", "вычеркнутый из их семейного завещания",
            "обладающий довольно избирательной памятью", "играющий почти на всех музыкальных инструментах",
            "говорящий предложениями из десяти слов", "продавший душу тьме", "носящий на шее загадочное кольцо",
            "путающий право и лево", "владеющий змеиным языком", "потерявший память и решивший начать жизнь с чистого листа",
            "понимающий животных", "разбирающийся в магических предметах", "любящий все , что блестит", "проживший долгое время в диких лесах",
            "ненавидящий зло во всех его проявлениях", "присягнувший ордену паладинов", "узнавший, что смертельно болен",
            "укрывшийся на суше от морских демонов", "постоянно забывающий куда он шел"]

appearance_features = ["носящий татуировку с инициалами", "носящий татуировку с любимым оружием", "носящий татуировку с черепом", "носящий атуировку со змеей",
                       "носящий татуировку со скорпионом", "носящий татуировку с пауком", "носящий татуировку с цветком", "носящий татуировку с драконом",
                       "носящий татуировку с таинственным символом", "носящий татуировку с сердцем", "носящий татуировку с растительным орнаметном",
                       "носящий серьгу в ухе", "носящий тонкую цепочку на шее", "носящий крупную цепочку на шее", "носящий толстую цепь на шее", "носящий плотный ошейник на шее",
                       "носящий приметную брошь", "носящий кольцо на пальце", "носящий перстень на пальце", "носящий несколько колец", "носящий простой браслет", "носящий дорогой браслет",
                       "носящий необычный браслет", "носящий кольцо в носу", "носящий медальон на шее", "носящий богато укрешенный пояс", "в маске скрывающей лицо",
                       "в маске скрывающей часть лица", "носящий маленькие очки", "в больших очках", "носящий очки с толстыми стеклами", "носящий фальшивые очки",
                       "носящий дорогие украшения", "носящий тонкую повязку", "носящий кожанную повязку", "одетый в глубокий капюшон", "носящий маленькую шляпу", "в шляпе",
                       "в широкой шляпе", "в ярком головном уборе", "носящий необычную диадему", "с необычным цветом волос", "с мощными руками", "с нежными руками",
                       "с грубыми руками", "с мягкими руками", "потерявший руку на войне", "потерявший ногу во время службы моряком", "потерявший кисть, работая на кухне", "без пальца на руке",
                       "в шрамах по всему телу", "с глубоким шрамом на теле", "со странными знаками на теле", "сильно сутулящийся", "с прямой осанкой", "с тонкой кожей",
                       "с волосатым телом", "с костлявым телом", "с длинными конечностями", "с короткими конечностями", "с длинными пальцами", "с короткими пальцами"]

pre_histories = ["Твое дество прошло на берегу моря", "Ты родился на туманных островах", "Твое детство прошло в небольшой деревушке", "Ты абсолютно не помнишь своего дества",
                 "Воспитанник таинственного ордена ассасинов", "Ты был найден и воспитан труппой бродячего цирка", "Ты родился в семье лавочника, но потерял все в страшном пожаре",
                 "Ты был рожден в семье богатого аристократа", "Ты жил в красивом южном городе", "Твое детство прошло в уютном доме вблизи лесов", "Тебя воспитали монахи",
                 "Ты родился в семье рыбака", "Тебя с детства учили в магической академии", "Ты родился в семье крестьян", "Ты родился и рос в семье кузнецов",
                 "Ты родился в семье пекаря", "Ты провел свое детсво в духовной семинарии", "Тебя воспитал оккультный орден", "Ты выходец из рода варваров",
                 "Ты провел свое дество в пустыне", "Ты родился в эльфийских лесах", "Ты рос в деревне, расположенной в горах", "Ты рос в небогатой семье и часто помогал отцу на мельнице",
                 "Ты рос в небольшом городке, расположенном среди болот", "Ты вырос в замке туманного городка, и о вашей семье ходили слухи, что вы вампиры",
                 "Ты являешься выходцем из гильдии механиков", "Ты рос в большом промышленном городе", "Твои юные годы прошли в боях против диких зверей на арене",
                 "Ты родился в племени людей поклонявшимся смерти", "Ты родился в клане, который поклонялся деревьям", "Ты рос в семье лучников"]

motivation = ["а теперь ты все бросил ради приключений", "а теперь ты отправился искать себя в боях", "но ты выбрал идти своим путем, и тебя влекут магические искусства", "а теперь ты бросил вызов судьбе и решил стать волшебником, каких еще не видел свет",
              "но пришло время двигаться дальше и обрести бессмертие", "но ты решил , что такая жизнь тебе не подходит и тебе нужна хорошая компания для приключений",
              "и теперь одержимый идеей захватить мир ты двигаешься к своей цели", "и теперь ты отправился в поход за боевыми трофеями",
              "но узнав, что где-то в мире есть затерянная деревня, где владеют секретами ковки необычно прочного металла ты отправился на ее поиски",
              "и поняв, что ты устал от всего, ты решил пребиться к отряду странников", "когда твой отец тяжело заболел ты отправился в странствие, чтобы найти лекарство",
              "и вот сейчас ты собрал свои вещи и отправился искать славы своему роду в боях, что вернуться с трофеями и умножить славу отцов",
              "но в 20 лет на твоей руке проступил рисунок в виде узорной вязи, не найдя ответов ты отправился в путь, чтобы разгадать эту тайну",
              "но однажды врачи обнаружили у тебя смертельную болезнь, и решив прожить остаток жизни ярко ты отправился в путешествие",
              "а теперь ты нашел в себе искру магии и отправился искать учителя, способного развить твои навыки", "однажды ты потерял руку в несчастном случае, но очнувшись ты обнаружил, что ее заменили на полноценную механическую детальБ и теперь ты дал слово себе найти того, кто помог тебе",
              "а теперь отвергнутый красивой девушкой ты отправился куда глаза глядят, став женоненавистником =)", "но однажды ты потерял зрение в пожаре и решив развивать остальные свои чувства ты навсегда укрыл лицо под маской",
              "но ты всегла мечтал стать бардом и теперь отправился в путь", "а затем укрывшись от людских глаз в лесной глуши ты изучал язык животных"]


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Кто я?")
    markup.add(btn)

    mess = f'Приветствую тебя о, <b>{message.from_user.first_name}</b> <b>{message.from_user.last_name}</b>, давай узнаем кем же ты будешь сегодня!'
    bot.send_message(message.chat.id, {mess}, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def hundle(message):
    # if message.text == 'Кто я?':
    #     answer = f'Сегодня ты {choice(character_traits).lower()} {choice(race_list)} - {choice(profession_list)}, {choice(appearance_features)}, {choice(features)}, {choice(phobias)}. {choice(pre_histories)}, {choice(motivation)}.'
    #     bot.send_message(message.chat.id, {answer})
    if message.text == 'Кто я?':
        answer = f'Сегодня ты {choice(character_traits).lower()} {choice(race_list)} - {choice(profession_list)}, {choice(appearance_features)}, {choice(features)}. {choice(pre_histories)}, {choice(motivation)}. Среди твоих страхов {choice(phobias)}, но будь отважен и ты сможешь все преодолеть! Вперед! К приключениям!!!'
        bot.send_message(message.chat.id, {answer})

bot.polling(none_stop=True, interval=0)




