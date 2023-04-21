import pytest
import responses
from website.views import format_number

def test_home_title(client):
    response = client.get('/')
    
    assert "<title>Strona główna</title>" in response.data.decode('utf-8')

@responses.activate
def test_procurment_first_page(client):
    responses.add(
        responses.GET,
        "https://tenders.guru/api/pl/tenders",
        json={"page_count":5822,"page_number":1,"page_size":100,"total":582145,"data":[{"id":"585088","date":"2022-11-23","deadline_date":"2022-12-08","deadline_length_days":"15","deadline_length_hours":"362","title":"Dostawa sprz\u0119tu medycznego dla potrzeb Uzdrowiska Gocza\u0142kowice - Zdr\u00f3j Sp. z o.o. z siedzib\u0105 w Gocza\u0142kowicach - Zdroju","category":"supplies","description":"W zakres zam\u00f3wienia wchodzi kolumna wolnostoj\u0105ca do progresywnego treningu oporowego dla rehabilitacji pourazowej \u2013 1 szt.","sid":"info:166659","awarded_value":"125915.52","awarded_currency":"PLN","awarded_value_eur":"26679.84","purchaser":{"id":"29445","sid":None,"name":None},"type":{"id":"art-275-pkt-2-ustawy","name":"art. 275 pkt 2 ustawy","slug":"art-275-pkt-2-ustawy"},"indicators":["low_value_awarded","high_value_awarded"],"awarded":[{"date":"2023-01-26","value_for_two":70356,"value_for_two_eur":14907.51,"suppliers":[{"name":"HAS-MED Sp. z o.o.","id":1325,"slug":"has-med-sp-z-o-o"}],"value_min":"116482.80","value_for_three":80540.4,"offers_count_status":"contains_only_one","value_for_one_eur":14907.51,"count":"5","value_for_one":70356,"value_for_three_eur":17065.45,"suppliers_id":"1325","value_eur":24681.17,"value_max":"136441.20","offers_count":[1,3,4],"suppliers_name":"HAS-MED Sp. z o.o.","value":"116482.80","value_estimated":"119209.26","offers_count_data":{"1":{"value_eur":14907.51,"count":"2","value":"70356.00"},"3":{"value_eur":2157.94,"count":"2","value":"10184.40"},"4":{"value_eur":7615.72,"count":"1","value":"35942.40"}}},{"date":"2023-01-26","value_for_two":503.28,"value_for_two_eur":106.64,"suppliers":[{"name":"ZARYS International Group Sp. z o.o. Sp. K.","id":63,"slug":"zarys-international-group-sp-z-o-o-sp-k"}],"value_min":"503.28","value_for_three":503.28,"offers_count_status":"only_one","value_for_one_eur":106.64,"count":"1","value_for_one":503.28,"value_for_three_eur":106.64,"suppliers_id":"63","value_eur":106.64,"value_max":"503.28","offers_count":[1],"suppliers_name":"ZARYS International Group Sp. z o.o. Sp. K.","value":"503.28","value_estimated":"1562.00","offers_count_data":{"1":{"value_eur":106.64,"count":"1","value":"503.28"}}},{"date":"2023-01-26","value_for_two":8929.44,"value_for_two_eur":1892.03,"suppliers":[{"name":"F.H.U. Euro-Medical Maciej \u015awida","id":8480,"slug":"f-h-u-euro-medical-maciej-swida"}],"value_min":"8929.44","value_for_three":8929.44,"value_for_one_eur":0,"count":"1","value_for_one":0,"value_for_three_eur":1892.03,"suppliers_id":"8480","value_eur":1892.03,"value_max":"9072.00","offers_count":[2],"suppliers_name":"F.H.U. Euro-Medical Maciej \u015awida","value":"8929.44","value_estimated":"8635.00","offers_count_data":{"2":{"value_eur":1892.03,"count":"1","value":"8929.44"}}}]}]},
        status=200
    )
    
    response = client.get('/dane-o-zamowieniach')

    assert "<h3>Strona 1</h3>" in response.data.decode('utf-8')

@responses.activate    
def test_procurment_fifth(client):
    responses.add(
        responses.GET,
        "https://tenders.guru/api/pl/tenders",
        json={"page_count":5822,"page_number":5,"page_size":100,"total":582145,"data":[{"id":"585088","date":"2022-11-23","deadline_date":"2022-12-08","deadline_length_days":"15","deadline_length_hours":"362","title":"Dostawa sprz\u0119tu medycznego dla potrzeb Uzdrowiska Gocza\u0142kowice - Zdr\u00f3j Sp. z o.o. z siedzib\u0105 w Gocza\u0142kowicach - Zdroju","category":"supplies","description":"W zakres zam\u00f3wienia wchodzi kolumna wolnostoj\u0105ca do progresywnego treningu oporowego dla rehabilitacji pourazowej \u2013 1 szt.","sid":"info:166659","awarded_value":"125915.52","awarded_currency":"PLN","awarded_value_eur":"26679.84","purchaser":{"id":"29445","sid":None,"name":None},"type":{"id":"art-275-pkt-2-ustawy","name":"art. 275 pkt 2 ustawy","slug":"art-275-pkt-2-ustawy"},"indicators":["low_value_awarded","high_value_awarded"],"awarded":[{"date":"2023-01-26","value_for_two":70356,"value_for_two_eur":14907.51,"suppliers":[{"name":"HAS-MED Sp. z o.o.","id":1325,"slug":"has-med-sp-z-o-o"}],"value_min":"116482.80","value_for_three":80540.4,"offers_count_status":"contains_only_one","value_for_one_eur":14907.51,"count":"5","value_for_one":70356,"value_for_three_eur":17065.45,"suppliers_id":"1325","value_eur":24681.17,"value_max":"136441.20","offers_count":[1,3,4],"suppliers_name":"HAS-MED Sp. z o.o.","value":"116482.80","value_estimated":"119209.26","offers_count_data":{"1":{"value_eur":14907.51,"count":"2","value":"70356.00"},"3":{"value_eur":2157.94,"count":"2","value":"10184.40"},"4":{"value_eur":7615.72,"count":"1","value":"35942.40"}}},{"date":"2023-01-26","value_for_two":503.28,"value_for_two_eur":106.64,"suppliers":[{"name":"ZARYS International Group Sp. z o.o. Sp. K.","id":63,"slug":"zarys-international-group-sp-z-o-o-sp-k"}],"value_min":"503.28","value_for_three":503.28,"offers_count_status":"only_one","value_for_one_eur":106.64,"count":"1","value_for_one":503.28,"value_for_three_eur":106.64,"suppliers_id":"63","value_eur":106.64,"value_max":"503.28","offers_count":[1],"suppliers_name":"ZARYS International Group Sp. z o.o. Sp. K.","value":"503.28","value_estimated":"1562.00","offers_count_data":{"1":{"value_eur":106.64,"count":"1","value":"503.28"}}},{"date":"2023-01-26","value_for_two":8929.44,"value_for_two_eur":1892.03,"suppliers":[{"name":"F.H.U. Euro-Medical Maciej \u015awida","id":8480,"slug":"f-h-u-euro-medical-maciej-swida"}],"value_min":"8929.44","value_for_three":8929.44,"value_for_one_eur":0,"count":"1","value_for_one":0,"value_for_three_eur":1892.03,"suppliers_id":"8480","value_eur":1892.03,"value_max":"9072.00","offers_count":[2],"suppliers_name":"F.H.U. Euro-Medical Maciej \u015awida","value":"8929.44","value_estimated":"8635.00","offers_count_data":{"2":{"value_eur":1892.03,"count":"1","value":"8929.44"}}}]}]},
        status=200
    )
    response = client.post("/dane-o-zamowieniach", data={"page": "5"})
    
    assert "<h3>Strona 5</h3>" in response.data.decode('utf-8')
    
@responses.activate
def test_details(client):
    responses.add(
        responses.GET,
        "https://tenders.guru/api/pl/tenders/583899",
        json={"id":"583899","date":"2022-11-16","deadline_date":"2022-11-24","deadline_length_days":"8","deadline_length_hours":"196","title":"Zakup wyposa\u017cenia do Centrum Opieku\u0144czo Mieszkalnego w K\u0119trzynie przy ul. Sikorskiego 46 (3).","category":"supplies","description":"Dostawa wyposa\u017cenia kuchennego i sprz\u0119tu AGD.Zam\u00f3wienie obejmuje m.in.: talerze, kubki, szklanki, patelnie, sztu\u0107ce, garnki, akcesoria kuchenne, mikrofal\u00f3wki, termosy stalowe, podgrzewacze, kocio\u0142ki elektryczne, lod\u00f3wka, czajniki, itp.Szczeg\u00f3\u0142owy opis zam\u00f3wienia znajduje si\u0119 w Za\u0142\u0105czniku nr 1a dla Cz\u0119\u015bci 1.","sid":"info:162944","awarded_value":"118796.66","awarded_currency":"PLN","awarded_value_eur":"25272.55","purchaser":{"id":"24952","sid":None,"name":None},"type":{"id":"art-275-pkt-1-ustawy","name":"art. 275 pkt 1 ustawy","slug":"art-275-pkt-1-ustawy"},"notices":[{"id":"162944","sid":"2022BZP 0044045301","date":"2022-11-16","type":{},"src_id":None,"src_url":None,"data":{"id":"162944","sid":"2022BZP 0044045301","date":"2022-11-16","type":{"id":1,"slug":"info","name":"Zamiar udzielenia zam\u00f3wienia","name_en":"Intention to award the contract"}},"sections":[]},{"id":"162945","sid":"2023BZP 0003906701","date":"2023-01-17","type":{},"src_id":None,"src_url":None,"data":{"id":"162945","sid":"2023BZP 0003906701","date":"2023-01-17","type":{"id":2,"slug":"award","name":"Udzielenie zam\u00f3wienia","name_en":"Award of the contract"}},"sections":[]}],"awarded":[{"date":"2023-01-22","suppliers_id":"17403","count":"1","value":"102039.57","value_min":"102039.57","value_max":"198276.00","value_estimated":"105691.06","suppliers_name":"DRZEWIARZ BIS SP. Z O.O.","suppliers":[{"id":17403,"slug":"drzewiarz-bis-sp-z-o-o","name":"DRZEWIARZ BIS SP. Z O.O."}],"value_for_one":0,"value_for_two":0,"value_for_three":0,"offers_count_data":{"7":{"count":"1","value":"102039.57","value_eur":21664.45}},"offers_count":[7],"offers_declined":[3],"value_eur":21664.45,"value_for_one_eur":0,"value_for_two_eur":0,"value_for_three_eur":0},{"date":"2022-12-22","suppliers_id":"2540","count":"1","value":"16757.09","value_min":"16757.09","value_max":"34988.58","value_estimated":"32520.33","suppliers_name":"PH ENERGIA S.C.","suppliers":[{"id":2540,"slug":"ph-energia-s-c","name":"PH ENERGIA S.C."}],"value_for_one":0,"value_for_two":0,"value_for_three":0,"offers_count_data":{"7":{"count":"1","value":"16757.09","value_eur":3608.1}},"offers_count":[7],"offers_declined":[2],"value_eur":3608.1,"value_for_one_eur":0,"value_for_two_eur":0,"value_for_three_eur":0}]},
        status=200
    )
    
    responnse = client.get('/detils/583899')
    
    assert '<td class="col-sm-9 text-break">583899</td>' in responnse.data.decode('utf-8')
    
@pytest.mark.parametrize("num_string, expected_output", [
    ("10000", "10 000,00"),
    ("1756.54", "1 756,54"),
    ("34.5678", "34,57"),
])
def test_format_number(num_string, expected_output):
    assert format_number(num_str=num_string).replace('\xa0', ' ') == expected_output