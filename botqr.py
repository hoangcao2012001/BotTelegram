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
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sử dụng lệnh theo định dạng: /input <nganhang> <stk> <amount> <name>")
        return

    # Tạo đường dẫn với giá trị nhập vào
    image_url = f"https://img.vietqr.io/image/{nganhang}-{stk}-compact2.jpg?amount={amount}&addInfo=Bank%20luli&accountName={name}"

    # Gửi hình ảnh trực tiếp từ URL
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url)

def main() -> None:
    # Khởi tạo bot với token của bạn
    updater = Updater("6878423204:AAFN5uSwJfo5WXzoNn6BoPqCFF-XdD6Y9MY", use_context=True)

    # Lấy đối tượng dispatcher để đăng ký lệnh
    dp = updater.dispatcher

    # Đăng ký lệnh /input với hàm xử lý tương ứng
    dp.add_handler(CommandHandler("input", input_command))

    # Bắt đầu bot
    updater.start_polling()

    # Dừng bot khi nhận được tín hiệu từ bàn phím
    updater.idle()

if __name__ == '__main__':
    main()
