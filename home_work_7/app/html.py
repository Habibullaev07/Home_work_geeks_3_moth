html_for_message = """
<html>
    <head>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f8f8f8;
                color: #333;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 600px;
                margin: 30px auto;
                background-color: #ffffff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                text-align: center;
                margin-bottom: 20px;
            }}
            .header h2 {{
                color: #4CAF50;
                font-size: 24px;
                margin: 0;
            }}
            .message-text {{
                font-size: 16px;
                color: #444;
                line-height: 1.6;
                margin-top: 20px;
                padding: 15px;
                background-color: #f1f1f1;
                border-left: 5px solid #4CAF50;
                border-radius: 6px;
            }}
            .footer {{
                text-align: center;
                font-size: 14px;
                color: #999;
                margin-top: 30px;
            }}
            .footer p {{
                margin: 0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>🌟 Новое сообщение от бота 📩</h2>
            </div>
            <div class="message-text">
                <p><strong>Текст вашего сообщения:</strong></p>
                <p>{message_text}</p>
            </div>
            <div class="footer">
                <p>© 2024 Все права защищены</p>
            </div>
        </div>
    </body>
</html>
"""


html_for_photo = """<html>
                        <head>
                            <style>
                                body {
                                    font-family: Arial, sans-serif;
                                    color: #333;
                                    background-color: #f4f4f9;
                                    padding: 20px;
                                }
                                .content {
                                    background-color: #ffffff;
                                    padding: 20px;
                                    border-radius: 8px;
                                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                                    max-width: 600px;
                                    margin: 0 auto;
                                }
                                h2 {
                                    color: #4CAF50;
                                    text-align: center;
                                }
                                p {
                                    font-size: 16px;
                                    line-height: 1.6;
                                    color: #555;
                                    text-align: center;
                                }
                                .photo {
                                    text-align: center;
                                    margin-top: 20px;
                                }
                            </style>
                        </head>
                        <body>
                            <div class="content">
                                <h2>📸 Фото успешно отправлено</h2>
                                <p>Здравствуйте! Мы получили ваше фото. Благодарим за отправку!</p>
                                <div class="photo">
                                    <p><i>Ваше фото прикреплено ниже:</i></p>
                                </div>
                            </div>
                        </body>
                    </html>"""

html_for_video = """<html>
                        <head>
                            <style>
                                body {
                                    font-family: Arial, sans-serif;
                                    color: #333;
                                    background-color: #f4f4f9;
                                    padding: 20px;
                                }
                                .content {
                                    background-color: #ffffff;
                                    padding: 20px;
                                    border-radius: 8px;
                                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                                    max-width: 600px;
                                    margin: 0 auto;
                                }
                                h2 {
                                    color: #4CAF50;
                                    text-align: center;
                                }
                                p {
                                    font-size: 16px;
                                    line-height: 1.6;
                                    color: #555;
                                    text-align: center;
                                }
                                .video {
                                    text-align: center;
                                    margin-top: 20px;
                                }
                            </style>
                        </head>
                        <body>
                            <div class="content">
                                <h2>🎥 Новое видео успешно отправлено</h2>
                                <p>Здравствуйте! Мы получили ваше видео. Благодарим за отправку!</p>
                                <div class="video">
                                    <p><i>Ваше видео успешно обработано. Мы его получили и скоро его просмотрим!</i></p>
                                </div>
                            </div>
                        </body>
                    </html>"""
                    
                    
html_for_audio = """<html>
                        <head>
                            <style>
                                body {
                                    font-family: Arial, sans-serif;
                                    color: #333;
                                    background-color: #f4f4f9;
                                    padding: 20px;
                                }
                                .content {
                                    background-color: #ffffff;
                                    padding: 20px;
                                    border-radius: 8px;
                                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                                    max-width: 600px;
                                    margin: 0 auto;
                                }
                                h2 {
                                    color: #4CAF50;
                                    text-align: center;
                                }
                                p {
                                    font-size: 16px;
                                    line-height: 1.6;
                                    color: #555;
                                    text-align: center;
                                }
                                .audio {
                                    text-align: center;
                                    margin-top: 20px;
                                }
                            </style>
                        </head>
                        <body>
                            <div class="content">
                                <h2>🎶 Новое аудио успешно отправлено</h2>
                                <p>Здравствуйте! Мы получили ваше аудио. Благодарим за отправку!</p>
                                <div class="audio">
                                    <p><i>Ваше аудио успешно обработано. Мы его получили и скоро прослушаем!</i></p>
                                </div>
                            </div>
                        </body>
                    </html>"""
