Config { font    = "xft:Mononoki Nerd Font:pixelsize=15:antialias=true:hinting=true"
       , bgColor = "#282c34"
       , fgColor = "#ff6c6b"
       , position = Static { xpos = 0 , ypos = 0, width = 3440, height = 24 }
       , lowerOnStart = True
       , hideOnStart = False
       , allDesktops = True
       , persistent = True
       , commands = [
			Run Cpu       [ "--template" , ": <total>%"
                             , "--Low"      , "50"         -- units: %
                             , "--High"     , "85"         -- units: %
                             , "--low"      , "#A3BE8C"
                             , "--normal"   , "#EBCB8B"
                             , "--high"     , "#BF616A"
                             ] 10
			, Run Memory         [ "--template" ,": <usedratio>%"
					     , "--Low"      , "20"        -- units: %
					     , "--High"     , "90"        -- units: %
					     , "--low"      , "#A3BE8C"
					     , "--normal"   , "#EBCB8B"
					     , "--high"     , "#BF616A"
					     ] 10

			, Run Date           "<fc=#EBCB8B>%a %b %_d %Y %H:%M:%S</fc>" "date" 10
            , Run Com "/home/jt/.xmonad/get-volume" [] "myvolume" 10
            , Run Com "/bin/sh" ["/home/jt/.xmonad/music.sh"] "spotify" 10
			, Run   WeatherX "CYTZ"--  https://en.wikipedia.org/wiki/List_of_airports_by_ICAO_code:_K#K_%E2%80%93_United_States
			   [ ("clear", "望")
			   , ("sunny", "")
			   , ("mostly clear", "")
			   , ("mostly sunny", "盛")
			   , ("partly sunny", "")
			   , ("fair", "")
			   , ("cloudy","")
			   , ("overcast","")
			   , ("partly cloudy", "杖")
			   , ("mostly cloudy", "")
			   , ("considerable cloudiness", "")]
			   ["-t", "<skyConditionS> <tempC>糖  <rh>%  <windKmh>"
			   , "-L","10", "-H", "25", "--normal", "#EBCB8B"
			   , "--high", "#BF616A", "--low", "#A3BE8C"]
			   1800
			, Run Com "/home/jt/.xmonad/trayer-padding-icon.sh" [] "trayerpad" 5
			, Run StdinReader
                    ]
       , sepChar = "%"
       , alignSep = "}{"
       , template = "%StdinReader% }{ %spotify%%CYTZ% | %cpu% | %memory% | 墳 %myvolume% | %date%%trayerpad%"
       }
