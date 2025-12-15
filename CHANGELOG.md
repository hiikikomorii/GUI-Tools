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









