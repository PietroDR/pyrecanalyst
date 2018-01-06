# coding: utf-8

import re


class MapName(object):
    """
    Extracts the map name from the Objectives tab of a recorded game. That's the
    only place where the name of a custom random map is stored.
    """
    def __init__(self, rec):
        # Recorded game file to use.
        self.rec = rec

        # Possible formats for map type lines in the Objectives tab.
        # The Map Type strings used in the Objectives message tab are stored in
        # string id 9654. self array was generated using:
        # grep "9654" "SteamApps/common/Age2HD/resources/*/strings/key-value/key-value-strings-utf8.txt"
        #
        # HD Edition uses UTF-8, but older versions used localization-specific code pages.
        # Code page information for zh, jp and ko was taken from:
        # https:#msdn.microsoft.com/en-us/library/cc194886.aspx
        self.map_type_regexes = {
            'br': 'Tipo de Mapa: (.*)',
            'de': 'Kartentyp: (.*)',
            'en': 'Map Type: (.*)',
            'es': 'Tipo de mapa: (.*)',
            'fr': 'Type de carte : (.*)',
            'it': 'Tipo di mappa: (.*)',
            'jp': 'マップの種類: (.*)'.decode("utf-8").encode("cp932"),
            'jp_utf8': u'マップの種類: (.*)',
            'ko': '지도 종류: (.*)'.decode("utf-8").encode("cp949"),
            'ko_utf8': u'지도 종류: (.*)',
            'nl': 'Kaarttype: (.*)'.decode("utf-8").encode("windows-1251"),
            'nl_utf8': 'Kaarttype: (.*)',
            'ru': 'Тип карты: (.*)'.decode("utf-8").encode("cp936"),
            'ru_utf8': u'Тип карты: (.*)',
            'zh': '地图类型: (.*)'.decode("utf-8").encode("cp936"),
            'zh_utf8': u'地图类型: (.*)'
        }

    def run(self):
        """Run the processor."""
        header = self.rec.header()
        messages = header.messages
        instructions = messages["instructions"]
        lines = instructions.split('\n')
        for line in lines:
            # We don't know what language the game was played in, so we try
            # every language we know.
            for lang, rx in self.map_type_regexes.iteritems():
                matches = re.match(rx, line)
                if matches:
                    return matches.group(1)
