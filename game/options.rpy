﻿
define config.name = _("Resurrection of Hikikomori")


define gui.show_name = True




define config.version = "2.0"




define gui.about = _p("""
""")




define build.name = "Resurrection_of_Hikikomori"




define config.has_sound = True
define config.has_music = True
define config.has_voice = True





define config.main_menu_music = "audio/main-menu-theme.mp3"




define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None




define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)




default preferences.text_cps = 35


default preferences.afm_time = 15




define config.save_directory = "Resurrection_of_Hikikomori"




define config.window_icon = "gui/window_icon.png"




init python:


    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)



    build.documentation('*.html')
    build.documentation('*.txt')


