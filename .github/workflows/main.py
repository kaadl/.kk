#coded by CLOVR https://t.me/CLOVRTOOLS
#لاتغير الحقوق
#لاتغير الحقوق


import os
os.system("pip install pyTelegramBotAPI requests SignerPy")

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random, string, time, requests, uuid, binascii, threading
import SignerPy

BOT_TOKEN = "8492754625:AAF2ekQG3qsKpoGS91Y60sSfNr-TXkLq7Fc" #ضع توكن بوتك هنا
YOUTUBE_LINK = "https://www.youtube.com/channel/UCj7TtZr6-7ViVvzVCt0U5SA"

bot = telebot.TeleBot(BOT_TOKEN)

user_sessions = {}   # للتحكم في بدء/إيقاف الفحص
user_verified = {}   # لتتبع الاشتراك الفعلي

# ---------------- توليد أسماء -----------------
def generate_username(length_type):
    if length_type == "2":
        return ''.join(random.choices(string.ascii_lowercase, k=2))
    elif length_type == "3":
        return ''.join(random.choices(string.ascii_lowercase, k=3))
    elif length_type == "4":
        return ''.join(random.choices(string.ascii_lowercase, k=4))
    elif length_type == "semi4":  # شبه رباعي محدد 5 أحرف
        total_length = 5
        separator = random.choice(["_", "."])
        part1_length = total_length - 1
        part1 = ''.join(random.choices(string.ascii_lowercase, k=part1_length))
        part2 = random.choice(string.ascii_lowercase + "")
        return f"{part1}{separator}{part2}"

# ---------------- توليد بارامترز وكوكيز عشوائية -----------------
def generate_random_params():
    import secrets
    iid = str(random.randint(10**18, 10**19-1))
    device_id = str(random.randint(10**18, 10**19-1))
    openudid = binascii.hexlify(uuid.uuid4().bytes).decode()
    cdid = str(uuid.uuid4())
    rticket = str(int(time.time() * 1000))
    csrf = secrets.token_hex(16)
    cookies = {
    "passport_csrf_token": csrf,
    "passport_csrf_token_default": csrf,
    "store-idc": "alisg",
    "tt-target-idc": "alisg",
    "d_ticket": "a277b7920c033a246094bad8d12601294e801",
    "multi_sids": "7489305185481032722%3A63c7bc83f68b3cadfac1296bd062d3f3",
    "cmpl_token": "AgQQAPO_F-RPsLfRtcVTJF0r8u-D5cRJ_5IhYN3Law",
    "sid_guard": "63c7bc83f68b3cadfac1296bd062d3f3|1755027797|15552000|Sun, 08-Feb-2026 19:43:17 GMT",
    "uid_tt": "1853441515214c866259320d74a130bcfd6a41db7228bf83465faef158877a8d",
    "uid_tt_ss": "1853441515214c866259320d74a130bcfd6a41db7228bf83465faef158877a8d",
    "sid_tt": "63c7bc83f68b3cadfac1296bd062d3f3",
    "sessionid": "63c7bc83f68b3cadfac1296bd062d3f3",
    "sessionid_ss": "63c7bc83f68b3cadfac1296bd062d3f3",
    "store-country-code": "sa",
    "store-country-code-src": "uid",
    "tt_ticket_guard_has_set_public_key": "1",
    "install_id": "7533989803811227408",
    "ttreq": "1$ace788c95ce3e52f3b2662b04f5a6a397967e973",
    "store-country-sign": "MEIEDKHo20zJwPs4qJlLHgQgzE_e9myznlV6uYjC93B8dYZ4ydh17IcEEdUcjNXAJvEEELoqj04eTYODXoUPSVoMwP0",
    "odin_tt": "f3494e6288aa70a56f338594e2aa5733ea1110092c0dedb0fbec8add09789e9ba93aba37e426e8af5ead0e8b5f1c1e68144fec6673b4778ebf3cd913a8ded816cd4251337f10e4a958f1ad12581387a0",
    "msToken": "o25n5w8_JpwKQ3D-8AhopwpEtA82nfNULSoMJU9f_r40j4-mU8ago0Lp6UiPeGETYC1dNjLEIBL-D1ilvpLnqTGFuGfCNuXBNNh93YJfwwqV1Z5R4l7OFibZYQ=="
}
 

    params = {
    "unique_id": "",  # اسم المستخدم المطلوب التحقق منه
    "device_platform": "android",
    "os": "android",
    "ssmix": "a",
    "_rticket": str(int(time.time() * 1000)),  # ملي ثانية
    "cdid": str(uuid.uuid4()),
    "channel": "googleplay",
    "aid": "1233",
    "app_name": "musical_ly",
    "version_code": "370805",
    "version_name": "37.8.5",
    "manifest_version_code": "2023708050",
    "update_version_code": "2023708050",
    "ab_version": "37.8.5",
    "resolution": "1600*900",
    "dpi": "240",
    "device_type": "NE2211",
    "device_brand": "OnePlus",
    "language": "ar",
    "os_api": "28",
    "os_version": "9",
    "ac": "wifi",
    "is_pad": "0",
    "current_region": "JP",
    "app_type": "normal",
    "sys_region": "EG",
    "last_install_time": "1755004070",
    "mcc_mnc": "44020",
    "timezone_name": "Asia/Riyadh",
    "carrier_region_v2": "440",
    "residence": "JP",
    "app_language": "ar",
    "carrier_region": "JP",
    "timezone_offset": "10800",
    "host_abi": "arm64-v8a",
    "locale": "ar",
    "ac2": "wifi",
    "uoo": "0",
    "op_region": "JP",
    "build_number": "37.8.5",
    "region": "EG",
    "ts": str(int(time.time())),  # وقت Unix بالثواني
    "iid": "7533989803811227408",  # نفس الكوكيز
    "device_id": "7533988734871979536",  # نفس الكوكيز
    "openudid": "b2e93cc8fb3bb13c",  # ثابت
    "app_version": "37.8.5"
}

    return cookies, params

# ---------------- فحص اسم مستخدم -----------------
def check_username(username):
    url = "https://api22-normal-c-alisg.tiktokv.com/aweme/v1/unique/id/check/"
    cookies, params = generate_random_params()
    params["unique_id"] = username
    try:
        m = SignerPy.sign(params=params, cookie=cookies)
        headers = {
            'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; ar_EG; NE2211; Build/SKQ1.220617.001;tt-ok/3.12.13.16)",
            'Accept-Encoding': "gzip",
            'rpc-persist-pyxis-policy-v-tnc': "1",
            'x-tt-pba-enable': "1",
            'x-bd-kmsv': "0",
            'x-tt-dm-status': "login=1;ct=1;rt=1",
            'x-ss-req-ticket': m['x-ss-req-ticket'],
            'x-bd-client-key': "#sCiPlt4HRVuetlku1tNQw6ivQh4xJTdtwM2F6OWG5qyop8BNpl6Q84rjnEaPQFZ+5X+9816JDYHcHHQ5",
            'sdk-version': "2",
            'passport-sdk-version': "6031990",
            'oec-vc-sdk-version': "3.0.5.i18n",
            'x-vc-bdturing-sdk-version': "2.3.8.i18n",
            'x-tt-request-tag': "n=0;nr=011;bg=0",
            'x-tt-store-region': "sa",
            'x-tt-store-region-src': "uid",
            'x-ladon': m['x-ladon'],
            'x-khronos': m['x-khronos'],
            'x-argus': m['x-argus'],
            'x-gorgon': m['x-gorgon'],
        }

        response = requests.get(url, params=params, cookies=cookies, headers=headers, timeout=10)

        # نحاول تحويل الرد إلى JSON
        try:
            data = response.json()
        except:
            data = {"error": response.text}  # إذا لم يكن JSON نضعه في القاموس
       
        print(data)  # طباعة الرد دائماً
        return data.get("is_valid", False)

    except Exception as e:
        print(f"❌ خطأ أثناء التحقق من {username}: {e}")
        return False



# ---------------- بدء الفحص -----------------
def start_checking(chat_id, length_type):
    user_sessions[chat_id] = True
    while user_sessions.get(chat_id):
        username = generate_username(length_type)
        is_valid = check_username(username)
        if is_valid:
            bot.send_message(chat_id, f"""✅ {username} هذا اليوزر متاح
                             
                             
                             by CLOVR @https://t.me/CLOVRTOOLS""")
        else:
            bot.send_message(chat_id, f"❌ {username}")
        time.sleep(1)

# ---------------- الأزرار -----------------
def get_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton("ثنائي", callback_data="2"),
        InlineKeyboardButton("ثلاثي", callback_data="3"),
        InlineKeyboardButton("رباعي", callback_data="4"),
        InlineKeyboardButton("شبه رباعي", callback_data="semi4")
    )
    keyboard.row(
        InlineKeyboardButton("توقف", callback_data="stop")
    )
    return keyboard


# ---------------- أوامر البوت -----------------
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "أهلاً! اختر نوع الاسم للفحص:",
        reply_markup=get_keyboard()
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id = call.message.chat.id

    if call.data == "stop":
        user_sessions[chat_id] = False
        bot.answer_callback_query(call.id, "تم إيقاف الفحص")
        bot.send_message(chat_id, "تم إيقاف الفحص ✅")
    else:
        bot.answer_callback_query(call.id, f"بدء فحص الأسماء {call.data}")
        threading.Thread(
            target=start_checking,
            args=(chat_id, call.data),
            daemon=True
        ).start()

bot.infinity_polling()
