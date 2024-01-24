import sender_stand_request



def get_trackid():
    res = sender_stand_request.create_order()
    if res.ok:
        return res.json()['track']
    else:
        return ''


def test_get_order():
    trackid = get_trackid()
    res = sender_stand_request.get_order(trackid)
    assert res.status_code == 200



##Окулов Егор 12-ая когорта - Финальный проект. Инженер по тестированию плюс.