from telebot import * 
from telebot.types import * 
from requests import get as GET

app = TeleBot("5924205984:AAE6GT1vffx2l33fpVWBmWYueldJFg_getw")

key = InlineKeyboardMarkup([
[InlineKeyboardButton("تحميل",callback_data="d")],
[InlineKeyboardButton("source",url="xco_de.t.me")]])

key2 = InlineKeyboardMarkup([[
InlineKeyboardButton("source",url="xco_de.t.me")]])

key3 = InlineKeyboardMarkup([[InlineKeyboardButton("تحميل عادي",callback_data='1'),InlineKeyboardButton("تحميل HD ",callback_data='2')],[
InlineKeyboardButton("channel",url="xco_de.t.me")]])

def getvedio(m:Message):
	url = m.text
	app.delete_message(m.chat.id,m.id)
	v = app.send_message(m.chat.id,"جارى البحث انتظر ✨")
	if url.startswith("https://vm.tiktok"):
		main = f"https://tiktokapi.body25.repl.co/get?url={url}"
		req = GET(main).json()["true"]
		app.delete_message(m.chat.id,v.id)
		ph = req["avtar"]
		likes = req["likes-count"]
		com = req["comments-count"]
		sh = req["share-count"]
		date = req["postdate"]
	
		app.send_photo(m.chat.id,photo=ph,caption=f"**Vedio information : **\n\n- likes : `{str(likes)}` like ✅\n- comments : `{str(com)}` comment ✅\n- shares :`{str(sh)}` share ✅\n- post date : `{date}` ✅\n- url : {url}  ",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("تحميل عادي",callback_data="1"),InlineKeyboardButton("تحميل HD ",callback_data="2")],[
InlineKeyboardButton("channel",url="xco_de.t.me")]])
,parse_mode="MARKDOWN")
	else:
		app.reply_to(m,"ارسل رابط فيديو تيك توك.لتحميله !",reply_markup=key2)
	
@app.message_handler(commands=["start"])
def x(m:Message):
	app.reply_to(m,"مرحبا بك في بوت التحميل من تيك توك 💝\nاضغط الزر بالاسقل ✅",
	reply_markup=key)
	
@app.callback_query_handler(func=lambda call:True)
def callback(call:CallbackQuery):
	if call.message:
		if call.data == "d":
			app.delete_message(call.message.chat.id,call.message.id)
			cc = app.send_message(call.message.chat.id,"حسناا ارسل الآن رابط الفيديو لتحميله !",reply_markup=key2)
			app.register_next_step_handler(cc , getvedio)
		elif call.data == "1":
			url = " ".join(call.message.caption.split("url : ")[1:])
			main = f"https://tiktokapi.body25.repl.co/get?url={url}"
			req = GET(main).json()["true"]
			vid = req["normal-download"]
			app.delete_message(call.message.chat.id,call.message.id)
			app.send_chat_action(call.message.chat.id,action="upload_video")
			app.send_video(call.message.chat.id,vid,reply_markup=key2)
		elif call.data == "2":
			url = " ".join(call.message.caption.split("url : ")[1:])
			main = f"https://tiktokapi.body25.repl.co/get?url={url}"
			req = GET(main).json()["true"]
			vid = req["download-url-hd"]
			app.delete_message(call.message.chat.id,call.message.id)
			app.send_chat_action(call.message.chat.id,action="upload_video")
			app.send_video(call.message.chat.id,vid,reply_markup=key2)
app.polling()