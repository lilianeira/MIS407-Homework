#Test Case: 3

1. Objective
--------------------------

This Test Case will manually test all of the commands used in the sports function.

2. Command being tested:
------------------------------

  * what iowa state athletics events are coming up: all sports
  * what games are coming up: all sports
  * what's going on in isu sports: all sports
  * what's coming up in sports: all sports
  * when are the next mens basketball games: Men's Basketball
  * when is the next men's basketball game: Men's Basketball
  * what's coming up in men's basketball: Men's Basketball
  * when are the next women's basketball games: Women's Basketball
  * when is the next women's basketball game: Women's Basketball
  * what's coming up in women's basketball: Women's Basketball
  * when is the next cross country meet: Cross Country
  * when are the next cross country meets: Cross Country
  * what's coming up in cross country: Cross Country
  * when is the next men's golf tournament: Men's Golf
  * "when is the next men's golf competition: Men's Golf
  * what's coming up in men's golf?: Men's Golf
  * when is the next women's golf tournament: Women's Golf
  * what is the next women's golf competition: Women's Golf
  * what's coming up in women's golf: Women's golf
  * when are the next football games: Football
  * when is the next football game: Football
  * what's coming up in football: Football
  * when is the next wrestling meet: Wrestling
  * when are the next wrestling meets: Wrestling
  * what's coming up in wrestling: Wrestling
  * when is the next track meet: Track and Field
  * when are the upcoming track meets: Track and Field
  * what's coming up in track and field: Track and Field
  * when is the next softball game: Softball
  * when are the next softball games: Softball
  * what's coming up in softball: Softball
  * what in the next gymnastics meet: Gymnastics
  * when are the next gymnastics meets: Gymnastics
  * what's coming up in gymnastics: Gymnastics
  * when is the next soccer game: Soccer
  * when is the next soccer match: Soccer
  * what's coming up in soccer: Soccer
  * when is the next swim meet: Swimming
  * when is the next swimming competition: Swimming
  * what's coming up in swimming: Swimming
  * when is the next tennis match: Tennis
  * when is the next tennis game: Tennis
  * what's coming up in tennis: Tennis
  * when is the next volleyball game: Volleyball
  * what is the next volleyball match: Volleyball
  * what's coming up in volleyball: Volleyball


3. Expected output
--------------------------------
  * For each individual sport command we expect up to the next four events of the requested sport to be given. If none are scheduled CyBot will respond "No upcoming events for that sport are scheduled at this time."
  * When a general all sports command is called we expect the next four events of all sports to be given


4. Observed output:
----------------------------
  * For all sports commands:
    - 11/2 2:00 PM Soccer vs  Oklahoma in Kansas City, Mo. 11/2 6:30 PM Volleyball vs  West Virginia in Ames, Iowa 11/3 6:30 PM Football vs  Oklahoma in Ames, Iowa 11/4 7:00 PM Wrestling at  South Dakota State in Brookings, S.D.
  * For men's basketball:
    - 11/6 6:00 PM Men's Basketball vs  Sioux Falls (Exhibition) in Ames, Iowa 11/11 7:00 PM Men's Basketball vs  Savannah State in Ames, Iowa 11/14 7:00 PM Men's Basketball vs  Mount St. Mary's (Md.) in Ames, Iowa 11/20 1:00 PM Men's Basketball vs  The Citadel in Ames, Iowa
  * For women's basketball:
    - 11/6 1:00 PM Women's Basketball vs  Briar Cliff University (Iowa) in Ames, Iowa 11/11 12:00 PM Women's Basketball vs  UCSB in Ames, Iowa 11/15 7:00 PM Women's Basketball vs  UNI in Ames, Iowa 11/20 6:00 PM Women's Basketball vs  Drake in Ames, Iowa
  * For cross country:
    - 11/11 12:00 PM Cross Country vs  NCAA Midwest Regional in Iowa City, Iowa 11/19 11:00 AM Cross Country vs  NCAA Championship in Terre Haute, Ind.
  * For men's golf:
    - 1/23 Men's Golf vs  Arizona Intercollegiate in Tucson, Ariz. 1/24 Men's Golf vs  Arizona Intercollegiate in Tucson, Ariz. 2/20 Men's Golf vs  Prestige at PGA West in La Quinta, Calif. 2/21 Men's Golf vs  Prestige at PGA West in La Quinta, Calif.
  * For women's golf:
    - 1/29 Women's Golf vs  Northwestern University in West Palm Beach, Calif. 2/5 Women's Golf vs  Central Florida Invitational in Orlando, Fla. 2/6 Women's Golf vs  Central Florida Invitational in Orlando, Fla. 2/7 Women's Golf vs  Central Florida Invitational in Orlando, Fla.
  * For football:
    - 11/3 6:30 PM Football vs  Oklahoma in Ames, Iowa 11/12 11:00 AM Football at  Kansas in Lawrence, Kan. 11/19 Football vs  Texas Tech in Ames, Iowa 11/26 Football vs  West Virginia in Ames, Iowa
  * For wrestling:
    - 11/4 7:00 PM Wrestling at  South Dakota State in Brookings, S.D. 11/6 2:00 PM Wrestling at  North Dakota State in Fargo, N.D. 11/13 Wrestling vs  Harold Nichols Cyclone Open in Ames, Iowa 11/26 3:00 PM Wrestling at  Northern Colorado in Greeley, Colo.
  * For track and field:
    - 1/14 Track and Field at  Hawkeye Challenge in Iowa City, Iowa 1/20 Track and Field at  Power 5 Premier Invitational in Iowa City, Iowa 1/21 Track and Field at  Power 5 Premier Invitational in Iowa City, Iowa 2/3 Track and Field at  Husker Invitational in Lincoln, Neb.
  * For softball:
    - No upcoming events for that sport are scheduled at this time.
  * For gymnastics:
    - 1/6 6:30 PM Gymnastics vs  Arizona State (Beauty & the Beast) in Ames, Iowa 1/13 6:30 PM Gymnastics vs  Towson in Ames, Iowa 1/13 6:30 PM Gymnastics vs  Wisconsin-Oshkosh in Ames, Iowa 1/21 5:00 PM Gymnastics at  Arizona in Tucson, Ariz.
  * For soccer:
    - 11/2 2:00 PM Soccer vs  Oklahoma in Kansas City, Mo.
  * For swimming:
    - 11/4 6:00 PM Swimming and Diving at  Texas Christian in Forth Worth, TX 11/17 Swimming and Diving at  Mizzou Invite (Divers Only) in Columbia, Mo. 11/18 Swimming and Diving at  The Big Challenge in Topeka, Kan. 12/2 Swimming and Diving at  Jean Freeman Invite (Divers Only) in Minneapolis, Minn.
  * For tennis:
    - No upcoming events for that sport are scheduled at this time.
  * For volleyball:
    - 11/2 6:30 PM Volleyball vs  West Virginia in Ames, Iowa 11/4 5:00 PM Volleyball at  Texas Tech in Lubbock, Texas 11/9 7:00 PM Volleyball at  Oklahoma in Norman, Okla. 11/12 4:00 PM Volleyball vs  Texas in Ames, Iowa

5. The test is passed
------------------------------------

  10/31/2016:21:12
  Version: 00.03
