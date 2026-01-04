## 04.01.2026
* **в модули, которые находятся в разделе /files/, добавлен отдельный запуск для примеров / GUI тестов.**

***
## 31.12.2025
**Последнее обновление в этом году**  
**С новым годом!**

1. **добавлена кнопка, которая очищает `` __pycache__``  и ``.pyc`` файлы всех директориях, начиная от корня HidlowGUI.**

2. **добавлены ряд пинг-функций в debug (debugconsole), которые проверяют faker, qrcode, monitoring и ctypes утилиты из none_textbox_utils.py и main_api_utils.py.**

3. **замена цвета логов в HidlowToolsGUI и в других модулях, + добавлены доп. логи**

4. **убраны лишние переменные в faker_func**

5. **Оптимизирована Debugсonsole (17mb ram)**

6. **В main_api_func в API в entry-вводом если api выдает ошибку, он перехватывает ответ и выводит в textbox, вместо того, чтобы спамить "не найдено".
Также пофикшены мелкие баги, связанные с CTkTextBox.**

7. **В Info удалено "about console" > лишнее место занимает, сами команды в подробности расписаны в debugconsole**

8. **В about project в разделе с "Версия" теперь ссылка на официальный CHANGELOG**

9. **обновлена команда 'help' в debugconsole. теперь команды разделены на определенные темы: console color, system & info, ping utils**

***
# Backend refactoring 27.12.2025
* **Все функции теперь в отдельных модулях**
* **Оптимизация скрипта до 21% ram**
* **Улучшена архитектура в main**
* **Переписана функция go_back()**
```python
def go_back(hide_frame):
    hide_frame.pack_forget()
    for widget in root.winfo_children():
        if isinstance(widget, ctk.CTkLabel):
            widget.pack_forget()
    menu_frame.pack(pady=20)
    menu_frame2.pack(pady=20)
```
* **В каждом файле пофикшены ошибки/баги**

***
## 21.12.20225
* **полностью переписан фронтед. Теперь фон сливается и не конфликтует с цветом фреймов, а так же теперь выглядит как системный ctk**
* **скрипт оптимизирован в 2 раза (30мб ram)**
* **убран tk.Text (Наконец-то) и заменен на ctk.CTkTextbox абсолютно везде.**
* **переписана архитектура создания кнопок**
***
## 15.12.2025
* **troll теперь в GUI**

* **подробное описание в help**

* **улучшено ctypes**

* **улучшена функция gpt chc**

* **исправлен баг при котором конфиги Monitoring_Frame и Monitoring_frame_stat не возвращали свой цвет после белого фона.**

* **вырезан psutil.cpu_percent(), и вместо него добавлен script PID**

* **убран импорт модуля pingapi_func в начале**

* **оптимизирован HidlowAPI (Flask) до базовых 60мб ram**

***
## 10.12.2025
**1. Оптимизирована работа GUI (70mb ram) и boottraper (11,8 mb)**

![upd_10.12](assets_upd/ram_70.png)

![upd_10.12](assets_upd/bsod_11.png)

***
## 09.12.2025
**1. оптимизирован debugconsole & pingapi_func | 130mb ram -> 18.5mb ram**

![upd_09.12](assets/console_ram.png)

**2. Удалена синяя тема для лучшей оптимизации**
**3. Обновлена функция ``monitoring`` и теперь совместима с белой темой**

![monitor](assets/monitoring_work.png)

![monitor](assets/monitoring_work_white.png)
***

## 07.12.2025
**1. Функция ``Monitor`` (Alpha-version) - выводит на экран % загруженности ``RAM``, ``CPU`` и ``актуальное время``. Работает по принципу ``диспечера задач``**

![monitoring_work.png](assets/monitoring_work.png)

**2. ``Оптимизация GUI`` - раньше скрипт потреблял до 250mb ram. сейчас скрипт потребляет от 150mb до 200mb**

![ram_optimized.png](assets/ram_optimized.png)
















