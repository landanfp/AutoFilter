class script(object):
    START_TXT = """<b>👋 سلام {} |🥰😉\n\n<u>• به ربات ریلز دانلودر خوش آمدید ❤️</u>\n\n• لینک اینستاگرامی موردنظرتان را ارسال کنید.\nتا فایلشو براتون بفرستم. 😊\n\n🖍️ سازنده ربات : <a href='t.me/Farshidband'>FﾑRSみɨの-BﾑŊの</a></b> """

    GSTART_TXT = """<b>ʜᴇʏ {},\n\nɪ ᴀᴍ ᴛʜᴇ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘʀᴇᴍɪᴜᴍ ꜰᴇᴀᴛᴜʀᴇꜱ.\n\nᴍᴀɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/cryxelys">ᴍɪᴋᴇʏ</a></b>"""
    
    HELP_TXT = """<b>ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟʟᴏᴡ ᴛᴏ ɢᴇᴛ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ᴀʙᴏᴜᴛ sᴘᴇᴄɪғɪᴄs ᴄᴏᴍᴍᴀɴᴅ!</b>"""

    ABOUT_TXT = """
<b>❍ ᴍʏ ɴᴀᴍᴇ : <a href="https://t.me/Lucy_Filter_bot">ʟᴜᴄʏ ʙᴏᴛ</a>
❍ ᴄʀᴇᴀᴛᴏʀ : <a href="https://t.me/veldxd">мɪкєʏ</a>
❍ ʟɪʙʀᴀʀʏ : <a href="https://pyrogram.org/">ᴘʏʀᴏɢʀᴀᴍ</a>
❍ ʟᴀɴɢᴜᴀɢᴇ : <a href="https://www.python.org/">ᴘʏᴛʜᴏɴ</a>
❍ ᴅᴀᴛᴀʙᴀꜱᴇ : <a href="https://www.mongodb.com/">ᴍᴏɴɢᴏ ᴅʙ</a>
❍ ʜᴏꜱᴛᴇᴅ ᴏɴ : <a href="https://t.me/codeflix_bots">ᴠᴘs</a>
❍ ʙᴜɪʟᴅ ꜱᴛᴀᴛᴜꜱ : ᴠ4.4.1 [ᴀᴅᴠᴀɴᴄᴇ ғᴇᴀᴛᴜʀᴇs]

➲  ɪ ᴄᴀɴ ʀᴇꜱᴛʀɪᴄᴛ ᴜꜱᴇʀꜱ.
➲  ɪ ʜᴀᴠᴇ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀᴜᴛᴏ-ғɪʟᴛᴇʀ ꜱʏꜱᴛᴇᴍ.
➲  ɪ ᴄᴀɴ ɢʀᴇᴇᴛ ᴜꜱᴇʀꜱ ᴡɪᴛʜ ᴄᴜꜱᴛᴏᴍɪᴢᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇꜱꜱᴀɢᴇꜱ.
➲  ɪ ᴄᴀɴ ʙᴀɴ, ᴍᴜᴛᴇ, ᴋɪᴄᴋ, ᴇᴛᴄ.
➲  ɪ ʜᴀᴠᴇ ᴍᴀɴʏ ᴍᴏᴅᴜʟᴇs ʟɪᴋᴇ ғɪʟᴇ sᴛᴏʀᴇ, ғᴏɴᴛ, ᴋᴀɴɢ, ᴀɪ ɪᴍᴀɢᴇ ᴀɴᴅ ᴍᴏʀᴇ.

➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ ᴍᴇ.</b>"""

    SUBSCRIPTION_TXT = """
<b>ʀᴇғᴇʀʀᴇ ʏᴏᴜʀ ʟɪɴᴋ ᴛᴏ ʏᴏᴜʀ ғʀɪᴇɴᴅs, ғᴀᴍɪʟʏ, ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ɢʀᴏᴜᴘ ᴛᴏ ɢᴇᴛ ғʀᴇᴇ ᴘʀᴇᴍɪᴜᴍ ғᴏʀ {}

ʀᴇғᴇʀᴀʟ ʟɪɴᴋ - https://telegram.me/{}?start=Lucy-{}

ɪғ {} ᴜɴɪǫᴜᴇ ᴜsᴇʀ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴡɪᴛʜ ʏᴏᴜʀ ʀᴇғᴇʀᴀʟ ʟɪɴᴋ ᴛʜᴇɴ ʏᴏᴜ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀᴅᴅᴇᴅ ɪɴ ᴘʀᴇᴍɪᴜᴍ ʟɪsᴛ.

ʙᴜʏ ᴘᴀɪᴅ ᴘʟᴀɴ ʙʏ - /plan</b>"""

    SOURCE_TXT = """
<b>ʜᴇʏ,
ᴛʜɪs ɪs ʟᴜᴄʏ,
ᴀɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴀɪ ᴀɴᴅ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ᴍᴏᴅᴜʟᴇs ʙᴏᴛ.

ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ <a href='https://github.com/pyrogram/pyrogram'>ᴩʏʀᴏɢʀᴀᴍ</a> & <a href='https://github.com/python-telegram-bot/python-telegram-bot'>ᴩʏᴛʜᴏɴ-ᴛᴇʟᴇɢʀᴀᴍ-ʙᴏᴛ</a>  
ᴀɴᴅ ᴜsɪɴɢ ᴀɴᴅ <a href='https://cloud.mongodb.com'>ᴍᴏɴɢᴏ</a> ᴀs ᴅᴀᴛᴀʙᴀsᴇ.


» ʜᴇʀᴇ ɪs ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://github.com/codeflix-bots/autofilter'>ɢɪᴛʜᴜʙ</a>


ʟᴜᴄʏ ɪs ʟɪᴄᴇɴsᴇᴅ ᴜɴᴅᴇʀ ᴛʜᴇ <a href='https://github.com/Codeflix-Bots/AutoFilter/blob/Lucy-main/LICENSE'>ᴍɪᴛ ʟɪᴄᴇɴsᴇ</a> .
© 2023 - 2024 | <a href='https://t.me/+DnmZbLjS0iw0YWI1'>sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ</a> , ᴀʟʟ ʀɪɢʜᴛs ʀᴇsᴇʀᴠᴇᴅ.
</b>"""

    MAIN_TXT = """
ʜᴇʀᴇ ɪꜱ ʜᴇʟᴘ ᴍᴇɴᴜ
"""

    SPECIAL_TXT = """
ᴄʜᴇᴄᴋ ʏᴏᴜʀ ғᴀᴠᴏᴜʀɪᴛᴇ ᴍᴏᴅᴜʟᴇ
"""
    
    CHANNELS = """
<b>๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴛᴏ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ɢᴇᴛ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴜs.

ɪғ ʏᴏᴜ ғᴏᴜɴᴅ ᴀɴʏ ʙᴜɢ ɪɴ ˹ʟᴜᴄʏ˼ ᴏʀ ɪғ ʏᴏᴜ ᴡᴀɴɴᴀ ɢɪᴠᴇ ғᴇᴇᴅʙᴀᴄᴋ ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ˼, ᴩʟᴇᴀsᴇ ʀᴇᴩᴏʀᴛ ɪᴛ ᴀᴛ <a href='https://t.me/+DnmZbLjS0iw0YWI1'>sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ</a>.</b>"""

    DONATE = """<b>Aʀᴇ ʏᴏᴜ ɪɴᴛᴇʀᴇsᴛᴇᴅ ɪɴ ʜᴇʟᴘɪɴɢ ᴍʏ ᴄʀᴇᴀᴛᴏʀ ᴡɪᴛʜ ʜɪs ᴇғғᴏʀᴛs ᴛᴏ ᴋᴇᴇᴘ ᴍᴇ ɪɴ ᴀᴄᴛɪᴠᴇ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ? Iғ ʏᴇs, Yᴏᴜ'ʀᴇ ɪɴ ᴛʜᴇ ʀɪɢʜᴛ ᴘʟᴀᴄᴇ. 

Wᴇ ᴇᴍᴘʜᴀsɪsᴇ ᴛʜᴇ ɪᴍᴘᴏʀᴛᴀɴᴄᴇ ᴏғ ɴᴇᴇᴅɪɴɢ ғᴜɴᴅs ᴛᴏ ᴋᴇᴇᴘ ʟᴜᴄʏ ᴜɴᴅᴇʀ ᴀᴄᴛɪᴠᴇ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ. Yᴏᴜʀ ᴅᴏɴᴀᴛɪᴏɴs ɪɴ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ᴏғ ᴍᴏɴᴇʏ ᴛᴏ ʟᴜᴄʏ sᴇʀᴠᴇʀs ᴀɴᴅ ᴏᴛʜᴇʀ ᴜᴛɪʟɪᴛɪᴇs ᴡɪʟʟ ᴀʟʟᴏᴡ ᴜs ᴛᴏ sᴜsᴛᴀɪɴ ᴛʜᴇ ʟɪғᴇsᴘᴀɴ ɪɴ ᴛʜᴇ ʟᴏɴɢ ᴛᴇʀᴍ. Wᴇ ᴡɪʟʟ ᴜsᴇ ᴀʟʟ ᴏғ ᴛʜᴇ ᴅᴏɴᴀᴛɪᴏɴs ᴛᴏ ᴄᴏᴠᴇʀ ғᴜᴛᴜʀᴇ ᴇxᴘᴇɴsᴇs ᴀɴᴅ ᴜᴘɢʀᴀᴅᴇs ᴏғ ᴛʜᴇ sᴇʀᴠᴇʀs ᴄᴏsᴛs. Iғ ʏᴏᴜ'ᴠᴇ ɢᴏᴛ sᴘᴀʀᴇ ᴍᴏɴᴇʏ ᴛᴏ ʜᴇʟᴘ ᴜs ɪɴ ᴛʜɪs ᴇғғᴏʀᴛ, Kɪɴᴅʟʏ ᴅᴏ sᴏ ᴀɴᴅ ʏᴏᴜʀ ᴅᴏɴᴀᴛɪᴏɴs ᴄᴀɴ ᴀʟsᴏ ᴍᴏᴛɪᴠᴀᴛᴇ ᴜs ᴋᴇᴇᴘ ʙʀɪɴɢ ᴏɴ ɴᴇᴡ ғᴇᴀᴛᴜʀᴇs.

Yᴏᴜ ᴄᴀɴ ʜᴇʟᴘ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ ᴡɪᴛʜ ᴅᴏɴᴀᴛɪᴏɴs
Upi : Gautam8292@fam

sᴇɴᴅ ss ʜᴇʀᴇ : @cosmic_freak</b>"""

    SETTINGS_TXT = """
Hᴇʟᴘ : <b>Sᴇᴛᴛɪɴɢꜱ</b>
    
◈ sᴇᴛᴛɪɴɢs ɪs ᴍᴏsᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ғᴇᴀᴛᴜʀᴇ ɪɴ ᴛʜɪs ʙᴏᴛ.
◈ ʏᴏᴜ ᴄᴀɴ ᴇᴀsɪʟʏ ᴄᴜsᴛᴏᴍɪᴢᴇ ᴛʜɪs ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

<b>Nᴏᴛᴇ :</b>
1. ᴏɴʟʏ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs.
2. ɪᴛ ᴡᴏʀᴋs ᴏɴʟʏ ᴡʜᴇɴ ʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /connect - ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ʙᴏᴛ
• /settings - ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ """

    TELEGRAPH_TXT = """ Hᴇʟᴘ : <b>Tᴇʟᴇɢʀᴀᴘʜ</b>

<b>Nᴏᴛᴇ</b>: ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪꜱ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ɢʀᴏᴜᴘꜱ ᴀɴᴅ ᴘᴍꜱ. ᴀʟꜱᴏ ᴄᴀɴ ʙᴇ ᴜꜱᴇ ʙʏ ᴇᴠᴇʀʏᴏɴᴇ.

<b>Cᴏᴍᴍᴀɴᴅs & Usᴀɢᴇ :</b>
• /telegraph - sᴇɴᴅ ᴍᴇ ᴘɪᴄᴛᴜʀᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴜɴᴅᴇʀ 𝟻ᴍʙ"""

    FONT_TXT = """Hᴇʟᴘ : <b>Fᴏɴᴛ</b>

<b>Nᴏᴛᴇ</b>: ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴍᴏᴅᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ꜰᴏɴᴛꜱ ꜱᴛʏʟᴇ, ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴍᴇ ʟɪᴋᴇ ᴛʜɪꜱ ꜰᴏʀᴍᴀᴛ. 

<code>/font Team Netflix</code>"""

    MANUELFILTER_TXT = """Hᴇʟᴘ : <b>Fɪʟᴛᴇʀꜱ</b>
    
◈ ꜰɪʟᴛᴇʀ ɪꜱ ᴀ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ɪ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ɪɴ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ.

<b>Nᴏᴛᴇ :</b>
1. ᴛʜɪꜱ ʙᴏᴛ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /filter - ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ
• /filters - ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ
• /del - ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ
• /delall - ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)"""

    BUTTON_TXT = """Hᴇʟᴘ : <b>Bᴜᴛᴛᴏɴꜱ</b>
    
◈ ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ.

<b>Nᴏᴛᴇ :</b>
𝟷. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ꜱᴇɴᴅ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, ꜱᴏ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴍᴀɴᴅᴀᴛᴏʀʏ.
𝟸. ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
𝟹. ʙᴜᴛᴛᴏɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀꜱᴇᴅ ᴀꜱ ᴍᴀʀᴋᴅᴏᴡɴ ꜰᴏʀᴍᴀᴛ

ᴜʀʟ ʙᴜᴛᴛᴏɴꜱ :
<code>[Button Text](buttonurl:https://t.me/team_netflix)</code>

ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ :
<code>[Button Text](buttonalert:ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀʟᴇʀᴛ ᴍᴇꜱꜱᴀɢᴇ)</code>"""

    AUTOFILTER_TXT = """Hᴇʟᴘ : <b>Aᴜᴛᴏ Fɪʟᴛᴇʀ</b>
    
<b>Nᴏᴛᴇ :</b> Fɪʟᴇ Iɴᴅᴇx
𝟷. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏꜰ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜰ ɪᴛ'ꜱ ᴘʀɪᴠᴀᴛᴇ.
𝟸. ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇꜱ ɴᴏᴛ ᴄᴏɴᴛᴀɪɴꜱ ᴄᴀᴍʀɪᴘꜱ, ᴘᴏʀɴ ᴀɴᴅ ꜰᴀᴋᴇ ꜰɪʟᴇꜱ.
𝟹. ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ ǫᴜᴏᴛᴇꜱ. ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ.

<b>Nᴏᴛᴇ :</b> Aᴜᴛᴏ Fɪʟᴛᴇʀ
𝟷. Aᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
𝟸. Usᴇ /connect ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴛʜᴇ ʙᴏᴛ.
𝟹. Usᴇ /settings ᴏɴ ʙᴏᴛ's ᴘᴍ ᴀɴᴅ ᴛᴜʀɴ ᴏɴ AᴜᴛᴏFɪʟᴛᴇʀ ᴏɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ."""

    
    RULE_TXT = """♦ 𝗚𝗿𝗼𝘂𝗽 𝗥𝘂𝗹𝗲𝘀 ♦

◈ <b>Sᴇᴀʀᴄʜ Mᴏᴠɪᴇ Wɪᴛʜ Cᴏʀʀᴇᴄᴛ Sᴘᴇʟʟɪɴɢ:</b>
• ᴀᴠᴀᴛᴀʀ 𝟸𝟶𝟶𝟿 ✅
• ᴀᴠᴀᴛᴀʀ ʜɪɴᴅɪ ✅
• ᴀᴠᴀᴛᴀʀ ᴍᴏᴠɪᴇ ❌
• ᴀᴠᴀᴛᴀʀ ʜɪɴᴅɪ ᴅᴜʙʙᴇᴅ..❌

◈ <b>Sᴇᴀʀᴄʜ Wᴇʙ Sᴇʀɪᴇs Iɴ ᴛʜɪs Fᴏʀᴍᴀᴛ:</b>
• ᴠɪᴋɪɴɢs S𝟶𝟷 ✅
• ᴠɪᴋɪɴɢs S𝟶𝟷E𝟶𝟷 ✅
• ᴠɪᴋɪɴɢs S𝟶𝟷 ʜɪɴᴅɪ ✅
• ᴠɪᴋɪɴɢs S𝟶𝟷 ʜɪɴᴅɪ ᴅᴜʙʙ... ❌
• ᴠɪᴋɪɴɢs sᴇᴀsᴏɴ 𝟷 ❌
• ᴠɪᴋɪɴɢs ᴡᴇʙ sᴇʀɪᴇs ❌

<b>➙ ᴅᴏɴ'ᴛ ᴅᴏ ᴀɴʏ ꜱᴇʟꜰ ᴘʀᴏᴍᴏᴛɪᴏɴ. 
➙ ᴅᴏɴ'ᴛ ꜱᴇɴᴅ ᴀɴʏ ᴋɪɴᴅ ᴏꜰ ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ, ᴅᴏᴄᴜᴍᴇɴᴛꜱ, ᴜʀʟ, ᴇᴛᴄ...
➙ ᴅᴏɴ'ᴛ ʀᴇǫᴜᴇꜱᴛ ᴀɴʏ ᴛʜɪɴɢꜱ ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴍᴏᴠɪᴇꜱ, ꜱᴇʀɪᴇꜱ, ᴀɴɪᴍᴀᴛɪᴏɴ, ᴄᴀʀᴛᴏᴏɴ, ᴀɴɪᴍᴇ, ᴋ-ᴅʀᴀᴍᴀ ᴍᴀɴʏ ᴍᴏʀᴇ.</b>

🔰 <b>Nᴏᴛᴇ :</b> ᴀʟʟ ᴍᴇꜱꜱᴀɢᴇꜱ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇᴅ ᴀꜰᴛᴇʀ 𝟷𝟶 ᴍɪɴᴜᴛᴇꜱ ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪꜱꜱᴜᴇꜱ."""

    CONNECTION_TXT = """Hᴇʟᴘ : <b>Cᴏɴɴᴇᴄᴛɪᴏɴꜱ</b>
    
◈ ᴜꜱᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ꜰᴏʀ ᴍᴀɴᴀɢɪɴɢ ꜰɪʟᴛᴇʀꜱ 
◈ ɪᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.

<b>Nᴏᴛᴇ :</b>
1. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. ꜱᴇɴᴅ /ᴄᴏɴɴᴇᴄᴛ ꜰᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴘᴍ

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /connect  - ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ
• /disconnect  - ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ
• /connections - ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ"""

    EXTRAMOD_TXT = """Hᴇʟᴘ : <b>Exᴛʀᴀ Mᴏᴅᴜʟᴇs</b>
    
<b>Nᴏᴛᴇ :</b>
ᴛʜᴇꜱᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ꜰᴇᴀᴛᴜʀᴇꜱ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /id - ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.
• /info  - ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.
• /imdb  - ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.
• /search  - ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ."""

    STICKER_TXT = """<b>yᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴍᴏᴅᴜʟᴇ ᴛᴏ ꜰɪɴᴅᴀɴy  ꜱᴛɪᴄᴋᴇʀꜱ ɪᴅ.
• ᴜꜱᴀɢᴇ :ᴛᴏ ɢᴇᴛ ꜱᴛɪᴄᴋᴇʀ
 
 ʜᴏᴡ ᴛᴏ ᴜꜱᴇ
◉ Reply To Any Sticker [/stickerid]

/stickerid 𝐬𝐭𝐢𝐜𝐤𝐞𝐫 𝐢𝐝

</b>"""

    ALL_FILTERS = """
<b>Hᴇʏ {}, Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
    
    GFILTER_TXT = """Hᴇʟᴘ : <b>Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs</b>
    
◈ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.
    
<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /gfilter - Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.
• /gfilters - Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.
• /delg - Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.
• /delallg - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ."""
    
    FILE_STORE_TXT = """Hᴇʟᴘ : <b>Fɪʟᴇ Sᴛᴏʀᴇ</b>
    
◈ Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /batch - ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.
• /link - ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.
• /pbatch - ᴊᴜsᴛ ʟɪᴋᴇ <code>/batch</code>, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.
• /plink - ᴊᴜsᴛ ʟɪᴋᴇ <code>/link</code>, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ."""


    YTTHUMB = """<b>ʏᴛ-ᴛʜᴜᴍʙ

ʜᴇʟᴘs ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ᴛʜᴜᴍʙɴᴀɪʟ


ᴜsᴇ ᴛʜɪs ꜰᴏʀᴍᴀᴛ 👇</b> 

<code>/ytthumb https://youtu.be/BqlMwyABHOE</code>"""

    GITHUB = """<b>ɢɪᴛʜᴜʙ ᴅᴇᴛᴀɪʟs -</b>

ᴡɪᴛʜ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ, ʏᴏᴜ ᴄᴀɴ ꜰɪɴᴅ ᴏᴜᴛ ᴛʜᴇ ꜰᴜʟʟ ᴅᴇᴛᴀɪʟs ᴏꜰ ᴛʜᴇ ɢɪᴛʜᴜʙ ᴀᴄᴄᴏᴜɴᴛ ᴏꜰ ᴀɴʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴏʀ ᴜsᴇʀs ᴡʜᴏ ʜᴀᴠᴇ ᴀᴄᴄᴏᴜɴᴛ

ᴜsᴇ ᴛʜɪs ꜰᴏʀᴍᴀᴛ 👇

❍ /github phoenix-erotixe
❍ /git : to get github id information
"""

    YTTAGS = """<b>ꜰᴏʀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ᴛᴀɢs -

ʏᴏᴜ ᴄᴀɴ ꜰɪɴᴅ ᴏᴜᴛ ᴛʜᴇ ᴛᴀɢs ᴏꜰ ᴀɴʏ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ᴡɪᴛʜ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ

➤  𝐂𝐨𝐦𝐦𝐚𝐧𝐝 :

/yttags - Reply to a YouTube video</b>"""

    VIDEO_TXT ="""<b>ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇ

ʏᴏᴜ ᴄᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ᴠɪᴅᴇᴏ ꜰʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ

➤  ᴄᴏᴍᴍᴀɴᴅs

ᴛʏᴘᴇ /video or /mp4

ᴇxᴀᴍᴘʟᴇ :</b>

<code>/mp4 https://youtu.be/BqlMwyABHOE</code>

<code>/video https://youtu.be/BqlMwyABHOE</code>"""

    REPORT = """<b>ʀᴇᴘᴏʀᴛ 🧑🏻‍✈️  

ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴘs ʏᴏᴜ ᴛᴏ ʀᴇᴘᴏʀᴛ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ᴀ ᴜsᴇʀs ᴛᴏ ᴛʜᴇ ᴀᴅᴍɪɴs ᴏꜰ ᴛʜᴇ ʀᴇsᴘᴇᴄᴛɪᴠᴇ ɢʀᴏᴜᴘ


➤  𝐂𝐨𝐦𝐦𝐚𝐧𝐝 :

/report 𝗈𝗋 @admin - 𝖳𝗈 𝗋𝖾𝗉𝗈𝗋𝗍 𝖺 𝗎𝗌𝖾𝗋 𝗍𝗈 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇𝗌 (𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾).</b>"""

    MIKEY = """
<b>This is Lucy bot 🦚,
A powerful stable and cute telegram Auto filter bot and management bot.</b>"""

    GEN_PASS = """<b>ᴘᴀssᴡᴏʀᴅ ɢᴇɴᴇʀᴀᴛᴏʀ</b>

There Is Nothing To Know More. Send Me The Limit Of Your Password.

- I Will Give The Password Of That Limit.

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝:

• /genpassword or /genpw 20

NOTE:
• Only Digits Are Allowed
• Maximum Allowed Digits Till 84 
  (I Can't Generate Passwords Above The Length 84)
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    OPNAI_TXT = """ᴏᴘᴇɴᴀɪ ɪꜱ ᴀ ᴀɪ ꜱʏꜱᴛᴇᴍ ᴛʜᴀᴛ ᴡɪʟʟ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ꜰɪɴᴅ ᴀɴꜱᴡᴇʀ ᴏꜰ ʏᴏᴜʀ Qᴜᴇꜱᴛɪᴏɴ ᴀɴᴅ ɪᴛ ᴡɪʟʟ ᴏɴʟʏ ᴡᴏʀᴋ ᴏɴ ʙᴏᴛ ᴘᴍ.

ʜᴏᴡ ᴛᴏ ᴜꜱᴇ

/ᴏᴘᴇɴᴀɪ ᴡʜᴀᴛ ɪꜱ ᴀᴘᴘᴇɴᴅ ᴍᴇᴛʜᴏᴅ ɪɴ ᴘʏᴛʜᴏɴ
"""

    KANG = """
𝐂𝐫𝐞𝐚𝐭𝐞 𝐎𝐰𝐧 𝐒𝐭𝐢𝐜𝐤𝐞𝐫 𝐀𝐧𝐝 𝐒𝐭𝐢𝐜𝐤𝐞𝐫 𝐏𝐚𝐜𝐤
𝐒𝐞𝐧𝐝 𝐓𝐨 𝐈𝐦𝐚𝐠𝐞
𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐢𝐦𝐚𝐠𝐞 𝐚𝐧𝐝 𝐬𝐞𝐧𝐝 /𝐤𝐚𝐧𝐠 𝐂𝐨𝐦𝐦𝐚𝐧𝐝
"""

    GROUP_TXT = """
<b>๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴛᴏ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ɢᴇᴛ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴜs.

ɪғ ʏᴏᴜ ғᴏᴜɴᴅ ᴀɴʏ ʙᴜɢ ɪɴ ˹𝐋ᴜᴄʏ˼ ᴏʀ ɪғ ʏᴏᴜ ᴡᴀɴɴᴀ ɢɪᴠᴇ ғᴇᴇᴅʙᴀᴄᴋ ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ˼, ᴩʟᴇᴀsᴇ ʀᴇᴩᴏʀᴛ ɪᴛ ᴀᴛ <a href='https://t.me/+DnmZbLjS0iw0YWI1'>sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ</a>.</b>"""

    PURGE_TXT = """<b>ᴘᴜʀɢᴇ
    
ᴅᴇʟᴇᴛᴇ ᴀ ʟᴏᴛ ᴏꜰ ᴍᴇssᴀɢᴇs ꜰʀᴏᴍ ɢʀᴏᴜᴘs! 
    
 ᴀᴅᴍɪɴ 

◉ /purge :- ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇssᴀɢᴇs ꜰʀᴏᴍ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇssᴀɢᴇ, ᴛᴏ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴍᴇssᴀɢᴇ​</b>"""

    JSON_TXT = """<b>
ᴊsᴏɴ:

ʙᴏᴛ ʀᴇᴛᴜʀɴs ᴊsᴏɴ ꜰᴏʀ ᴀʟʟ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇs ᴡɪᴛʜ /json

ꜰᴇᴀᴛᴜʀᴇs:

ᴍᴇssᴀɢᴇ ᴇᴅɪᴛᴛɪɴɢ ᴊsᴏɴ
ᴘᴍ sᴜᴘᴘᴏʀᴛ
ɢʀᴏᴜᴘ sᴜᴘᴘᴏʀᴛ

ɴᴏᴛᴇ:

ᴇᴠᴇʀʏᴏɴᴇ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ , ɪꜰ sᴘᴀᴍɪɴɢ ʜᴀᴘᴘᴇɴs ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʙᴀɴ ʏᴏᴜ ꜰʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ.​</b>"""

    CARB_TXT = """<b>ʜᴇʟᴩ ꜰᴏʀ ᴄᴀʀʙᴏɴ

ᴄᴀʀʙᴏɴ ɪꜱ ᴀ ꜰᴇᴜᴛᴜʀᴇ ᴛᴏ ᴍᴀᴋᴇ ᴛʜᴇ ɪᴍᴀɢᴇ ᴀꜱ ꜱʜᴏᴡɴ ɪɴ ᴛʜᴇ ᴛᴏᴩ ᴡɪᴛʜ ʏᴏᴜʀ ᴛᴇxᴛꜱ.
ꜰᴏʀ ᴜꜱɪɴɢ ᴛʜᴇ ᴍᴏᴅᴜʟᴇ ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴛʜᴇ ᴛᴇxᴛ ᴀɴᴅ ᴏᴇᴩʟᴀʏ ᴛɪ ɪᴛ ᴡɪᴛʜ  /carbon ᴄᴏᴍᴍᴀɴᴅ ᴛʜᴇ ʙᴏᴛ ᴡɪʟʟ ᴩᴇᴩᴀʏ ᴡɪᴛʜ ᴛʜᴇ ᴄᴀʀʙᴏɴ ɪᴍᴀɢᴇ

</b>"""

    SONG_TXT = """<b>sᴏɴɢ ᴅᴇᴛᴀɪʟs
sᴏɴɢ sᴇᴀʀᴄʜ ᴠɪᴅᴇᴏ ᴀɴᴅ ᴀᴜᴅɪᴏ

ᴇxᴀᴍᴘʟᴇ -
sᴀᴀᴠɴ sᴏɴɢs ᴄᴏᴍᴍᴀɴᴅ
/𝐬𝐬𝐨𝐧𝐠 ᴀʟᴏɴᴇ 
/𝐬𝐯𝐢𝐝𝐞𝐨 ᴀʟᴏɴᴇ

ʏᴛ ᴠɪᴅᴇᴏ ᴄᴏᴍᴍᴀɴᴅ
/𝐲𝐬𝐨𝐧𝐠 ᴀʟᴏɴᴇ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ
/𝐲𝐯𝐢𝐝𝐞𝐨  ᴀʟᴏɴᴇ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ
</b>"""

    ALIVE = """<b>ᴘɪɴɢ ᴅᴇᴛᴀɪʟs -</b>
/𝐀𝐥𝐢𝐯𝐞 𝐁𝐨𝐭 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 𝐓𝐞𝐬𝐭 𝐂𝐨𝐦𝐦𝐚𝐧𝐝

/𝐩𝐢𝐧𝐠 𝐁𝐨𝐭 𝐒𝐩𝐞𝐞𝐝 𝐓𝐞𝐬𝐭
"""

    REPO = """<b>ʀᴇᴘᴏ ᴅᴇᴛᴀɪʟs -</b>

ʏᴏᴜ ᴄᴀɴ ғɪɴᴅ ɢɪᴛʜᴜʙ's ʀᴇᴘᴏ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴘ ᴏғ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.

❍ /repo : search any repo
❍ /allrepo : get all repo
❍ /downloadrepo : download the repo

ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇ ᴄᴏᴍɪɴɢ sᴏᴏɴ."""

    SHORTNER = """<b>ᴜʀʟ sʜᴏʀᴛɴᴇʀ</b>

ᴛʜɪs ᴍᴏᴅᴜʟᴇ ʜᴇʟᴘs ʏᴏᴜ ᴛᴏ sʜᴏʀᴛ ᴀ ᴜʀʟ ᴀɴᴅ Yᴏᴜ ᴄᴀɴ ᴇᴀʀɴ ᴍᴏɴᴇʏ ғʀᴏᴍ ᴛʜɪs ʙᴏᴛ ᴜɴᴛɪʟ ᴛʜɪs ʙᴏᴛ ɪs ᴀʟɪᴠᴇ.

➤ ᴄᴏᴍᴍᴀɴᴅs:

➪ /short - 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌
➪ /shortlinkon - ᴏɴ ꜱʜᴏʀᴛʟɪɴᴋ ꜰᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
➪ /shortlinkoff - ᴏꜰꜰ ꜱʜᴏʀᴛʟɪɴᴋ ꜰᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
➪ /shortlink_info - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ.
➪ /set_shortlink - ᴛᴏ sᴇᴛ ᴀ sʜᴏʀᴛʟɪɴᴋ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ, use ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ
➪ /set_tutorial - ᴛᴏ sᴇᴛ ᴜᴘ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛᴇɴᴇʀ ᴛᴜᴛᴏʀɪᴀʟ, ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ"""

    LYRICS = """<b>ʟʏʀɪᴄs</b>

ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴘ ᴏғ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ʟʏʀɪᴄs ᴏғ sᴏɴɢs.

➤ ᴄᴏᴍᴍᴀɴᴅ:

➪ /lyrics - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ɢᴇᴛ ʟʏʀɪᴄs."""


    RESTRIC_TXT = """➤ 𝐇𝐞𝐥𝐩: Mᴜᴛᴇ 🚫

𝚃𝚑𝚎𝚜𝚎 𝚊𝚛𝚎 𝚝𝚑𝚎 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝚊 𝚐𝚛𝚘𝚞𝚙 𝚊𝚍𝚖𝚒𝚗 𝚌𝚊𝚗 𝚞𝚜𝚎 𝚝𝚘 𝚖𝚊𝚗𝚊𝚐𝚎 𝚝𝚑𝚎𝚒𝚛 𝚐𝚛𝚘𝚞𝚙 𝚖𝚘𝚛𝚎 𝚎𝚏𝚏𝚒𝚌𝚒𝚎𝚗𝚝𝚕𝚢.

➪/ban: 𝖳𝗈 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unban: 𝖳𝗈 𝗎𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tban: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋.
➪/mute: 𝖳𝗈 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unmute: 𝖳𝗈 𝗎𝗇𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tmute: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋.

ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴄᴏᴅᴇғʟɪx ʙᴏᴛs

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tmute 𝗈𝗋 /tban 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗍𝗂𝗆𝖾 𝗅𝗂𝗆𝗂𝗍.

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝖻𝖺𝗇 2𝖽 𝗈𝗋 /𝗍𝗆𝗎𝗍𝖾 2𝖽.
𝖸𝗈𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝗆/𝗁/𝖽. 
 • 𝗆 = 𝗆𝗂𝗇𝗎𝗍𝖾𝗌
 • 𝗁 = 𝗁𝗈𝗎𝗋𝗌
 • 𝖽 = 𝖽𝖺𝗒𝗌"""

    
    CC_TXT = """
<b>HELP: CC Tools

Credit Card stuffs being easy with CC Module!

USAGE:
➢ /sk - Check if stripe key is live or not.
➢ /bin - Check if given bin is valid or not.
➢ /fake - Generate random fake user details.
➢ /gen - Generate random credit cards info.
➢ /cc - Generate random credit cards.

NOTE:
• Lucy should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member.</b>"""

    

    FSUB_TXT = """
<b>Force members to join channel before writing on chat!

USAGE:
➢ /fsub - Get the current status.
➢ /fsub [off] - Disable forcesub in the chat.
➢ /fsub [channel id/ username] - Setup forcesub channel.
➢ /fsub [clear] - Unmute all members who are muted by me.

NOTE:
• Lucy should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member.</b>"""

    DONATION_TXT = """<b>donation</b> 

<b>ᴀʀᴇ ʏᴏᴜ ɪɴᴛᴇʀᴇsᴛᴇᴅ ɪɴ ʜᴇʟᴘɪɴɢ ᴍʏ ᴄʀᴇᴀᴛᴏʀ ᴡɪᴛʜ ʜɪs ᴇғғᴏʀᴛs ᴛᴏ ᴋᴇᴇᴘ ᴍᴇ ɪɴ ᴀᴄᴛɪᴠᴇ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ? Iғ ʏᴇs, Yᴏᴜ'ʀᴇ ɪɴ ᴛʜᴇ ʀɪɢʜᴛ ᴘʟᴀᴄᴇ. 

ᴡᴇ ᴇᴍᴘʜᴀsɪsᴇ ᴛʜᴇ ɪᴍᴘᴏʀᴛᴀɴᴄᴇ ᴏғ ɴᴇᴇᴅɪɴɢ ғᴜɴᴅs ᴛᴏ ᴋᴇᴇᴘ ʟᴜᴄʏ ʙᴏᴛ ᴜɴᴅᴇʀ ᴀᴄᴛɪᴠᴇ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ. ʏᴏᴜʀ ᴅᴏɴᴀᴛɪᴏɴs ɪɴ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ᴏғ ᴍᴏɴᴇʏ ᴛᴏ ʟᴜᴄʏ ʙᴏᴛ sᴇʀᴠᴇʀs ᴀɴᴅ ᴏᴛʜᴇʀ ᴜᴛɪʟɪᴛɪᴇs ᴡɪʟʟ ᴀʟʟᴏᴡ ᴜs ᴛᴏ sᴜsᴛᴀɪɴ ᴛʜᴇ ʟɪғᴇsᴘᴀɴ ɪɴ ᴛʜᴇ ʟᴏɴɢ ᴛᴇʀᴍ. ᴡᴇ ᴡɪʟʟ ᴜsᴇ ᴀʟʟ ᴏғ ᴛʜᴇ ᴅᴏɴᴀᴛɪᴏɴs ᴛᴏ ᴄᴏᴠᴇʀ ғᴜᴛᴜʀᴇ ᴇxᴘᴇɴsᴇs ᴀɴᴅ ᴜᴘɢʀᴀᴅᴇs ᴏғ ᴛʜᴇ sᴇʀᴠᴇʀs ᴄᴏsᴛs. Iғ ʏᴏᴜ'ᴠᴇ ɢᴏᴛ sᴘᴀʀᴇ ᴍᴏɴᴇʏ ᴛᴏ ʜᴇʟᴘ ᴜs ɪɴ ᴛʜɪs ᴇғғᴏʀᴛ, Kɪɴᴅʟʏ ᴅᴏ sᴏ ᴀɴᴅ ʏᴏᴜʀ ᴅᴏɴᴀᴛɪᴏɴs ᴄᴀɴ ᴀʟsᴏ ᴍᴏᴛɪᴠᴀᴛᴇ ᴜs ᴋᴇᴇᴘ ʙʀɪɴɢ ᴏɴ ɴᴇᴡ ғᴇᴀᴛᴜʀᴇs.

Yᴏᴜ ᴄᴀɴ ʜᴇʟᴘ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ ᴡɪᴛʜ ᴅᴏɴᴀᴛɪᴏɴs</b>"""

    
    REPORT_MSG = """ʀᴇᴘᴏʀᴛ ᴛᴏ ᴀᴅᴍɪɴs"""

    

    BG_TXT = """
ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʀᴇᴍᴏᴠᴇʀ ᴛᴏᴏʟ:

Our background remover tool is a powerful and easy-to-use solution for removing backgrounds from images. With just a few clicks, you can quickly and accurately remove the background from any photo, leaving you with a clean and professional-looking image. Whether you're a photographer looking to enhance your images or a graphic designer working on a project, our background remover tool is the perfect solution for all your editing needs. Say goodbye to tedious manual editing and let our tool do the work for you, saving you time and effort. Try it today and see the difference it can make in your images!

ᴇxᴀᴍᴘʟᴇ : /rmbg ʙʏ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ
"""

    
    

    

    


    SPECIAL_TXT = """
ᴄʜᴇᴄᴋ ʏᴏᴜʀ ғᴀᴠᴏᴜʀɪᴛᴇ ᴍᴏᴅᴜʟᴇ
"""

    

    
    STATUS_TXT = """<b>    
‣ ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs ᴏғ ʟᴜᴄʏ :

• ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ : <code>{}</code>
• ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ : <code>{}</code>
• ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘꜱ : <code>{}</code>
• ᴜꜱᴇᴅ ꜱᴛᴏʀᴀɢᴇ : <code>{}</code>
• ꜰʀᴇᴇ ꜱᴛᴏʀᴀɢᴇ : <code>{}</code>
</b>"""

    LOG_TEXT_G = """<b>#ɴᴇᴡ_ɢʀᴏᴜᴩ

◉ ɢʀᴏᴜᴩ: {}(<code>{}</code>)
◉ ᴍᴇᴍʙᴇʀꜱ: {}
◉ ᴀᴅᴅᴇᴅ ʙʏ: {}"""

    LOG_TEXT_P = """<b><u>✅ کاربر جدیدی به ربات پیوست 😍 </u>
🔺 نام کاربر  : <code>{}</code>
🔺 آیدی عددی کاربر : {}
🤖 ربات : @IR_InstagramdlBot</b>"""

    ALRT_TXT = """{},
ᴄʜᴇᴄᴋ  ʏᴏᴜʀ  ᴏᴡɴ  ʀᴇǫᴜᴇ𝗌ᴛ   😤
"""

    OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ, 
ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇǫᴜᴇꜱᴛ ᴀɢᴀɪɴ."""

    CUDNT_FND = """😴 ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɴᴏᴛ ғᴏᴜɴᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ.**\n\n» ᴍᴀʏʙᴇ ᴛᴜɴᴇ ɢᴀʟᴀᴛ ʟɪᴋʜᴀ ʜᴏ, ᴩᴀᴅʜᴀɪ - ʟɪᴋʜᴀɪ ᴛᴏʜ ᴋᴀʀᴛᴀ ɴᴀʜɪ ᴛᴜ !"""

    
    
    
    TOP_ALRT_MSG = """ꜱᴇᴀʀᴄʜɪɴɢ ꜰᴏʀ ǫᴜᴇʀʏ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ..."""

    MELCOW_ENG = """<b>›› ʜᴇʏ {}, ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {} \n\nʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ ꜱᴇᴀʀᴄʜ ʏᴏᴜʀ ꜰᴀᴠᴏᴜʀɪᴛᴇ ᴍᴏᴠɪᴇꜱ ᴏʀ ꜱᴇʀɪᴇꜱ ʙʏ ᴊᴜꜱᴛ ᴛʏᴘɪɴɢ ɪᴛ'ꜱ ɴᴀᴍᴇ\n\n›› ɪꜰ ʏᴏᴜ'ʀᴇ ʜᴀᴠɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʀᴇɢᴀʀᴅɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴏʀ ꜱᴏᴍᴇᴛʜɪɴɢ ᴇʟꜱᴇ ᴛʜᴇɴ ᴍᴇꜱꜱᴀɢᴇ ʜᴇʀᴇ</b>"""

    
    NORSLTS = """ 
#NoResults

Iᴅ : <code>{}</code>
Nᴀᴍᴇ : {}

Mᴇꜱꜱᴀɢᴇ : <b>{}</b>"""
 
   # PLEASE DO NOT REMOVE ANY CREDITS ❤️‍🩹
    
    CAPTION = """
<b>• {file_name}

• ᴘᴏᴡᴇʀᴇᴅ ʙʏ : <a href="https://t.me/codeflix_bots/161">ᴄᴏᴅᴇғʟɪx ʙᴏᴛs</a></b>"""

    IMDB_TEMPLATE_TXT = """
<b>Query: {query}
IMDb Data:

‣ ᴛɪᴛʟᴇ : <a href={url}>{title}</a>
‣ ɢᴇɴʀᴇs : {genres}
‣ ʏᴇᴀʀ : <a href={url}/releaseinfo>{year}</a>
‣ ʀᴀᴛɪɴɢ : <a href={url}/ratings>{rating}</a> / 10 (Based on {votes} user ratings)
‣ ʟᴀɴɢᴜᴀɢᴇ : <code>{languages}</code></a>
‣ ʀᴜɴᴛɪᴍᴇ : {runtime} Minutes</a>

‣ sᴛᴏʀʏ : {plot}

‣ ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ : {message.from_user.mention}</b>"""
    
    RESTART_TXT = """
<b>✅ ربات با موفقیت ران شد. 😍
📅 تاریخ : <code>{}</code>
⏰ زمان : <code>{}</code>
🌐 منطقه زمانی : <code>Asia/Kolkata</code>
🛠️ ورژن کد : <code>v4.4 [ Sᴛᴀʙʟᴇ ]</code></b>
🤖 ربات : @IR_InstagramdlBot</b>"""

    LOGO = """
                _       __ _ _        _           _       
   ___ ___   __| | ___ / _| (_)_  __ | |__   ___ | |_ ___ 
  / __/ _ \ / _` |/ _ \ |_| | \ \/ / | '_ \ / _ \| __/ __|
 | (__ (_) | (_| |  __/  _| | |>  <  | |_) | (_) | |_\__ \
  \___\___/ \__,_|\___|_| |_|_/_/\_\ |_.__/ \___/ \__|___/

"""

    PAGE_TXT = """ᴡʜʏ ᴀʀᴇ ʏᴏᴜ ꜱᴏ ᴄᴜʀɪᴏᴜꜱ ⁉️"""

    PURCHASE_TXT = """ꜱᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ."""

    
    
    
    
    

    DEVELOPER_TXT = """
special Thanks To ❤️ Developer -

-Dev [Owner of this bot ]<a href='https://t.me/sewxiy'>mikey</a>
"""

#- 
