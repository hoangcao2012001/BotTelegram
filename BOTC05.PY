from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def input_command(update: Update, context: CallbackContext) -> None:
    try:
        # Lấy giá trị từ lệnh /input
        message_text = context.args

        # Kiểm tra xem có đủ số lượng đối số không
        if len(message_text) < 3:
            raise ValueError()

        # Lấy giá trị từ các đối số
        nganhang, stk, *rest = message_text
        amount = rest[0] if rest else None
        name = " ".join(rest[1:]) if rest[1:] else None

        # Chuyển đổi amount thành số nguyên
        amount = int(amount) if amount else None

    except (ValueError, IndexError):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Chúng tôi đã tiếp nhận thông tin báo cáo.")
        return

    # Tạo đường dẫn với giá trị nhập vào
    image_url ="Chúng tôi đã tiếp nhận thông tin báo cáo.Cảm ơn Bạn"
    # Gửi hình ảnh trực tiếp từ URL
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url)

def main() -> None:
    # Khởi tạo bot với token của bạn
    updater = Updater("6693202029:AAHxSvhP3WSIFIMWlr2YiNa21faTLiVFVsw", use_context=True)

    # Lấy đối tượng dispatcher để đăng ký lệnh
    dp = updater.dispatcher

    # Đăng ký lệnh /input với hàm xử lý tương ứng
    dp.add_handler(CommandHandler("c50", input_command))

    # Bắt đầu bot
    updater.start_polling()

    # Dừng bot khi nhận được tín hiệu từ bàn phím
    updater.idle()

if __name__ == '__main__':
    main()
