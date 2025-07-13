# CSS классы для мобильной адаптации

## Общие мобильные классы

### Контейнеры
```css
.tg-web-app           /* Основной контейнер для Telegram Web App */
.mobile-loading       /* Индикатор загрузки для мобильных */
.keyboard-visible     /* Класс для body когда клавиатура видима */
.touch-active         /* Класс для touch feedback */
```

### Навигация
```css
.mobile-menu-toggle   /* Кнопка открытия мобильного меню */
.sidebar.open         /* Открытый сайдбар на мобильных */
.nav-menu             /* Мобильная навигация в виде сетки */
.nav-link             /* Ссылки навигации (вертикальные на мобильных) */
.nav-icon             /* Иконки навигации (увеличенные на мобильных) */
```

## Таблицы и карточки

### Мобильные таблицы
```css
.mobile-table-cards   /* Контейнер для мобильных карточек */
.mobile-card          /* Основная карточка (замена строки таблицы) */
.mobile-card.swipeable /* Карточка с поддержкой свайпов */
.mobile-card.loading  /* Карточка в состоянии загрузки */
.mobile-card.selected /* Выбранная карточка */
.mobile-card.expanded /* Развёрнутая карточка */
```

### Структура карточки
```css
.mobile-card-header   /* Заголовок карточки */
.mobile-card-id       /* ID элемента в карточке */
.mobile-card-status   /* Статус элемента */
.mobile-card-body     /* Основное содержимое карточки */
.mobile-card-row      /* Строка данных в карточке */
.mobile-card-label    /* Метка поля */
.mobile-card-value    /* Значение поля */
.mobile-card-actions  /* Кнопки действий */
```

### Статусы карточек
```css
.mobile-card-status.status-active   /* Активный статус */
.mobile-card-status.status-inactive /* Неактивный статус */
.mobile-card-status.status-pending  /* Ожидающий статус */
```

### Свайпы и действия
```css
.mobile-card-swipe-actions /* Действия при свайпе */
.mobile-card.swiped        /* Карточка в состоянии свайпа */
.swipe-container          /* Контейнер для свайпов */
.swipe-item               /* Элемент с поддержкой свайпов */
```

### Элементы управления таблицей
```css
.mobile-sort-controls  /* Кнопки сортировки на мобильных */
.mobile-sort-btn       /* Кнопка сортировки */
.mobile-sort-btn.active /* Активная кнопка сортировки */
.mobile-sort-btn.asc   /* Сортировка по возрастанию */
.mobile-sort-btn.desc  /* Сортировка по убыванию */
```

### Массовые действия
```css
.bulk-actions          /* Панель массовых действий */
.bulk-actions.visible  /* Видимая панель массовых действий */
.bulk-actions-count    /* Счётчик выбранных элементов */
.bulk-actions-buttons  /* Кнопки массовых действий */
```

## Формы

### Контейнеры форм
```css
.form-container        /* Контейнер формы */
.form-card            /* Карточка формы */
.form-header          /* Заголовок формы */
.form-title           /* Заглавие формы */
.form-subtitle        /* Подзаголовок формы */
.form-actions         /* Кнопки действий формы */
```

### Поля ввода
```css
.form-group           /* Группа полей */
.form-control         /* Основное поле ввода */
.form-control.is-valid    /* Валидное поле */
.form-control.is-invalid  /* Невалидное поле */
.valid-feedback       /* Сообщение об успешной валидации */
.invalid-feedback     /* Сообщение об ошибке валидации */
```

### Группы ввода
```css
.input-group          /* Группа полей ввода */
.input-group-prepend  /* Префикс группы */
.input-group-append   /* Суффикс группы */
```

### Чекбоксы и радио
```css
.form-check           /* Контейнер чекбокса/радио */
.form-check-input     /* Чекбокс или радио */
.form-check-label     /* Метка чекбокса/радио */
.form-switch          /* Переключатель */
```

### Файлы
```css
.form-file            /* Контейнер файлового поля */
.form-file-input      /* Скрытое файловое поле */
.form-file-label      /* Метка файлового поля */
.form-file-text       /* Текст файлового поля */
.form-file-subtext    /* Подпись файлового поля */
```

### Пошаговые формы
```css
.form-steps           /* Индикатор шагов */
.form-step            /* Отдельный шаг */
.form-step.active     /* Активный шаг */
.form-step.completed  /* Завершённый шаг */
.form-step-number     /* Номер шага */
.form-step-title      /* Название шага */
```

## Модальные окна

### Основные классы
```css
.modal                /* Основное модальное окно */
.modal-dialog         /* Диалог модального окна */
.modal-content        /* Содержимое модального окна */
.modal-header         /* Заголовок модального окна */
.modal-title          /* Заглавие модального окна */
.modal-close          /* Кнопка закрытия */
.modal-body           /* Тело модального окна */
.modal-footer         /* Подвал модального окна */
```

### Типы модальных окон
```css
.modal-alert          /* Модальное окно уведомления */
.modal-confirm        /* Модальное окно подтверждения */
.modal-icon           /* Иконка в модальном окне */
.modal-message        /* Сообщение в модальном окне */
.modal-submessage     /* Подсообщение в модальном окне */
```

### Статусы иконок
```css
.modal-icon.success   /* Иконка успеха */
.modal-icon.warning   /* Иконка предупреждения */
.modal-icon.error     /* Иконка ошибки */
```

## Кнопки

### Основные кнопки
```css
.btn                  /* Базовая кнопка */
.btn-primary          /* Основная кнопка */
.btn-secondary        /* Вторичная кнопка */
.btn-success          /* Кнопка успеха */
.btn-warning          /* Кнопка предупреждения */
.btn-danger           /* Кнопка опасности */
```

### Размеры кнопок
```css
.btn-xs               /* Очень маленькая кнопка */
.btn-sm               /* Маленькая кнопка */
.btn-lg               /* Большая кнопка */
.btn-xl               /* Очень большая кнопка */
```

### Специальные кнопки
```css
.btn-icon             /* Кнопка только с иконкой */
.btn-circle           /* Круглая кнопка */
.btn-fab              /* Floating Action Button */
.btn-gradient-primary /* Кнопка с градиентом */
.btn-loading          /* Кнопка в состоянии загрузки */
```

## Telegram Web App

### Специальные классы
```css
.tg-main-button       /* Главная кнопка Telegram */
.tg-main-button.visible /* Видимая главная кнопка */
.pull-refresh-indicator /* Индикатор обновления */
.pull-refresh-indicator.ready /* Готовый индикатор */
```

## Утилиты

### Текст
```css
.text-center          /* Центрированный текст */
.text-right           /* Текст по правому краю */
.text-muted           /* Приглушённый текст */
.text-primary         /* Основной цвет текста */
.text-success         /* Зелёный цвет текста */
.text-warning         /* Жёлтый цвет текста */
.text-danger          /* Красный цвет текста */
```

### Отступы
```css
.mb-0                 /* Нижний отступ 0 */
.mb-1                 /* Нижний отступ 0.5rem */
.mb-2                 /* Нижний отступ 1rem */
.mb-3                 /* Нижний отступ 1.5rem */
.mb-4                 /* Нижний отступ 2rem */
```

### Flexbox
```css
.flex                 /* display: flex */
.flex-column          /* flex-direction: column */
.justify-center       /* justify-content: center */
.justify-between      /* justify-content: space-between */
.items-center         /* align-items: center */
.gap-1                /* gap: 0.5rem */
.gap-2                /* gap: 1rem */
.gap-3                /* gap: 1.5rem */
```

### Общие
```css
.w-full               /* width: 100% */
.hidden               /* display: none */
.loading              /* Индикатор загрузки */
.fade-in              /* Анимация появления */
.truncate             /* Обрезка текста */
```

## Медиазапросы

### Основные breakpoints
```css
@media (max-width: 768px)  /* Мобильные устройства */
@media (max-width: 480px)  /* Маленькие экраны */
@media (min-width: 769px)  /* Десктоп */
```

### Специальные медиазапросы
```css
@media (hover: none) and (pointer: coarse)  /* Touch устройства */
@media (prefers-color-scheme: dark)         /* Тёмная тема */
@media (prefers-contrast: high)             /* Высокая контрастность */
@media (prefers-reduced-motion: reduce)     /* Уменьшенная анимация */
@media print                                /* Печать */
```

## Переменные CSS

### Цвета
```css
--primary-color       /* Основной цвет */
--success-color       /* Цвет успеха */
--warning-color       /* Цвет предупреждения */
--error-color         /* Цвет ошибки */
--bg-primary          /* Основной фон */
--bg-secondary        /* Вторичный фон */
--text-primary        /* Основной текст */
--text-secondary      /* Вторичный текст */
--text-muted          /* Приглушённый текст */
--border-color        /* Цвет границ */
```

### Размеры
```css
--radius              /* Основное скругление */
--radius-sm           /* Маленькое скругление */
--radius-lg           /* Большое скругление */
--shadow-sm           /* Маленькая тень */
--shadow-md           /* Средняя тень */
--shadow-lg           /* Большая тень */
```

### Telegram Web App
```css
--tg-theme-bg-color           /* Фон Telegram */
--tg-theme-text-color         /* Текст Telegram */
--tg-theme-button-color       /* Кнопка Telegram */
--tg-viewport-height          /* Высота viewport */
--mobile-safe-area-top        /* Верхняя безопасная зона */
--mobile-safe-area-bottom     /* Нижняя безопасная зона */
```

## Примеры использования

### Мобильная карточка
```html
<div class="mobile-card swipeable">
    <div class="mobile-card-header">
        <span class="mobile-card-id">#1001</span>
        <span class="mobile-card-status status-active">Активен</span>
    </div>
    <div class="mobile-card-body">
        <div class="mobile-card-row">
            <span class="mobile-card-label">Имя</span>
            <span class="mobile-card-value">Иван Петров</span>
        </div>
    </div>
    <div class="mobile-card-actions">
        <button class="btn btn-sm btn-primary">Изменить</button>
    </div>
</div>
```

### Мобильная форма
```html
<div class="form-card">
    <div class="form-header">
        <h2 class="form-title">Заголовок</h2>
    </div>
    <div class="form-group">
        <label>Поле</label>
        <input type="text" class="form-control">
    </div>
    <div class="form-actions">
        <button class="btn btn-primary">Сохранить</button>
    </div>
</div>
```

### Модальное окно
```html
<div class="modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h3 class="modal-title">Заголовок</h3>
                <button class="modal-close">×</button>
            </div>
            <div class="modal-body">
                Содержимое
            </div>
            <div class="modal-footer">
                <button class="btn btn-primary">OK</button>
            </div>
        </div>
    </div>
</div>
```