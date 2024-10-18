# TODO: Translation updated at 2024-10-17 03:54

translate russian strings:

    # game/screens.rpy:424
    old "History"
    new "История"

    # game/screens.rpy:425
    old "Skip"
    new "Пропуск"

    # game/screens.rpy:426
    old "Auto"
    new "Авто"

    # game/screens.rpy:427
    old "Save"
    new "Сохранить"

    # game/screens.rpy:428
    old "Load"
    new "Загрузить"

    # game/screens.rpy:431
    old "Settings"
    new "Настройки"

    # game/screens.rpy:482
    old "ŔŗñĮ¼»ŧþŀÂŻŕěōì«"
    new "ŔŗñĮ¼»ŧþŀÂŻŕěōì«"

    # game/screens.rpy:484
    old "New Game"
    new "Новая игра"

    # game/screens.rpy:490
    old "Save Game"
    new "Сохранить игру"

    # game/screens.rpy:492
    old "Load Game"
    new "Загрузить игру"

    # game/screens.rpy:495
    old "Extras"
    new "Экстра"

    # game/screens.rpy:499
    old "End Replay"
    new "Завершить повтор"

    # game/screens.rpy:503
    old "Main Menu"
    new "Главное меню"

    # game/screens.rpy:510
    old "Credits"
    new "Авторы"

    # game/screens.rpy:518
    old "Quit"
    new "Выход"

    # game/screens.rpy:705
    old "Return"
    new "Вернуться"

    # game/screens.rpy:802
    old "Version [config.version!t]\n"
    new "Версия [config.version!t]\n"

    # game/screens.rpy:813
    old "Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n[renpy.license!t]"
    new "Сделано с помощью {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n[renpy.license!t]"

    # game/screens.rpy:921
    old "{#file_time}%A, %B %d %Y, %H:%M"
    new "{#file_time}%A, %d %B %Y, %H:%M"

    # game/screens.rpy:921
    old "empty slot"
    new "Пустой слот"

    # game/screens.rpy:1122
    old "Display"
    new "Режим экрана"

    # game/screens.rpy:1123
    old "Windowed"
    new "Оконный"

    # game/screens.rpy:1124
    old "Fullscreen"
    new "Полный"

    # game/screens.rpy:1130
    old "Rollback Side"
    new "Сторона отката"

    # game/screens.rpy:1131
    old "Disable"
    new "Отключено"

    # game/screens.rpy:1132
    old "Left"
    new "Левая"

    # game/screens.rpy:1133
    old "Right"
    new "Правая"

    # game/screens.rpy:1138
    old "Unseen Text"
    new "Всего текста"

    # game/screens.rpy:1139
    old "After Choices"
    new "После выборов"

    # game/screens.rpy:1151
    old "Text Speed"
    new "Скорость текста"

    # game/screens.rpy:1161
    old "Auto-Forward Time"
    new "Скорость авточтения"

    # game/screens.rpy:1173
    old "Music Volume"
    new "Громкость музыки"

    # game/screens.rpy:1185
    old "Sound Volume"
    new "Громкость звуков"

    # game/screens.rpy:1195
    old "Test"
    new "Тест"

    # game/screens.rpy:1199
    old "Voice Volume"
    new "Громкость голоса"

    # game/screens.rpy:1214
    old "Mute All"
    new "Без звука"

    # game/screens.rpy:1225
    old "Game Modes"
    new "Игровые режимы"

    # game/screens.rpy:1226
    old "Uncensored Mode"
    new ""

    # game/screens.rpy:1232
    old "Let's Play Mode"
    new ""

    # game/screens.rpy:1241
    old "Player Name"
    new ""

    # game/screens.rpy:1246
    old "No Name Set"
    new ""

    # game/screens.rpy:1250
    old "Change Name"
    new ""

    # game/screens.rpy:1263
    old "Discord RPC"
    new ""

    # game/screens.rpy:1266
    old "Disconnected"
    new ""

    # game/screens.rpy:1268
    old "Disabled"
    new ""

    # game/screens.rpy:1270
    old "Connected"
    new ""

    # game/screens.rpy:1277
    old "Enable"
    new "Активировано"

    # game/screens.rpy:1285
    old "Reconnect"
    new ""

    # game/screens.rpy:1296
    old "Language"
    new "Язык"

    # game/screens.rpy:1477
    old "The dialogue history is empty."
    new "История диалогов пуста."

    # game/screens.rpy:1714
    old "OK"
    new "ОК"

    # game/screens.rpy:1795
    old "Yes"
    new "Да"

    # game/screens.rpy:1796
    old "No"
    new "Нет"

    # game/screens.rpy:1849
    old "Skipping"
    new "Пропускаю"

    # game/screens.rpy:2061
    old "{#in language font}Please select a language"
    new "{font=gui/font/allercyrillic.ttf}Пожалуйста выберите язык{/font}"

    # game/screens.rpy:2068
    old "English"
    new "Английский"

    # game/screens.rpy:2073
    old "Russian"
    new "Русский"

    # game/screens.rpy:2086
    old "{#in language font}Select"
    new "{font=gui/font/riffic-bold.ttf}Выбрать{/font}"

translate russian style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font "gui/font/riffic-bold.ttf"
    color "#7eafa0"
    outlines [(4, "#a200ff", 0, 0), (2, "#a200ff", 2, 2)]
    hover_outlines [(4, "#7eafa0", 0, 0), (2, "#7eafa0", 2, 2)]
    hover_color "#a200ff"
    insensitive_outlines [(4, "#dea5ff", 0, 0), (2, "#dea5ff", 2, 2)]

translate russian style nav_button_text:
    font "gui/font/riffic-bold.ttf"
    color "#7eafa0"
    outlines [(4, "#a200ff", 0, 0), (2, "#a200ff", 2, 2)]
    hover_outlines [(4, "#7eafa0", 0, 0), (2, "#7eafa0", 2, 2)]
    hover_color "#a200ff"
    insensitive_outlines [(4, "#dea5ff", 0, 0), (2, "#dea5ff", 2, 2)]
    xalign 0.0


translate russian style game_menu_label_text:
    font "gui/font/riffic-bold.ttf"
    size gui.title_text_size
    color "#fff"
    outlines [(6, text_outline_color, 0, 0), (3, text_outline_color, 2, 2)]
    #outlines [(6, "#b59", 0, 0), (3, "#b59", 2, 2)]
    yalign 0.5


translate russian style pref_label_text:
    font "gui/font/riffic-bold.ttf"
    size 24
    color "#a200ff"
    outlines [(3, "#02a574", 0, 0), (1, "#02a574", 1, 1)]
    yalign 1.0

translate russian style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "gui/font/Halogen_0.ttf"
    outlines []


translate russian style check_button_text:
    properties gui.button_text_properties("check_button")
    font "gui/font/Halogen_0.ttf"
    outlines []