class script(object):
    START_TXT = """<b>👋 سلام {} |🥰😉\n\n<u>• به ربات ریلز دانلودر خوش آمدید ❤️</u>\n\n• لینک اینستاگرامی موردنظرتان را ارسال کنید.\nتا فایلشو براتون بفرستم. 😊\n\n🖍️ سازنده ربات : <a href='t.me/Farshidband'>FﾑRSみɨの-BﾑŊの</a></b> """

    GSTART_TXT = """<b>ʜᴇʏ {},\n\nɪ ᴀᴍ ᴛʜᴇ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘʀᴇᴍɪᴜᴍ ꜰᴇᴀᴛᴜʀᴇꜱ.\n\nᴍᴀɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/cryxelys">ᴍɪᴋᴇʏ</a></b>"""
    
    HELP_TXT = """<b>ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟʟᴏᴡ ᴛᴏ ɢᴇᴛ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ᴀʙᴏᴜᴛ sᴘᴇᴄɪғɪᴄs ᴄᴏᴍᴍᴀɴᴅ!</b>"""
    
    DONATE = """<b>Aʀᴇ ʏᴏᴜ ɪɴᴛᴇʀᴇsᴛᴇᴅ ɪɴ ʜᴇʟᴘɪɴɢ ᴍʏ ᴄʀᴇᴀᴛᴏʀ ᴡɪᴛʜ ʜɪs ᴇғғᴏʀᴛs ᴛᴏ ᴋᴇᴇᴘ ᴍᴇ ɪɴ ᴀᴄᴛɪᴠᴇ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ? Iғ ʏᴇs, Yᴏᴜ'ʀᴇ ɪɴ ᴛʜᴇ ʀɪɢʜᴛ ᴘʟᴀᴄᴇ. 

Wᴇ ᴇᴍᴘʜᴀsɪsᴇ ᴛʜᴇ ɪᴍᴘᴏʀᴛᴀɴᴄᴇ ᴏғ ɴᴇᴇᴅɪɴɢ ғᴜɴᴅs ᴛᴏ ᴋᴇᴇᴘ ʟᴜᴄʏ ᴜɴᴅᴇʀ ᴀᴄᴛɪᴠᴇ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ. Yᴏᴜʀ ᴅᴏɴᴀᴛɪᴏɴs ɪɴ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ᴏғ ᴍᴏɴᴇʏ ᴛᴏ ʟᴜᴄʏ sᴇʀᴠᴇʀs ᴀɴᴅ ᴏᴛʜᴇʀ ᴜᴛɪʟɪᴛɪᴇs ᴡɪʟʟ ᴀʟʟᴏᴡ ᴜs ᴛᴏ sᴜsᴛᴀɪɴ ᴛʜᴇ ʟɪғᴇsᴘᴀɴ ɪɴ ᴛʜᴇ ʟᴏɴɢ ᴛᴇʀᴍ. Wᴇ ᴡɪʟʟ ᴜsᴇ ᴀʟʟ ᴏғ ᴛʜᴇ ᴅᴏɴᴀᴛɪᴏɴs ᴛᴏ ᴄᴏᴠᴇʀ ғᴜᴛᴜʀᴇ ᴇxᴘᴇɴsᴇs ᴀɴᴅ ᴜᴘɢʀᴀᴅᴇs ᴏғ ᴛʜᴇ sᴇʀᴠᴇʀs ᴄᴏsᴛs. Iғ ʏᴏᴜ'ᴠᴇ ɢᴏᴛ sᴘᴀʀᴇ ᴍᴏɴᴇʏ ᴛᴏ ʜᴇʟᴘ ᴜs ɪɴ ᴛʜɪs ᴇғғᴏʀᴛ, Kɪɴᴅʟʏ ᴅᴏ sᴏ ᴀɴᴅ ʏᴏᴜʀ ᴅᴏɴᴀᴛɪᴏɴs ᴄᴀɴ ᴀʟsᴏ ᴍᴏᴛɪᴠᴀᴛᴇ ᴜs ᴋᴇᴇᴘ ʙʀɪɴɢ ᴏɴ ɴᴇᴡ ғᴇᴀᴛᴜʀᴇs.

Yᴏᴜ ᴄᴀɴ ʜᴇʟᴘ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ ᴡɪᴛʜ ᴅᴏɴᴀᴛɪᴏɴs
Upi : Gautam8292@fam

sᴇɴᴅ ss ʜᴇʀᴇ : @cosmic_freak</b>"""

    GROUP_TXT = """
<b>๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴛᴏ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ɢᴇᴛ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴜs.

ɪғ ʏᴏᴜ ғᴏᴜɴᴅ ᴀɴʏ ʙᴜɢ ɪɴ ˹𝐋ᴜᴄʏ˼ ᴏʀ ɪғ ʏᴏᴜ ᴡᴀɴɴᴀ ɢɪᴠᴇ ғᴇᴇᴅʙᴀᴄᴋ ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ˼, ᴩʟᴇᴀsᴇ ʀᴇᴩᴏʀᴛ ɪᴛ ᴀᴛ <a href='https://t.me/+DnmZbLjS0iw0YWI1'>sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ</a>.</b>"""

    ALIVE = """<b>ᴘɪɴɢ ᴅᴇᴛᴀɪʟs -</b>
/𝐀𝐥𝐢𝐯𝐞 𝐁𝐨𝐭 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 𝐓𝐞𝐬𝐭 𝐂𝐨𝐦𝐦𝐚𝐧𝐝

/𝐩𝐢𝐧𝐠 𝐁𝐨𝐭 𝐒𝐩𝐞𝐞𝐝 𝐓𝐞𝐬𝐭"""

    DONATION_TXT = """<b>donation</b> 

<b>ᴀʀᴇ ʏᴏᴜ ɪɴᴛᴇʀᴇsᴛᴇᴅ ɪɴ ʜᴇʟᴘɪɴɢ ᴍʏ ᴄʀᴇᴀᴛᴏʀ ᴡɪᴛʜ ʜɪs ᴇғғᴏʀᴛs ᴛᴏ ᴋᴇᴇᴘ ᴍᴇ ɪɴ ᴀᴄᴛɪᴠᴇ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ? Iғ ʏᴇs, Yᴏᴜ'ʀᴇ ɪɴ ᴛʜᴇ ʀɪɢʜᴛ ᴘʟᴀᴄᴇ. 

ᴡᴇ ᴇᴍᴘʜᴀsɪsᴇ ᴛʜᴇ ɪᴍᴘᴏʀᴛᴀɴᴄᴇ ᴏғ ɴᴇᴇᴅɪɴɢ ғᴜɴᴅs ᴛᴏ ᴋᴇᴇᴘ ʟᴜᴄʏ ʙᴏᴛ ᴜɴᴅᴇʀ ᴀᴄᴛɪᴠᴇ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ. ʏᴏᴜʀ ᴅᴏɴᴀᴛɪᴏɴs ɪɴ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ᴏғ ᴍᴏɴᴇʏ ᴛᴏ ʟᴜᴄʏ ʙᴏᴛ sᴇʀᴠᴇʀs ᴀɴᴅ ᴏᴛʜᴇʀ ᴜᴛɪʟɪᴛɪᴇs ᴡɪʟʟ ᴀʟʟᴏᴡ ᴜs ᴛᴏ sᴜsᴛᴀɪɴ ᴛʜᴇ ʟɪғᴇsᴘᴀɴ ɪɴ ᴛʜᴇ ʟᴏɴɢ ᴛᴇʀᴍ. ᴡᴇ ᴡɪʟʟ ᴜsᴇ ᴀʟʟ ᴏғ ᴛʜᴇ ᴅᴏɴᴀᴛɪᴏɴs ᴛᴏ ᴄᴏᴠᴇʀ ғᴜᴛᴜʀᴇ ᴇxᴘᴇɴsᴇs ᴀɴᴅ ᴜᴘɢʀᴀᴅᴇs ᴏғ ᴛʜᴇ sᴇʀᴠᴇʀs ᴄᴏsᴛs. Iғ ʏᴏᴜ'ᴠᴇ ɢᴏᴛ sᴘᴀʀᴇ ᴍᴏɴᴇʏ ᴛᴏ ʜᴇʟᴘ ᴜs ɪɴ ᴛʜɪs ᴇғғᴏʀᴛ, Kɪɴᴅʟʏ ᴅᴏ sᴏ ᴀɴᴅ ʏᴏᴜʀ ᴅᴏɴᴀᴛɪᴏɴs ᴄᴀɴ ᴀʟsᴏ ᴍᴏᴛɪᴠᴀᴛᴇ ᴜs ᴋᴇᴇᴘ ʙʀɪɴɢ ᴏɴ ɴᴇᴡ ғᴇᴀᴛᴜʀᴇs.

Yᴏᴜ ᴄᴀɴ ʜᴇʟᴘ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ ᴡɪᴛʜ ᴅᴏɴᴀᴛɪᴏɴs</b>"""

    BG_TXT = """
ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʀᴇᴍᴏᴠᴇʀ ᴛᴏᴏʟ:

Our background remover tool is a powerful and easy-to-use solution for removing backgrounds from images. With just a few clicks, you can quickly and accurately remove the background from any photo, leaving you with a clean and professional-looking image. Whether you're a photographer looking to enhance your images or a graphic designer working on a project, our background remover tool is the perfect solution for all your editing needs. Say goodbye to tedious manual editing and let our tool do the work for you, saving you time and effort. Try it today and see the difference it can make in your images!

ᴇxᴀᴍᴘʟᴇ : /rmbg ʙʏ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ
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
    DEVELOPER_TXT = """
special Thanks To ❤️ Developer -

-Dev [Owner of this bot ]<a href='https://t.me/sewxiy'>mikey</a>
"""

#- 
