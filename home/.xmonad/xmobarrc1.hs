Config { font    = "xft:Mononoki Nerd Font:pixelsize=15:antialias=true:hinting=true"
       , bgColor = "#282c34"
       , fgColor = "#ff6c6b"
       , position = Static { xpos = 3440 , ypos = 0, width = 1080, height = 24 }
       , lowerOnStart = True
       , hideOnStart = False
       , allDesktops = True
       , persistent = True
       , commands = [
			  Run Date           "<fc=#EBCB8B>%a %b %_d %Y %H:%M:%S</fc>" "date" 10
			, Run StdinReader
                    ]
       , sepChar = "%"
       , alignSep = "}{"
       , template = "%StdinReader% }{ %date% " 
       }
