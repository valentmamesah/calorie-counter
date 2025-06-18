
def hitung_total_kalori(detected_items, kalori_dict):
    rincian = {}
    total_kalori = 0
    for item in detected_items:
        kalori = kalori_dict.get(item, 0)
        rincian[item] = rincian.get(item, 0) + kalori
        total_kalori += kalori
    return total_kalori, rincian
