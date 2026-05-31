from email_reader import Email

dict = {
    "spam": [
        ("данные карты", 1000), ("dannye karty", 1000),
        ("данные банковской карты", 1000), ("bankovskoy karty", 1000),
        ("перейдите по ссылке", 100), ("pereydite po ssylke", 100),
        ("подозрительн", 100), ("podozriteln", 100),
        ("только сегодня", 1000), ("tolko segodnya", 1000),
        ("exclusive offer", 1000),
        ("поздравляем", 1000), ("pozdravlyaem", 1000),
        ("congratulations", 1000),
        ("розыгр", 1000), ("rozygr", 1000),
        ("эксклюзив", 1000), ("eksklyuziv", 1000),
        ("выигр", 1000), ("vyigr", 1000),
        ("побед", 1000), ("pobed", 1000),
        ("приз", 1000), ("priz", 1000),
        ("скидка", 1000), ("skidka", 1000),
    ],

    "draft": [
        ("не отправлять", 500), ("ne otpravlyat", 500),
        ("черновик", 500), ("chernovik", 500),
        ("draft", 500),
        ("todo", 500),
        ("to do", 500),
    ],

    "critical": [
        ("инцидент", 10), ("intsident", 10),
        ("outage", 20),
        ("critical", 50),
        ("urgent", 50),
        ("immediately", 50),
        ("немедл", 50),
        ("критичн", 50), ("kritichn", 50),
        ("критическ", 50), ("kritichesk", 50),
        ("warning", 10),
        ("срочн", 50), ("srochn", 50),
        ("упал", 20), ("upal", 20),
    ],

    "software_issues": [
        ("сбой авторизации", 10), ("sboy avtorizatsii", 10),
        ("доступ запрещен", 10), ("dostup zapreshchen", 10),
        ("нет доступа", 10), ("net dostupa", 10),
        ("восстановить доступ", 10), ("vosstanovit dostup", 10),
        ("не могу войти", 10), ("ne mogu voyti", 10),
        ("пропал доступ", 10), ("propal dostup", 10),
        ("перестал запуск", 10), ("perestal zapusk", 10),
        ("после обновл", 10), ("posle obnovl", 10),
        ("код ошибки", 10), ("kod oshibki", 10),
        ("unauthorized", 10),
        ("не запуск", 7), ("ne zapusk", 7),
        ("не откры", 7), ("ne otkry", 7),
        ("не отвеч", 7), ("ne otvech", 7),
        ("не работает", 7), ("ne rabotaet", 7),
        ("заблокирован", 10), ("zablokirovan", 10),
        ("запрос доступа", 10), ("zapros dostupa", 10),
        ("выдать доступ", 10), ("vydat dostup", 10),
        ("нужны права", 10), ("nuzhny prava", 10),
        ("переустан", 6), ("pereуstan", 6),
        ("остановл", 6), ("ostanovl", 6),
        ("затронут", 6), ("zatronut", 6),
        ("недоступен", 10), ("nedostupen", 10),
        ("вылетает", 10), ("vyletaet", 10),
        ("зависает", 10), ("zavisaet", 10),
        ("error", 10),
        ("ошибк", 10), ("oshibk", 10),
        ("сбой", 10), ("sboy", 10),
        ("bug", 10),
        ("баг", 10), ("bag", 10),
    ],
    "hardware_issues": [
        ("после падения", 10), ("posle padeniya", 10),
        ("посторонние звуки", 10), ("postoronnie zvuki", 10),
        ("не определяется", 8), ("ne opredelyaetsya", 8),
        ("жесткий диск", 10), ("zhestkiy disk", 10),
        ("неисправ", 7), ("neisprav", 7),
        ("диагностик", 7), ("diagnostik", 7),
        ("не вкл", 7), ("ne vkl", 7),
        ("гарнитура", 10), ("garnitura", 10),
        ("процессор", 6), ("protsessor", 10),
        ("ноутбук", 10), ("noutbuk", 10),
        ("принтер", 10), ("printer", 10),
        ("клавиатур", 10), ("klaviatur", 10),
        ("компьютер", 10), ("kompyuter", 10),
        ("сканер", 10), ("skaner", 10),
        ("мыш", 10), ("mysh", 10),
        ("экран", 10), ("ekran", 10),
        ("ссд", 10), ("ssd", 10),
        ("симптом", 5), ("simptom", 5),
        ("оборудов", 10), ("oborudov", 10),
        ("устройств", 10), ("ustroystv", 10),
        ("ремонт", 10), ("remont", 10),
        ("замен", 10), ("zamen", 10),
        ("слом", 10), ("slom", 10),
    ],
    "financial_requests": [
        ("оказанные услуги", 10), ("okazannye uslugi", 10),
        ("уточнение по оплате", 10), ("utochneniye po oplate", 10),
        ("задолжен", 10), ("zadolzhen", 10),
        ("реквизит", 10), ("rekvizit", 10),
        ("invoice", 10),
        ("billing", 10),
        ("платёж", 10), ("platyozh", 10),
        ("платеж", 10), ("platezh", 10),
        ("бухгалтер", 7), ("bukhgalter", 7),
        ("договор", 7), ("dogovor", 7),
        ("payment", 10),
        ("счёт", 10), ("schyot", 10),
        ("счет", 10), ("schet", 10),
        ("финанс", 6), ("finans", 6),
        ("budget", 5),
        ("акт", 5), ("akt", 5),
        ("плат", 10), ("plat", 10),
    ],
    "meeting_requests": [
        ("интервью", 10), ("intervyu", 10),
        ("interview", 10),
        ("демо", 10), ("demo", 10),
        ("встреч", 10), ("vstrech", 10),
        ("встрет", 10), ("vstret", 10),
        ("пригла", 10), ("prigla", 10),
        ("расписани", 5), ("raspisani", 5),
        ("schedule", 5),
        ("calendar", 5),
        ("invite", 10),
        ("перенос", 10), ("perenos", 10),
        ("zoom", 10),
        ("teams", 10),
        ("meet", 10),
        ("обсу", 6), ("obsu", 6),
        ("звон", 10), ("zvon", 10),
    ],
    "informational": [
        ("нетрудоспособ", 10), ("netrudosposob", 10),
        ("сотрудник", 10), ("sotrudnik", 10),
        ("технические работы", 10), ("tekhnicheskiye raboty", 10),
        ("плановые работы", 10), ("planovyye raboty", 10),
        ("рабочее место", 10), ("rabocheye mesto", 10),
        ("announcement", 10),
        ("объявлен", 10), ("obyavlen", 10),
        ("дайджест", 10), ("daydzhest", 10),
        ("мониторинг", 10), ("monitoring", 10),
        ("направляем", 10), ("napravlyaem", 10),
        ("высылаем", 10), ("vysylaem", 10),
        ("информ", 10), ("inform", 10),
        ("метрик", 10), ("metrik", 10),
        ("отчёт", 10), ("otchyot", 10),
        ("отчет", 10), ("otchet", 10),
        ("политик", 10), ("politik", 10),
        ("больн", 10), ("boln", 10),
        ("болен", 10), ("bolen", 10),
        ("отпуск", 10), ("otpusk", 10),
        ("оформ", 10), ("oform", 10),
        ("график", 10), ("grafik", 10),
        ("итог", 10), ("itog", 10),
    ],

        "unclassified": []
}


class Classifier:
    @staticmethod
    def classify(email: Email) -> str:
        if email.isu:
            return "unclassified"
        text = email.text.lower()
        rating = {}
        for i, mp in dict.items():
            if i == "unclassified":
                continue
            balls = sum(w for kw, w in mp if kw.lower() in text)
            if balls > 0:
                rating[i] = balls
        if not rating:
            return "unclassified"
        mx = -1
        best = ""
        for x in rating.keys():
            if mx < rating[x]:
                mx = rating[x]
                best = x
        return best