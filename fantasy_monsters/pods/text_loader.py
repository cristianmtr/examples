__copyright__ = "Copyright (c) 2020 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

from typing import Dict

from jina.executors.crafters import BaseCrafter


class TextExtractor(BaseCrafter):
    def craft(self, text: str, *args, **kwargs) -> Dict:
        monster_name, monster_description = text.split('[SEP]')
        return dict(weight=1., text=monster_description, meta_info=monster_name.encode('utf8'))
