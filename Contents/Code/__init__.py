import re

TITLE  = 'Viasat Play'
PREFIX = '/video/viasatplay'

ART   = "art-default.jpg"
THUMB = 'icon-default.png'

MAX_SEARCH_ITEMS = 50

CHANNEL_NAMES = []

CHANNELS = {
    1209:
    {
        'base_url': 'http://www.tv3play.se',
        'thumb':    R('viasat_tv3.png'),
        'desc':     unicode('TV3 är kanalen med starka känslor och starka karaktärer. Det är en suverän mix av serier, livsstilsprogram, storfilmer, reportage och intressanta program.')
    },
    
    959:
    {
        'base_url': 'http://www.tv6play.se',
        'thumb':    R('viasat_tv6.png'),
        'desc':     unicode('TV6 En underhållningskanal för den breda publiken. Actionfilmer och den vassaste humorn.')
    },
    
    801:
    {
        'base_url': 'http://www.tv8play.se',
        'thumb':    R('viasat_tv8.png'),
        'desc':     unicode('TV8 är en svensk livsstils- och underhållningskanal med ett brett utbud. Du som gillar bilar, hus och vill veta allt om slottsliv, kommer inte vilja missa våra svenska produktioner i höst.')
    },
    
    5462:
    {
        'base_url': 'http://www.tv10play.se',
        'thumb':    R('viasat_tv10.png'),
        'desc':     unicode('På TV10 Play ser du alla TV10:s egna program och vissa av våra livesändningar och utländska serier. Vi har dessutom extramaterial till många av våra program. Mer information om våra program finns på TV10.se.')
    },
    
    1550:
    {
        'base_url': 'http://www.tv3play.no',
        'thumb':    R('tv3_norway.png'),
        'desc':     unicode('TV3 er en underholdningskanal for alle. Våre verdier er leken, nyskapende, oppløftende og engasjerende. Kanalens programtilbud består av innkjøpte serier, filmer og norske egenproduserte programmer i ulike kategorier.')
    },
    
    935:
    {
        'base_url': 'http://www.viasat4play.no',
        'thumb':    R('viasat4_norway.png'),
        'desc':     unicode('Viasat 4 er en norsk underholdnings- og sportskanal fra Modern Times Group (MTG). Kanalen startet sendinger 8. september 2007 i forbindelse med utbyggingen av det digitale bakkenettet.')
    },
    
    1337:
    {
        'base_url': 'http://www.tv6play.no',
        'thumb':    R('tv6_norway.png'),
        'desc':     unicode('TV6 er en underholdnings- og livsstilskanal hovedsakelig rettet mot moderne, voksne kvinner, med et bredt tilbud av programmer som skal inspirere og bevege seerne. Ved siden av TV3 og Viasat 4 har TV6 fått sin plass i MTG-familien, som et litt voksnere tv-alternativ for moderne, voksne kvinner. Typiske programsjangre vil være mat, hjem og bolig, talkshow, kvalitetsdramaserier og filmer, samt andre livsstilstemaer som er i vinden.')
    },
    
    3687:
    {
        'base_url': 'http://www.tv3play.dk',
        'thumb':    R('tv3_denmark.png'),
        'desc':     unicode('På TV3 Play kan du se alle TV3’s egne programmer og nogen af vores udenlandske serier. Vi har også ekstramateriale til flere af vores programmer. Mer information om vores programmer findes på TV3.dk')
    },
    
    1375:
    {
        'title':    'TV3 Play Eesti',
        'base_url': 'http://www.tv3play.ee',
        'thumb':    R('tv3_denmark.png'),
        'desc':     ''
    },
    
    1482:
    {
        'base_url': 'http://www.tv3play.lv',
        'thumb':    R('tv3_latvia.png'),
        'desc':     ''
    },
    
    3000:
    {
        'base_url': 'http://www.tv3play.lt',
        'thumb':    R('tv3_norway.png'),
        'desc':     ''
    },
    
    1933:
    {
        'base_url': 'http://www.play.novatv.bg',
        'thumb':    R('novatv.png'),
        'desc':     ''
    },
    
    4000:
    {
        'base_url': 'http://www.viagame.com',
        'thumb':    R('viagame.png'),
        'desc':     'Viagame is an eSports enthusiast website providing the best streamed gaming content to a global audience. We deliver premium live and on demand eSports content from the biggest leagues including The International and Dreamleague. We also deliver casual content such as review shows and interviews.'
    },
    
    6000:
    {
        'base_url': 'http://www.tv3play.se',
        'thumb':    'http://resources-cdn.plexapp.com/image/source/com.plexapp.plugins.mtv.jpg',
        'desc':     ''
    },
    
    6001:
    {
        'base_url': 'http://www.tv3play.se',
        'thumb':    'http://resources-cdn.plexapp.com/image/source/com.plexapp.plugins.comedycentral.jpg',
        'desc':     ''
    },
    
    6003:
    {
        'base_url': 'http://www.tv3play.se',
        'thumb':    R('zeeland.png'),
        'desc':     ''
    },
    
    6004:
    {
        'base_url': 'http://www.tv3play.se',
        'thumb':    R(THUMB),
        'desc':     ''
    },

    6005:
    {
        'base_url': 'http://www.juicyplay.se',
        'thumb':    R('juicy.png'),
        'desc':     unicode('JuicyPlay är en portal för allt du älskar inom nöje och kändisar. Här finns det senaste om stjärnorna från våra hetaste TV3-program, men också rykande färska nyheter om kändisar från såväl Hollywood som Stureplan.')
    },
    
    6100:
    {
        'base_url': 'http://www.tv3play.no',
        'thumb':    'http://resources-cdn.plexapp.com/image/source/com.plexapp.plugins.mtv.jpg',
        'desc':     ''
    },
    
    6101:
    {
        'base_url': 'http://www.tv3play.no',
        'thumb':    'http://resources-cdn.plexapp.com/image/source/com.plexapp.plugins.comedycentral.jpg',
        'desc':     ''
    },
    
    6102:
    {
        'base_url': 'http://www.tv3play.no',
        'thumb':    R(THUMB),
        'desc':     ''
    },
    
    6200:
    {
        'base_url': 'http://www.tv3play.dk',
        'thumb':    'http://resources-cdn.plexapp.com/image/source/com.plexapp.plugins.mtv.jpg',
        'desc':     ''
    },
    
    6201:
    {
        'base_url': 'http://www.tv3play.dk',
        'thumb':    'http://resources-cdn.plexapp.com/image/source/com.plexapp.plugins.comedycentral.jpg',
        'desc':     ''
    },
    
    6202:
    {
        'base_url': 'http://www.tv3play.dk',
        'thumb':    R(THUMB),
        'desc':     ''
    },
    
    6300:
    {
        'base_url': 'http://www.tv3play.ee',
        'thumb':    R(THUMB),
        'desc':     ''
    },
    
    6301:
    {
        'base_url': 'http://www.tv3play.ee',
        'thumb':    R(THUMB),
        'desc':     ''
    },

    6302:
    {
        'base_url': 'http://www.tv3play.ee',
        'thumb':    R(THUMB),
        'desc':     ''
    },

    6400:
    {
        'base_url': 'http://www.tvplay.lv',
        'thumb':    R(THUMB),
        'desc':     ''
    },

    6401:
    {
        'base_url': 'http://www.tvplay.lv',
        'thumb':    R(THUMB),
        'desc':     ''
    },

    6402:
    {
        'base_url': 'http://www.tvplay.lv',
        'thumb':    R(THUMB),
        'desc':     ''
    },

    6403:
    {
        'base_url': 'http://www.tvplay.lv',
        'thumb':    R(THUMB),
        'desc':     ''
    },

}

COUNTRIES = {
    'Sweden':       ['se', 'vg'],
    'Norway':       ['no'],
    'Denmark':      ['dk'],
    'Estonia':      ['ee'],
    'Lithuania':    ['lt'],
    'Latvia':       ['lv'],
    'Bulgaria':     ['bg']
}

API_BASE_URL = String.Decode('aHR0cDovL3BsYXlhcGkubXRneC50di92My8=')

###################################################################################################
def Start():
    DirectoryObject.thumb = R(THUMB)
    ObjectContainer.art   = R(ART)

    HTTP.CacheTime = CACHE_1HOUR  

###################################################################################################
@handler(PREFIX, TITLE, thumb = THUMB, art = ART)
def MainMenu():
    # global CHANNEL_NAMES
    oc = ObjectContainer(title1 = TITLE, no_cache = True)
    
    if Prefs['country'] != 'None':
        country = ",".join(COUNTRIES[Prefs['country']])

        oc.add(
            DirectoryObject(
                key   = Callback(Latest, channel=None, country=country), 
                title = 'Latest'
                )
            )

        oc.add(
            DirectoryObject(
                key   = Callback(Popular, channel=None, country=country),
                title = 'Popular'
            )
        )

        oc.add(
            DirectoryObject(
                key   = Callback(Collections, country=country), 
                title = 'Collections'
                )
            )

        oc.add(
            DirectoryObject(
                key   = Callback(Categories, channel=None, country=country), 
                title = 'Categories'
                )
            )

        oc.add(
            DirectoryObject(
                key   = Callback(Channels, country=country), 
                title = 'Channels'
                )
            )

        oc.add(
            DirectoryObject(
                key   = Callback(AllPrograms, channel=None, country=country), 
                title = 'All Programs'
                )
            )

        oc.add(
            InputDirectoryObject(
                key    = Callback(Search, channel=None, country=country),
                title  = 'Search Program',
                prompt = 'Search Program',
                thumb  = R(THUMB)
            )
        )
    else:
        oc.add(
            DirectoryObject(
                key     = Callback(NoCountrySelected),
                title   = 'Please select country',
                summary = 'Select country in preferences to get started'
            )
        )
        
    oc.add(PrefsObject(title = "Preferences..."))
    
    return oc

####################################################################################################
@route(PREFIX + '/Channels')
def Channels(country):

    oc = ObjectContainer(title1 = TITLE, title2='Channels', no_cache = True)

    data = JSON.ObjectFromURL(API_BASE_URL + 'channels/')
        
    for channel in data['_embedded']['channels']:
        if channel['country'] in COUNTRIES[Prefs['country']] and channel['id'] in CHANNELS:
            oc.add(
                DirectoryObject(
                    key = 
                    Callback(
                        ChannelMenu, 
                        title = channel['name'], 
                        country = country,
                        id = channel['id'],
                        base_url = CHANNELS[channel['id']]['base_url'],
                        thumb = CHANNELS[channel['id']]['thumb']
                        ), 
                    title = channel['name'],
                    summary = CHANNELS[channel['id']]['desc'],
                    thumb = CHANNELS[channel['id']]['thumb']
                    )
                )
    oc.objects.sort(key = lambda obj: obj.title)
    return oc

####################################################################################################
@route(PREFIX + '/Latest', episodes = bool)
def Latest(channel, country, episodes = True):

    title2='Latest'
    section = "videos.latest"
    if not episodes:
        title2 = title2 + " - Clips"
        section = "videos.latest_clips"

    if channel:
        videos_url = API_BASE_URL + 'sections?sections=%s&premium=open&device=mobile&channel=%s' % (section, channel)
    else:
        videos_url = API_BASE_URL + 'sections?sections=%s&premium=open&device=mobile&country=%s' % (section, country)

    oc = Videos(title1=GetTitle1(channel), title2=title2, videos_url=videos_url)

    if episodes:
        # Prepend Clips directory
        oc.objects.reverse()
        
        oc.add(
            DirectoryObject(
                key = 
                    Callback(
                        Latest, 
                        channel  = channel,
                        country  = country,
                        episodes = False, 
                    ),
                title = "Clips"
            )
        )
        
        oc.objects.reverse()
    return oc

####################################################################################################
@route(PREFIX + '/Popular')
def Popular(channel, country):

    if channel:
        videos_url = API_BASE_URL + 'sections?sections=videos.popular&premium=open&device=mobile&channel=%s' % channel
    else:
        videos_url = API_BASE_URL + 'sections?sections=videos.popular&premium=open&device=mobile&country=%s' % country

    return Videos(title1=GetTitle1(channel), title2='Popular', videos_url=videos_url)

####################################################################################################
@route(PREFIX + '/ChannelMenu')
def ChannelMenu(title, id, country, base_url, thumb):
    oc = ObjectContainer(title1 = TITLE, title2 = unicode(title))

    oc.add(
        DirectoryObject(
            key   = Callback(Latest, channel=id, country=None), 
            title = 'Latest',
            thumb = thumb
        )
    ) 

    oc.add(
        DirectoryObject(
            key   = Callback(Popular, channel=id, country=None),  
            title = 'Popular',
            thumb = thumb
        )
    )

    oc.add(
        DirectoryObject(
            # Seems channel must be added afterwards...
            key   = Callback(Categories, channel=id, country=country),
            title = 'Categories',
            thumb = thumb
        )
    )

    oc.add(
        DirectoryObject(
            key   = Callback(AllPrograms, channel=id, country=None),
            title = 'All Programs',
            thumb = thumb
        )
    )

    oc.add(
        InputDirectoryObject(
            key    = Callback(Search, channel=id, country=None),
            title  = 'Search Program',
            prompt = 'Search Program',
            thumb  = R(THUMB)
            )
        )
    
    return oc

####################################################################################################
def Search(query, channel, country, offset = 0):
    oc = ObjectContainer(title1 = GetTitle1(channel), title2 = 'Search Results')

    query   = unicode(query)
    results = []
    counter = 0

    videos = AllPrograms(channel, country).objects

    for video in videos:                
        # In case of single character - only compare initial character.
        if len(query) > 1 and query.lower() in video.title.lower() or \
                len(query) == 1 and query.lower() == video.title[0].lower():
                    
            results.append(
                {
                    'video': video, 
                    'title': video.title, 
                    'channel_title': video.source_title, 
                    'thumb': video.art
                }
            )
    
    results = sorted(results, key = lambda result: result['title'])           
    for result in results:
        counter = counter + 1
            
        if counter <= offset:
            continue
        
        video     = result['video']
        video.art = result['thumb']
                
        oc.add(video)
                    
        if len(oc) >= MAX_SEARCH_ITEMS:
            oc.objects.sort(key = lambda obj: obj.title)
                
            oc.add(
                NextPageObject(
                    key =
                        Callback(
                            Search,
                            query = query,
                            channel = channel,
                            country = country,
                            offset = counter
                        ),
                    title = "Next..."
                )
            )
            return oc

    if len(oc) == 0:
        return NoProgramsFound(oc)
    else:
        oc.objects.sort(key = lambda obj: obj.title)
        return oc

####################################################################################################
@route(PREFIX + '/Collections')
def Collections(country):

    oc = ObjectContainer(title1 = TITLE, title2 = unicode("Collections"))

    url = API_BASE_URL + 'collections?country=%s&device=mobile&premium=open' % country

    collectionsInfo = JSON.ObjectFromURL(url)
    pages = int(collectionsInfo['count']['total_pages'])
    for page in range(pages):
        for collection in collectionsInfo['_embedded']['collections']:
            oc.add(
                DirectoryObject(
                    key = 
                        Callback(
                            Programs,
                            title1 = TITLE,
                            title2 = unicode(collection['title']),
                            url    = collection['_links']['self']['href']
                        ),
                    title = unicode(collection['title']),
                    thumb = FixThumb(collection)
                )
             )
        
        if page + 2 > pages:
            break
        
        if pages > 1:
            collectionsInfo = JSON.ObjectFromURL(url + '&page=%s' % (page + 2))['_embedded']['sections'][0]

    if len(oc) < 1:
        return NoCollectionsFound(oc)

    return oc

####################################################################################################
@route(PREFIX + '/Categories')
def Categories(channel, country):

    oc = ObjectContainer(title1 = TITLE, title2 = unicode("Categories"))

    url = API_BASE_URL + 'categories?country=%s&device=mobile&premium=open' % country

    if channel:
        oc.title1 = GetChannelName(channel)

    categoriesInfo = JSON.ObjectFromURL(url)
    pages = int(categoriesInfo['count']['total_pages'])
    for page in range(pages):
        for category in categoriesInfo['_embedded']['categories']:
            programs_url = category['_links']['formats']['href']
            if channel:
                programs_url = programs_url + "&channel=%s" % channel
            oc.add(
                DirectoryObject(
                    key = 
                        Callback(
                            Programs,
                            title1 = oc.title1,
                            title2 = unicode(category['name']),
                            url    = programs_url
                        ),
                    title = unicode(category['name']),
                    thumb = FixThumb(category)
                )
             )
        
        if page + 2 > pages:
            break
        
        if pages > 1:
            categoriesInfo = JSON.ObjectFromURL(url + '&page=%s' % (page + 2))

    if len(oc) < 1:
        return NoCategoriesFound(oc)

    oc.objects.sort(key = lambda obj: obj.title)
  
    return oc

####################################################################################################
@route(PREFIX + '/AllPrograms')
def AllPrograms(channel, country):

    title1 = TITLE

    if channel:
        url = API_BASE_URL + 'formats?channel=%s&device=mobile&premium=open' % channel
        title1 = GetChannelName(channel)
    else:
        url = API_BASE_URL + 'formats?device=mobile&premium=open&country=%s' % country

    return Programs(title1, unicode("All Programs"), url)

####################################################################################################
@route(PREFIX + '/Programs')
def Programs(title1, title2, url):

    oc = ObjectContainer(title1 = title1, title2 = title2)
    
    programsInfo = JSON.ObjectFromURL(url)
    if 'count' in programsInfo:
        pages = int(programsInfo['count']['total_pages'])
    elif 'type' in programsInfo['_embedded']['items'][0]:
        # Assume episodes of collection
        return Videos(title1=title1, title2=title2, videos_url=url)
    else:
        pages = 1
        
    source_title = None
    for page in range(pages):

        if 'formats' in programsInfo['_embedded']:
            programs = programsInfo['_embedded']['formats']
        else:
            programs = programsInfo['_embedded']['items']

        for program in programs:
            if title1 == TITLE:
                source_title = GetChannelName(program['channel_id'])
            oc.add(
                TVShowObject(
                    key = 
                        Callback(
                            Seasons,
                            title1 = title1,
                            title2 = unicode(program['title']),
                            id = program['id']
                        ),
                    rating_key = program['id'],
                    title = unicode(program['title']),
                    source_title = source_title,
                    thumb = program['image'] if 'image' in program else FixThumb(program)
                )
             )
        
        if page + 2 > pages:
            break
        
        if pages > 1:
            programsInfo = JSON.ObjectFromURL(url + '&page=%s' % (page + 2))

    if len(oc) < 1:
        return NoProgramsFound(oc)

    oc.objects.sort(key = lambda obj: obj.title)
  
    return oc

####################################################################################################
@route(PREFIX + '/Seasons')
def Seasons(title1, title2, id):
    oc = ObjectContainer(title1 = unicode(title1), title2 = unicode(title2))

    seasons = JSON.ObjectFromURL(API_BASE_URL + 'seasons?format=%s' % id)['_embedded']['seasons']
    seasons = DeleteEmptySeasons(seasons)
    if len(seasons) == 1:
        try:
            art = seasons[0]['_links']['image']['href'].replace("{size}", "994x560")
        except:
            art = R(ART)
            
        return VideoTypeChoice(
            show  = title2,
            title = unicode(seasons[0]['title']),
            videos_url = seasons[0]['_links']['videos']['href'],
            art = art
        ) 
    
    else:
        for season in seasons:
            seasonName = unicode(season['title'])
            
            try:
                seasonImg = season['_links']['image']['href'].replace("{size}", "994x560")
            except:
                seasonImg = R(ART)

            try:
                index = int(re.sub("[^0-9]+","",season['format_position']['season']))
            except:
                index = None

            oc.add(
                SeasonObject(
                    key = 
                        Callback(
                            VideoTypeChoice, 
                            show       = title2,
                            title      = seasonName, 
                            videos_url = season['_links']['videos']['href'],
                            art        = seasonImg
                        ), 
                    rating_key = season['_links']['videos']['href'],
                    index      = index,
                    title      = seasonName,  
                    show       = title2,
                    thumb      = seasonImg,
                    art        = seasonImg
                )
            ) 

    try:
        oc.objects.sort(key = lambda obj: int(re.sub("[^0-9]+","",obj.title)), reverse = True)
    except:
        pass

    return oc

####################################################################################################
def DeleteEmptySeasons(seasons):
    result = []
    for s in seasons:
        try:
            videos = JSON.ObjectFromURL(s['_links']['videos']['href'])
            if videos['count']['total_items'] == 0:
                continue
        except Exception as e:
            pass
        result.append(s)

    return result

####################################################################################################
@route(PREFIX + '/VideoTypeChoice')
def VideoTypeChoice(show, title, videos_url, art = R(ART)):
    episodes_oc = Episodes(
        show  = show,
        title = title,
        videos_url = videos_url,
        art = art
    )

    if len(episodes_oc) < 1:
        return Clips(
            show = show,
            title = title,
            videos_url = videos_url,
            art = art
        )
    
    else:
        clips_oc = Clips(
            show = show,
            title = title,
            videos_url = videos_url,
            art = art
        )
        
        oc = ObjectContainer(title1 = unicode(show), title2 = unicode(title))
        
        if len(clips_oc) > 0:
            oc.add(
                DirectoryObject(
                    key =
                        Callback(
                            Clips,
                            show = show,
                            title = title,
                            videos_url = videos_url,
                            art = art
                        ),
                    title = 'Clips'
                )
            )
        
        for object in episodes_oc.objects:
            oc.add(object)

        return oc

####################################################################################################
@route(PREFIX + '/Episodes')
def Episodes(show, title, videos_url, art = R(ART)):
    return Videos(
        title1 = show,
        title2 = title,
        videos_url = videos_url + "&type=program",
        art = art,
        sort = True
    )
    
####################################################################################################
@route(PREFIX + '/Clips')
def Clips(show, title, videos_url, art = R(ART)):
    return Videos(
        title1 = show,
        title2 = title + " - Clips",
        videos_url = videos_url + "&type=clip",
        art = art,
        sort = True
    )
 
####################################################################################################
@route(PREFIX + '/Videos', sort = bool)
def Videos(title1, title2, videos_url, art = R(ART), sort=False):
    oc = ObjectContainer(title1 = unicode(title1), title2 = unicode(title2))
    
    try:
        videosInfo = JSON.ObjectFromURL(videos_url)
    except:
        return NoProgramsFound(oc)

    nextUrl = None
    try:
        videos = videosInfo['_embedded']['sections'][0]['_embedded']['videos']
        if 'next' in videosInfo['_embedded']['sections'][0]['_links']:
            nextUrl = videosInfo['_embedded']['sections'][0]['_links']['next']['href']
    except:
        try:
            videos = videosInfo['_embedded']['videos']
            if 'next' in videosInfo['_links']:
                nextUrl = videosInfo['_links']['next']['href']
        except:
            try:
                videos = videosInfo['_embedded']['items']
            except:
                return NoProgramsFound(oc)
    
    if videos:
        for video in videos:
            source_title = None
            if not "channel=" in videos_url and "country=" in videos_url:
                source_title = GetChannelName(video['channel_id'])
            try:
                if video['publishing_status']['login_required']:
                    continue
            except:
                continue
            
            try:
                url = video['sharing']['url'].replace("..", ".")
            except:
                continue
            
            try:
                title = unicode(video['title']).strip()
                org_title = title
            except:
                continue

            try:
                show = unicode(video['format_title'])
            except:
                show = None

            if sort and show and re.compile(ur'\b%s\b' % show, re.UNICODE).search(title):
                title = title + " - " + unicode(video['summary']).strip()
                title = re.sub(show+"[ 	\-,:]*((S[0-9]+)*E[0-9]+[ 	\-,:]*)*(.+)", "\\3", title)
                if title.strip() == "":
                    title = re.sub(show+"[ 	\-,:]*(.+)", "\\1", org_title)

            try:
                summary = unicode(video['summary']).strip()
                description = unicode(video['description'].strip())
                if not description in summary:
                    if description.endswith('.'):
                        summary = description + " " + summary
                    else:
                        summary = description + ". " + summary

                if 'premium' in video:
                    summary = AddAvailability(video['premium'], summary)
            except:
                summary = None

            try:
                thumb = FixThumb(video)
            except:
                thumb = None
                
            try:
                originally_available_at = Datetime.ParseDate(video['publish_at'].split("T")[0]).date()
            except:
                originally_available_at = None
                
            try:
                duration = int(video['duration']) * 1000
            except:
                duration = None
            
            try:
                season = int(video['format_position']['season'])
            except:
                season = None
                
            try:
                index = int(re.sub("[^0-9]+","",video['format_position']['episode']))
            except:
                index = None

            if source_title and not video['channel_id'] in CHANNELS:
                oc.add(
                    DirectoryObject(
                        key = Callback(ChannelNotSupported, channel=source_title),
                        title = title,
                        summary = summary,
                        duration = duration,
                        thumb = thumb,
                        art = art
                        )
                    )
            else:
                oc.add(
                    EpisodeObject(
                        url = url,
                        title = title,
                        source_title = source_title,
                        summary = summary,
                        show = show,
                        art = art,
                        thumb = thumb,
                        originally_available_at = originally_available_at,
                        duration = duration,
                        season = season,
                        index = index
                        )
                    )
            
    if len(oc) < 1:
        return NoProgramsFound(oc)
    else:
        if sort:
            try:
                sortOnAirData(oc)
            except:
                pass

        if nextUrl:
            oc.add(
                NextPageObject(
                    key =
                    Callback(
                        Videos,
                        title1 = title1,
                        title2 = title2,
                        videos_url = nextUrl,
                        art = art,
                        sort = sort
                        )
                    )
                )

    return oc

####################################################################################################
def NoCollectionsFound(oc):
    oc.header  = "Sorry"
    oc.message = "No collections found."
     
    return oc

####################################################################################################
def NoCategoriesFound(oc):
    oc.header  = "Sorry"
    oc.message = "No categories found."
     
    return oc

####################################################################################################
def NoProgramsFound(oc):
    oc.header  = "Sorry"
    oc.message = "No programs found."
     
    return oc
   
####################################################################################################
@route(PREFIX + '/NoCountrySelected')
def NoCountrySelected():
    oc = ObjectContainer()
    
    oc.header  = "Please select country"
    oc.message = "Select country in preferences to get started"
     
    return oc

####################################################################################################
@route(PREFIX + '/ChannelNotSupported')
def ChannelNotSupported(channel):
    oc         = ObjectContainer()
    oc.header  = unicode("%s is possibly a new Channel" % channel)
    oc.message = unicode("A new version of this plugin is required to watch this.")
    
    return oc

####################################################################################################
def GetChannelName(channel_id):
    if len(CHANNEL_NAMES) == 0:
        FetchChannelNames()
    for (channel, name) in CHANNEL_NAMES:
        if int(channel_id) == int(channel):
            return name
    Log("ChannelName not found for channel_id:%r channels:%r" % (channel_id, CHANNEL_NAMES))
    
    return None

####################################################################################################
def FetchChannelNames():
    global CHANNEL_NAMES
    data = JSON.ObjectFromURL(API_BASE_URL + 'channels/')
    for c in data['_embedded']['channels']:
        if c['country'] in COUNTRIES[Prefs['country']]:
            CHANNEL_NAMES.append((c['id'], c['name']))

####################################################################################################
def GetTitle1(channel):
    if channel:
        return GetChannelName(channel)
    else:
        return TITLE
    
####################################################################################################
def FixThumb(data):
    try:
        return data['_links']['image']['href'].replace("{size}", "497x280")
    except:
        return None

####################################################################################################
def sortOnAirData(Objects):
    for obj in Objects.objects:
        if obj.originally_available_at == None:
            # Assume given Objects are in correct order
            return Objects
    return Objects.objects.sort(key=lambda obj: (obj.originally_available_at,obj.title), reverse=True)

####################################################################################################
def AddAvailability(premium, summary):
    try:
        return unicode('Availability: %i days. \n%s' % (premium['time_left']['days'], summary))
    except:
        return summary
