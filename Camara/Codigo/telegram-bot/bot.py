from telegram.ext import Updater, CommandHandler


def start(update, context):
    update.message.reply_text(f'¡Hola, {update.effective_user.first_name}! ¿En qué puedo ayudarte?\n\n'
                              f'/start - Mensaje de bienvenida\n'
                              f'/about - Información sobre el bot\n'
                              f'/commandList - Lista de comandos\n')


def about(update, context):
    update.message.reply_text('RPi Cam Bot\n\n'
                              'El bot está programado para enviar al chat información relevante recopilada por el '
                              'módulo de cámara Raspberry Pi V2\n\n'
                              'Funcionalidades:\n'
                              ' - Detección de movimiento\n\n'
                              ' - ...\n\n'
                              'Hardware utilizado:\n'
                              '- Raspberry Pi Zero W\n'
                              '- Módulo de cámara Raspberry i V2 - 8 megapíxeles, 1080p (RPi-CAM-V2)')


def command_list(update, context):
    update.message.reply_text('Comando en desarrollo...')


if __name__ == '__main__':
    updater = Updater(token='TOKEN', use_context=True)  # Use the token given to you by The Botfather
    # (https://core.telegram.org/bots)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('about', about))
    dp.add_handler(CommandHandler('commandList', command_list))

    updater.start_polling()
    updater.idle()

