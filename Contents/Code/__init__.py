TITLE  = 'Viasat Play'
PREFIX = '/video/viasatplay'

ART   = "art-default.jpg"
THUMB = 'icon-default.png'

MAX_SEARCH_ITEMS = 50

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
    oc = ObjectContainer(title1 = TITLE, no_cache = True)
    
    if Prefs['country'] != 'None':
        country = COUNTRIES[Prefs['country']][0]
        
        title = 'Latest'
        oc.add(
            DirectoryObject(
                key = 
                    Callback(
                        Videos, 
                        title = title,
                        videos_url = API_BASE_URL + 'sections?sections=videos.latest&premium=open&device=mobile&country=%s' % country
                    ), 
                title = title
            )
        )
        
        title = 'Popular'
        oc.add(
            DirectoryObject(
                key = 
                    Callback(
                        Videos, 
                        title = title,
                        videos_url = API_BASE_URL + 'sections?sections=videos.popular&premium=open&device=mobile&country=%s' % country
                    ), 
                title = title
            )
        )
        
        data = JSON.ObjectFromURL(API_BASE_URL + 'channels/')
        
        for channel in data['_embedded']['channels']:
            if channel['country'] in COUNTRIES[Prefs['country']]:
                oc.add(
                    DirectoryObject(
                        key = 
                            Callback(
                                ChannelMenu, 
                                title = channel['name'], 
                                id = channel['id'],
                                base_url = CHANNELS[channel['id']]['base_url'],
                                thumb = CHANNELS[channel['id']]['thumb']
                            ), 
                        title = channel['name'],
                        summary = CHANNELS[channel['id']]['desc'],
                        thumb = CHANNELS[channel['id']]['thumb']
                    )
                )
        
        oc.add(
            InputDirectoryObject(
                key = Callback(Search),
                title  = 'Search Program',
                prompt = 'Search Program',
                thumb = R(THUMB)
            )
        )
    else:
        oc.add(
            DirectoryObject(
                key =
                    Callback(
                        NoCountrySelected
                    ),
                title = 'Please select country',
                summary = 'Select country in preferences to get started'
            )
        )
        
    oc.add(PrefsObject(title = "Preferences..."))
    
    return oc

####################################################################################################
@route(PREFIX + '/ChannelMenu')
def ChannelMenu(title, id, base_url, thumb):
    oc = ObjectContainer(title2 = unicode(title))
    
    title = 'Latest'
    oc.add(
        DirectoryObject(
            key = 
                Callback(
                    Videos, 
                    title = title,
                    videos_url = API_BASE_URL + 'sections?sections=videos.latest&premium=open&device=mobile&channel=%s' % id
                ), 
            title = title, 
            thumb = thumb
        )
    ) 

    title = 'Popular'
    oc.add(
        DirectoryObject(
            key = 
                Callback(
                    Videos, 
                    title = title, 
                    videos_url = API_BASE_URL + 'sections?sections=videos.popular&premium=open&device=mobile&channel=%s' % id
                ), 
            title = title, 
            thumb = thumb
        )
    )  
    
    title = 'All programs'
    oc.add(
        DirectoryObject(
            key = 
                Callback(
                    AllPrograms, 
                    title = title, 
                    url = API_BASE_URL + 'formats?channel=%s&device=mobile&premium=open' % id
                ), 
            title = title, 
            thumb = thumb
        )
    )
    
    return oc

####################################################################################################
def Search(query, offset = 0):
    oc = ObjectContainer(title1 = TITLE, title2 = 'Search Results')

    country = COUNTRIES[Prefs['country']][0]
        
    result = JSON.ObjectFromURL(API_BASE_URL + 'search?term=%s&country=%s&device=mobile&premium=open&limit=%s' % (String.Quote(query), country, MAX_SEARCH_ITEMS))
    
    if int(result['count']['total_items']) < 1:
        return NoProgramsFound(oc)
    
    for program in result['_embedded']['formats']:
        try:
            title = unicode(program['title'])
            id = program['id']
        except:
            continue
        
        try:
            thumb = program['_links']['image']['href'].replace("{size}", "497x280")
        except:
            thumb = R(THUMB)
            
        oc.add(
            DirectoryObject(
                key =
                    Callback(
                        Seasons,
                        title = title,
                        id = id
                    ),
                title = title,
                thumb = thumb
            )
        )
            

    if len(oc) == 0:
        return NoProgramsFound(oc)
    else:
        oc.objects.sort(key = lambda obj: obj.title)
        return oc

####################################################################################################
@route(PREFIX + '/AllPrograms')
def AllPrograms(title, url):
    oc = ObjectContainer(title2 = unicode(title))
    
    programsInfo = JSON.ObjectFromURL(url)
    pages = int(programsInfo['count']['total_pages'])
    
    for page in range(pages):
        for program in programsInfo['_embedded']['formats']:
            oc.add(
                DirectoryObject(
                    key = 
                        Callback(
                            Seasons,
                            title = unicode(program['title']),
                            id = program['id']
                        ),
                    title = unicode(program['title']),
                    thumb = program['image']
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
def Seasons(title, id):
    oc = ObjectContainer(title2 = unicode(title))
  
    seasonsInfo = JSON.ObjectFromURL(API_BASE_URL + 'seasons?format=%s' % id)
    
    if len(seasonsInfo['_embedded']['seasons']) == 1:
        try:
            art = seasonsInfo['_embedded']['seasons'][0]['_links']['image']['href'].replace("{size}", "994x560")
        except:
            art = R(ART)
            
        return VideoTypeChoice(
            title = unicode(seasonsInfo['_embedded']['seasons'][0]['title']),
            videos_url = seasonsInfo['_embedded']['seasons'][0]['_links']['videos']['href'],
            art = art
        ) 
    
    else:
        for season in seasonsInfo['_embedded']['seasons']:
            seasonName = unicode(season['title'])
            
            try:
                seasonImg = season['_links']['image']['href'].replace("{size}", "994x560")
            except:
                seasonImg = R(ART)

            oc.add(
                DirectoryObject(
                    key = 
                        Callback(
                            VideoTypeChoice, 
                            title      = seasonName, 
                            videos_url = season['_links']['videos']['href'],
                            art        = seasonImg
                        ), 
                    title   = seasonName,  
                    thumb   = seasonImg,
                    art     = seasonImg
                )
            ) 

    return oc


####################################################################################################
@route(PREFIX + '/VideoTypeChoice')
def VideoTypeChoice(title, videos_url, art = R(ART)):
    episodes_oc = Episodes(
        title = title,
        videos_url = videos_url,
        art = art
    )
    
    if len(episodes_oc) < 1:
        return Clips(
            title = title,
            videos_url = videos_url,
            art = art       
        )
    
    else:
        clips_oc = Clips(
            title = title,
            videos_url = videos_url,
            art = art
        )
        
        oc = ObjectContainer(title2 = unicode(title))
        
        if len(clips_oc) > 0:
            oc.add(
                DirectoryObject(
                    key =
                        Callback(
                            Clips,
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
def Episodes(title, videos_url, art = R(ART)):
    return Videos(
        title = title,
        videos_url = videos_url + "&type=program",
        art = art
    )
    
####################################################################################################
@route(PREFIX + '/Clips')
def Clips(title, videos_url, art = R(ART)):
    return Videos(
        title = title,
        videos_url = videos_url + "&type=clip",
        art = art
    )
 
####################################################################################################
@route(PREFIX + '/Videos')
def Videos(title, videos_url, art = R(ART)):
    oc = ObjectContainer(title2 = unicode(title))
    
    orgTitle = title

    try:
        videosInfo = JSON.ObjectFromURL(videos_url)
    except:
        return NoProgramsFound(oc)

    try:
        videos = videosInfo['_embedded']['sections'][0]['_embedded']['videos']
    except:
        try:
            videos = videosInfo['_embedded']['videos']
        except:
            return NoProgramsFound(oc)
    
    if videos:
        for video in videos:
            if video['publishing_status']['login_required']:
                continue
            
            try:
                url = video['sharing']['url'].replace("..", ".")
            except:
                continue
            
            try:
                title = unicode(video['title'])
            except:
                continue
                
            try:
                summary = unicode(video['summary'])
            except:
                summary = None
                
            try:
                show = unicode(video['format_title'])
            except:
                show = None
                
            try:
                thumb = video['_links']['image']['href'].replace("{size}", "497x280")
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
                index = int(video['format_position']['episode'])
            except:
                index = None
                
            oc.add(
                EpisodeObject(
                    url = url,
                    title = title,
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
    
    elif 'next' in videosInfo['_links']:
        oc.add(
            NextPageObject(
                key =
                    Callback(
                        Videos,
                        title = orgTitle,
                        videos_url = videosInfo['_links']['next']['href'],
                        art = art
                    )
            )
        )

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

