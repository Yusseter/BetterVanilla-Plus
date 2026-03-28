import json

graphical_cultures_order = [
    "chinese_building_gfx", "korean_building_gfx", "japanese_building_gfx",
    "southeast_asian_building_gfx", "austro_building_gfx",
    "western_building_gfx", "british_building_gfx", "german_building_gfx",
    "goidelic_building_gfx", "celtic_building_gfx", "vlach_building_gfx",
    "magyar_building_gfx", "scandinavian_building_gfx", "saxon_building_gfx",
    "indian_building_gfx", "burman_building_gfx", "tibetan_building_gfx",
    "mena_building_gfx", "arabic_group_building_gfx", "somali_building_gfx",
    "african_building_gfx", "guinean_building_gfx", "berber_group_building_gfx",
    "berber_building_gfx", "ethiopian_building_gfx", "sahelian_building_gfx",
    "steppe_building_gfx", "turkish_building_gfx", "mediterranean_building_gfx",
    "caucasian_building_gfx", "southslavic_building_gfx", "croatian_building_gfx",
    "sicilian_building_gfx", "norse_building_gfx", "slavic_building_gfx",
    "east_slavic_building_gfx", "tundra_building_gfx", "iberian_building_gfx",
    "iranian_building_gfx", "byzantine_building_gfx"
]

graphical_region_order = [
    "graphical_western", "graphical_mediterranean", "graphical_india",
    "graphical_burma", "graphical_tibet", "graphical_sea",
    "graphical_mena", "graphical_steppe", "graphical_east_asia",
    "graphical_siberia", "graphical_japan", "graphical_iran",
    "graphical_qixi", "graphical_caucasus"
]

graphical_faiths_order = [
    ("generic", None),
    ("catholic", "catholic_gfx"),
    ("orthodox", "orthodox_gfx"),
    ("islamic", "islamic_gfx"),
    ("judaism", "judaism_gfx"),
    ("zoroastrian", "zoroastrian_gfx"),
    ("dharmic", "dharmic_gfx"),
    ("sinitic", "sinitic_gfx"),
    ("shinto", "shinto_gfx"),
    ("tengrism", "tengrism_gfx"),
    ("pagan", "pagan_gfx")
]

regions_with_used_asset_templates = {
    "graphical_western": {
        "british_building_gfx": ["british_building_gfx"],
        "german_building_gfx": ["german_building_gfx"],
        "scandinavian_building_gfx": ["scandinavian_building_gfx"],
        "norse_building_gfx": ["norse_building_gfx"],
        "saxon_building_gfx": ["saxon_building_gfx"],
        "southslavic_building_gfx": ["southslavic_building_gfx", "croatian_building_gfx", "mediterranean_building_gfx", "byzantine_building_gfx", "turkish_building_gfx", "caucasian_building_gfx"],
        "magyar_building_gfx": ["magyar_building_gfx", "vlach_building_gfx"],
        "goidelic_building_gfx": ["goidelic_building_gfx", "celtic_building_gfx"],
        "slavic_building_gfx": ["slavic_building_gfx", "east_slavic_building_gfx", "tundra_building_gfx", "steppe_building_gfx"],
        "western_building_gfx": ["western_building_gfx", "indian_building_gfx", "burman_building_gfx", "tibetan_building_gfx", "japanese_building_gfx", "southeast_asian_building_gfx", "austro_building_gfx", "chinese_building_gfx", "korean_building_gfx", "iberian_building_gfx", "sicilian_building_gfx", "iranian_building_gfx", "mena_building_gfx", "arabic_group_building_gfx", "somali_building_gfx", "african_building_gfx", "guinean_building_gfx", "berber_group_building_gfx", "berber_building_gfx", "ethiopian_building_gfx", "sahelian_building_gfx"],
    },
    
    "graphical_mediterranean": {
        "byzantine_building_gfx": ["byzantine_building_gfx", "caucasian_building_gfx", "turkish_building_gfx", "steppe_building_gfx", "tundra_building_gfx", "east_slavic_building_gfx", "slavic_building_gfx"],
        "southslavic_building_gfx": ["southslavic_building_gfx", "croatian_building_gfx"],
        "mediterranean_building_gfx": ["mediterranean_building_gfx", "british_building_gfx", "norse_building_gfx", "scandinavian_building_gfx", "german_building_gfx", "western_building_gfx", "vlach_building_gfx", "goidelic_building_gfx", "celtic_building_gfx", "magyar_building_gfx", "saxon_building_gfx"],
        "iberian_building_gfx": ["iberian_building_gfx", "sicilian_building_gfx", "iranian_building_gfx", "mena_building_gfx", "arabic_group_building_gfx", "somali_building_gfx", "african_building_gfx", "guinean_building_gfx", "berber_group_building_gfx", "berber_building_gfx", "ethiopian_building_gfx", "sahelian_building_gfx", "indian_building_gfx", "burman_building_gfx", "tibetan_building_gfx", "japanese_building_gfx", "southeast_asian_building_gfx", "austro_building_gfx", "chinese_building_gfx", "korean_building_gfx"]
    },
    
    "graphical_india": {
        "burman_building_gfx": ["burman_building_gfx", "southeast_asian_building_gfx", "austro_building_gfx", "japanese_building_gfx", "chinese_building_gfx", "korean_building_gfx"],
        "indian_building_gfx": ["indian_building_gfx", "tibetan_building_gfx", "western_building_gfx", "british_building_gfx", "german_building_gfx", "goidelic_building_gfx", "celtic_building_gfx", "vlach_building_gfx", "magyar_building_gfx", "scandinavian_building_gfx", "saxon_building_gfx", "mena_building_gfx", "arabic_group_building_gfx", "somali_building_gfx", "african_building_gfx", "guinean_building_gfx", "berber_group_building_gfx", "berber_building_gfx", "ethiopian_building_gfx", "sahelian_building_gfx", "steppe_building_gfx", "turkish_building_gfx", "mediterranean_building_gfx", "caucasian_building_gfx", "southslavic_building_gfx", "croatian_building_gfx", "sicilian_building_gfx", "norse_building_gfx", "slavic_building_gfx", "east_slavic_building_gfx", "tundra_building_gfx", "iberian_building_gfx", "iranian_building_gfx", "byzantine_building_gfx"]
    },
    
    "graphical_burma": {
        "indian_building_gfx": ["indian_building_gfx"],
        "southeast_asian_building_gfx": ["southeast_asian_building_gfx", "austro_building_gfx", "japanese_building_gfx", "chinese_building_gfx", "korean_building_gfx"],
        "burman_building_gfx": ["burman_building_gfx", "western_building_gfx", "british_building_gfx", "german_building_gfx", "goidelic_building_gfx", "celtic_building_gfx", "vlach_building_gfx", "magyar_building_gfx", "scandinavian_building_gfx", "saxon_building_gfx", "tibetan_building_gfx", "mena_building_gfx", "arabic_group_building_gfx", "somali_building_gfx", "african_building_gfx", "guinean_building_gfx", "berber_group_building_gfx", "berber_building_gfx", "ethiopian_building_gfx", "sahelian_building_gfx", "steppe_building_gfx", "turkish_building_gfx", "mediterranean_building_gfx", "caucasian_building_gfx", "southslavic_building_gfx", "croatian_building_gfx", "sicilian_building_gfx", "norse_building_gfx", "slavic_building_gfx", "east_slavic_building_gfx", "tundra_building_gfx", "iberian_building_gfx", "iranian_building_gfx", "byzantine_building_gfx"]
    },
    
    "graphical_tibet": {
        "tibetan_building_gfx": ["tibetan_building_gfx", "burman_building_gfx", "southeast_asian_building_gfx", "austro_building_gfx", "japanese_building_gfx", "chinese_building_gfx", "korean_building_gfx", "western_building_gfx", "british_building_gfx", "german_building_gfx", "goidelic_building_gfx", "celtic_building_gfx", "vlach_building_gfx", "magyar_building_gfx", "scandinavian_building_gfx", "saxon_building_gfx", "indian_building_gfx", "mena_building_gfx", "arabic_group_building_gfx", "somali_building_gfx", "african_building_gfx", "guinean_building_gfx", "berber_group_building_gfx", "berber_building_gfx", "ethiopian_building_gfx", "sahelian_building_gfx", "mediterranean_building_gfx", "caucasian_building_gfx", "southslavic_building_gfx", "croatian_building_gfx", "sicilian_building_gfx", "norse_building_gfx", "slavic_building_gfx", "east_slavic_building_gfx", "iberian_building_gfx", "iranian_building_gfx", "byzantine_building_gfx", "steppe_building_gfx", "turkish_building_gfx", "tundra_building_gfx"]
    },
    
    "graphical_sea": {
        "burman_building_gfx": ["burman_building_gfx", "indian_building_gfx", "tibetan_building_gfx"],
        "chinese_building_gfx": ["chinese_building_gfx", "korean_building_gfx", "japanese_building_gfx", "steppe_building_gfx", "tundra_building_gfx"],
        "southeast_asian_building_gfx": ["southeast_asian_building_gfx", "austro_building_gfx", "western_building_gfx", "british_building_gfx", "german_building_gfx", "goidelic_building_gfx", "celtic_building_gfx", "vlach_building_gfx", "magyar_building_gfx", "scandinavian_building_gfx", "saxon_building_gfx", "mena_building_gfx", "arabic_group_building_gfx", "somali_building_gfx", "african_building_gfx", "guinean_building_gfx", "berber_group_building_gfx", "berber_building_gfx", "ethiopian_building_gfx", "sahelian_building_gfx", "turkish_building_gfx", "mediterranean_building_gfx", "caucasian_building_gfx", "southslavic_building_gfx", "croatian_building_gfx", "sicilian_building_gfx", "norse_building_gfx", "slavic_building_gfx", "east_slavic_building_gfx", "iberian_building_gfx", "iranian_building_gfx", "byzantine_building_gfx"]
    },
    
    "graphical_mena": {
		"somali_building_gfx": ["somali_building_gfx"],
		"ethiopian_building_gfx": ["ethiopian_building_gfx"],
		"sahelian_building_gfx": ["sahelian_building_gfx"],
		"african_building_gfx": ["african_building_gfx", "guinean_building_gfx"],
		"berber_building_gfx": ["berber_building_gfx", "berber_group_building_gfx", "sicilian_building_gfx", "iberian_building_gfx"],
        "iranian_building_gfx": ["iranian_building_gfx", "caucasian_building_gfx", "turkish_building_gfx", "byzantine_building_gfx", "mediterranean_building_gfx", "burman_building_gfx", "indian_building_gfx", "tibetan_building_gfx", "steppe_building_gfx", "tundra_building_gfx", "chinese_building_gfx", "korean_building_gfx", "japanese_building_gfx", "southeast_asian_building_gfx", "austro_building_gfx"],
        "mena_building_gfx": ["mena_building_gfx", "arabic_group_building_gfx", "western_building_gfx", "british_building_gfx", "german_building_gfx", "goidelic_building_gfx", "celtic_building_gfx", "vlach_building_gfx", "magyar_building_gfx", "scandinavian_building_gfx", "saxon_building_gfx", "southslavic_building_gfx", "croatian_building_gfx", "norse_building_gfx", "slavic_building_gfx", "east_slavic_building_gfx"]
    },
    
    "graphical_steppe": {
        "iranian_building_gfx": ["iranian_building_gfx", "indian_building_gfx", "mena_building_gfx", "arabic_group_building_gfx", "somali_building_gfx", "african_building_gfx", "guinean_building_gfx", "berber_group_building_gfx", "berber_building_gfx", "ethiopian_building_gfx", "sahelian_building_gfx", "mediterranean_building_gfx", "caucasian_building_gfx", "sicilian_building_gfx", "byzantine_building_gfx", "iberian_building_gfx", "turkish_building_gfx"],
        "chinese_building_gfx": ["chinese_building_gfx", "korean_building_gfx", "japanese_building_gfx", "southeast_asian_building_gfx", "austro_building_gfx", "burman_building_gfx"],
        "magyar_building_gfx": ["magyar_building_gfx", "vlach_building_gfx", "southslavic_building_gfx", "croatian_building_gfx"],
        "slavic_building_gfx": ["slavic_building_gfx", "east_slavic_building_gfx", "western_building_gfx", "british_building_gfx", "german_building_gfx", "goidelic_building_gfx", "celtic_building_gfx", "scandinavian_building_gfx", "saxon_building_gfx", "norse_building_gfx"],
        "steppe_building_gfx": ["tibetan_building_gfx", "steppe_building_gfx", "tundra_building_gfx"]
    },
    
    "graphical_east_asia": {
		"japanese_building_gfx": ["japanese_building_gfx"],
        "southeast_asian_building_gfx": ["southeast_asian_building_gfx", "austro_building_gfx", "indian_building_gfx", "burman_building_gfx", "tibetan_building_gfx"],
		"chinese_building_gfx": ["chinese_building_gfx", "korean_building_gfx", "steppe_building_gfx", "turkish_building_gfx", "mediterranean_building_gfx", "caucasian_building_gfx", "southslavic_building_gfx", "croatian_building_gfx", "sicilian_building_gfx", "norse_building_gfx", "slavic_building_gfx", "east_slavic_building_gfx", "tundra_building_gfx", "iberian_building_gfx", "iranian_building_gfx", "byzantine_building_gfx", "mena_building_gfx", "arabic_group_building_gfx", "somali_building_gfx", "african_building_gfx", "guinean_building_gfx", "berber_group_building_gfx", "berber_building_gfx", "ethiopian_building_gfx", "sahelian_building_gfx", "western_building_gfx", "british_building_gfx", "german_building_gfx", "goidelic_building_gfx", "celtic_building_gfx", "vlach_building_gfx", "magyar_building_gfx", "scandinavian_building_gfx", "saxon_building_gfx"]
	},
    
    "graphical_siberia": {
		"norse_building_gfx": ["norse_building_gfx"],
        "scandinavian_building_gfx": ["scandinavian_building_gfx", "western_building_gfx", "british_building_gfx", "german_building_gfx", "goidelic_building_gfx", "celtic_building_gfx", "saxon_building_gfx"],
        "slavic_building_gfx": ["slavic_building_gfx", "east_slavic_building_gfx", "vlach_building_gfx", "magyar_building_gfx"],
        "tundra_building_gfx": ["tundra_building_gfx", "steppe_building_gfx", "japanese_building_gfx", "southeast_asian_building_gfx", "austro_building_gfx", "indian_building_gfx", "burman_building_gfx", "tibetan_building_gfx", "mena_building_gfx", "arabic_group_building_gfx", "somali_building_gfx", "african_building_gfx", "guinean_building_gfx", "berber_group_building_gfx", "berber_building_gfx", "ethiopian_building_gfx", "sahelian_building_gfx", "turkish_building_gfx", "mediterranean_building_gfx", "caucasian_building_gfx", "southslavic_building_gfx", "croatian_building_gfx", "sicilian_building_gfx", "iberian_building_gfx", "iranian_building_gfx", "byzantine_building_gfx", "chinese_building_gfx", "korean_building_gfx"]
    },
    
    "graphical_japan": {
        "chinese_building_gfx": ["chinese_building_gfx", "korean_building_gfx", "steppe_building_gfx", "southeast_asian_building_gfx", "austro_building_gfx", "indian_building_gfx", "burman_building_gfx", "tibetan_building_gfx"],
        "japanese_building_gfx": ["japanese_building_gfx", "tundra_building_gfx", "turkish_building_gfx", "mediterranean_building_gfx", "caucasian_building_gfx", "southslavic_building_gfx", "croatian_building_gfx", "sicilian_building_gfx", "norse_building_gfx", "slavic_building_gfx", "east_slavic_building_gfx", "iberian_building_gfx", "iranian_building_gfx", "byzantine_building_gfx", "mena_building_gfx", "arabic_group_building_gfx", "somali_building_gfx", "african_building_gfx", "guinean_building_gfx", "berber_group_building_gfx", "berber_building_gfx", "ethiopian_building_gfx", "sahelian_building_gfx", "western_building_gfx", "british_building_gfx", "german_building_gfx", "goidelic_building_gfx", "celtic_building_gfx", "vlach_building_gfx", "magyar_building_gfx", "scandinavian_building_gfx", "saxon_building_gfx"]
    },
    
    "graphical_iran": {
        "iranian_building_gfx": ["iranian_building_gfx", "mena_building_gfx", "arabic_group_building_gfx", "turkish_building_gfx", "byzantine_building_gfx", "mediterranean_building_gfx", "somali_building_gfx", "ethiopian_building_gfx", "sahelian_building_gfx", "caucasian_building_gfx", "african_building_gfx", "guinean_building_gfx", "berber_group_building_gfx", "berber_building_gfx", "sicilian_building_gfx", "iberian_building_gfx", "burman_building_gfx", "indian_building_gfx", "tibetan_building_gfx", "steppe_building_gfx", "tundra_building_gfx", "chinese_building_gfx", "korean_building_gfx", "japanese_building_gfx", "southeast_asian_building_gfx", "austro_building_gfx", "western_building_gfx", "british_building_gfx", "german_building_gfx", "goidelic_building_gfx", "celtic_building_gfx", "vlach_building_gfx", "magyar_building_gfx", "scandinavian_building_gfx", "saxon_building_gfx", "southslavic_building_gfx", "croatian_building_gfx", "norse_building_gfx", "slavic_building_gfx", "east_slavic_building_gfx"]
    },
    
    "graphical_qixi": {
        "iranian_building_gfx": ["iranian_building_gfx", "steppe_building_gfx", "tundra_building_gfx", "indian_building_gfx", "tibetan_building_gfx", "mena_building_gfx", "arabic_group_building_gfx", "turkish_building_gfx", "mediterranean_building_gfx", "caucasian_building_gfx", "sicilian_building_gfx", "iberian_building_gfx", "byzantine_building_gfx", "western_building_gfx", "british_building_gfx", "german_building_gfx", "goidelic_building_gfx", "celtic_building_gfx", "vlach_building_gfx", "magyar_building_gfx", "scandinavian_building_gfx", "saxon_building_gfx", "somali_building_gfx", "african_building_gfx", "guinean_building_gfx", "berber_group_building_gfx", "berber_building_gfx", "ethiopian_building_gfx", "sahelian_building_gfx", "southslavic_building_gfx", "croatian_building_gfx", "norse_building_gfx", "slavic_building_gfx", "east_slavic_building_gfx"],
        "chinese_building_gfx": ["chinese_building_gfx", "korean_building_gfx", "japanese_building_gfx", "southeast_asian_building_gfx", "austro_building_gfx", "burman_building_gfx"]
    },
    
    "graphical_caucasus": {
        "caucasian_building_gfx": ["caucasian_building_gfx", "byzantine_building_gfx", "turkish_building_gfx", "steppe_building_gfx", "tundra_building_gfx", "east_slavic_building_gfx", "slavic_building_gfx", "southslavic_building_gfx", "croatian_building_gfx", "iberian_building_gfx", "sicilian_building_gfx", "iranian_building_gfx", "mena_building_gfx", "arabic_group_building_gfx", "somali_building_gfx", "african_building_gfx", "guinean_building_gfx", "berber_group_building_gfx", "berber_building_gfx", "ethiopian_building_gfx", "sahelian_building_gfx", "indian_building_gfx", "burman_building_gfx", "tibetan_building_gfx", "japanese_building_gfx", "southeast_asian_building_gfx", "austro_building_gfx", "chinese_building_gfx", "korean_building_gfx", "mediterranean_building_gfx", "british_building_gfx", "norse_building_gfx", "scandinavian_building_gfx", "german_building_gfx", "western_building_gfx", "vlach_building_gfx", "goidelic_building_gfx", "celtic_building_gfx", "magyar_building_gfx", "saxon_building_gfx"]
    }
}

region_based_asset_count = sum(
    len(graphical_region_order)
    for graphical_region_order in regions_with_used_asset_templates.values()
)

max_building_level = 4
asset_number = region_based_asset_count*len(graphical_faiths_order)
asset_number_building = asset_number*max_building_level

print("graphical_cultures count:", len(graphical_cultures_order))
print("graphical_region count:", len(graphical_region_order))
print("graphical_faiths count:", len(graphical_faiths_order))
print("Region based templates count:", region_based_asset_count)
print("Building levels count:", max_building_level)
print("Expected assets per temple tier:", asset_number)
print("Expected assets per temple tier for every building levels:", asset_number_building)
