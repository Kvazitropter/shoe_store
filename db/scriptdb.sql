CREATE TABLE pickup_point(
	id serial PRIMARY KEY NOT NULL,
	postal_code integer NOT NULL,
	city varchar(255) NOT NULL,
	street varchar(255) NOT NULL,
	building integer
);

CREATE TABLE role(
	id serial PRIMARY KEY NOT NULL,
	name varchar(255) NOT NULL
);

CREATE TABLE "user"(
	id serial PRIMARY KEY NOT NULL,
	role_id integer REFERENCES role(id) ON DELETE CASCADE NOT NULL,
	last_name varchar(255) NOT NULL,
	first_name varchar(255) NOT NULL,
	patronymic varchar(255),
	email varchar(255) NOT NULL,
	password varchar(255) NOT NULL
	last_login timestamp NULL,
	is_active boolean DEFAULT true,
	is_staff boolean DEFAULT false,
	is_superuser boolean DEFAULT false;
);

CREATE TABLE category(
	id serial PRIMARY KEY NOT NULL,
	name varchar(255) NOT NULL
);

CREATE TABLE producer(
	id serial PRIMARY KEY NOT NULL,
	name varchar(255) NOT NULL
);

CREATE TABLE provider(
	id serial PRIMARY KEY NOT NULL,
	name varchar(255) NOT NULL
);

CREATE TABLE unit(
	id serial PRIMARY KEY NOT NULL,
	name varchar(255) NOT NULL
);

CREATE TABLE type(
	id serial PRIMARY KEY NOT NULL,
	name varchar(255) NOT NULL
);

CREATE TABLE status(
	id serial PRIMARY KEY NOT NULL,
	name varchar(255) NOT NULL
);

CREATE TABLE product(
	id serial PRIMARY KEY NOT NULL,
	article varchar(255) NOT NULL,
	type_id integer REFERENCES type(id) ON DELETE CASCADE NOT NULL,
	unit_id integer REFERENCES unit(id) ON DELETE CASCADE NOT NULL,
	price decimal(10, 2) NOT NULL,
	provider_id integer references provider(id) ON DELETE CASCADE NOT NULL,
	producer_id integer references producer(id) ON DELETE CASCADE NOT NULL,
	category_id integer references category(id) ON DELETE CASCADE NOT NULL,
	discount decimal(5, 2) NOT NULL,
	stock integer NOT NULL,
	description text NOT NULL,
	photo varchar(255)
);

CREATE TABLE "order"(
	id serial PRIMARY KEY NOT NULL,
	created_at date NOT NULL,
	delivered_at date NOT NULL,
	pickup_point_address varchar(255) NOT NULL,
	user_id integer references "user"(id) ON DELETE CASCADE NOT NULL,
	receipt_code integer NOT NULL,
	status_id integer REFERENCES status(id) ON DELETE CASCADE NOT NULL
);

CREATE TABLE product_in_order(
	id serial PRIMARY KEY NOT NULL,
	order_id integer REFERENCES "order"(id) ON DELETE CASCADE NOT NULL,
	product_id integer REFERENCES product(id) ON DELETE CASCADE NOT NULL,
	amount integer NOT NULL
);

INSERT INTO public.pickup_point VALUES (1, 420151, 'Лесной', 'Вишневая', '32');
INSERT INTO public.pickup_point VALUES (2, 125061, 'Лесной', 'Подгорная', '8');
INSERT INTO public.pickup_point VALUES (3, 630370, 'Лесной', 'Шоссейная', '24');
INSERT INTO public.pickup_point VALUES (4, 400562, 'Лесной', 'Зеленая', '32');
INSERT INTO public.pickup_point VALUES (5, 614510, 'Лесной', 'Маяковского', '47');
INSERT INTO public.pickup_point VALUES (6, 410542, 'Лесной', 'Светлая', '46');
INSERT INTO public.pickup_point VALUES (7, 620839, 'Лесной', 'Цветочная', '8');
INSERT INTO public.pickup_point VALUES (8, 443890, 'Лесной', 'Коммунистическая', '1');
INSERT INTO public.pickup_point VALUES (9, 603379, 'Лесной', 'Спортивная', '46');
INSERT INTO public.pickup_point VALUES (10, 603721, 'Лесной', 'Гоголя', '41');
INSERT INTO public.pickup_point VALUES (11, 410172, 'Лесной', 'Северная', '13');
INSERT INTO public.pickup_point VALUES (12, 614611, 'Лесной', 'Молодежная', '50');
INSERT INTO public.pickup_point VALUES (13, 454311, 'Лесной', 'Новая', '19');
INSERT INTO public.pickup_point VALUES (14, 660007, 'Лесной', 'Октябрьская', '19');
INSERT INTO public.pickup_point VALUES (15, 603036, 'Лесной', 'Садовая', '4');
INSERT INTO public.pickup_point VALUES (16, 394060, 'Лесной', 'Фрунзе', '43');
INSERT INTO public.pickup_point VALUES (17, 410661, 'Лесной', 'Школьная', '50');
INSERT INTO public.pickup_point VALUES (18, 625590, 'Лесной', 'Коммунистическая', '20');
INSERT INTO public.pickup_point VALUES (19, 625683, 'Лесной', '8 марта', NULL);
INSERT INTO public.pickup_point VALUES (20, 450983, 'Лесной', 'Комсомольская', '26');
INSERT INTO public.pickup_point VALUES (21, 394782, 'Лесной', 'Чехова', '3');
INSERT INTO public.pickup_point VALUES (22, 603002, 'Лесной', 'Дзержинского', '28');
INSERT INTO public.pickup_point VALUES (23, 450558, 'Лесной', 'Набережная', '30');
INSERT INTO public.pickup_point VALUES (24, 344288, 'Лесной', 'Чехова', '1');
INSERT INTO public.pickup_point VALUES (25, 614164, 'Лесной', 'Степная', '30');
INSERT INTO public.pickup_point VALUES (26, 394242, 'Лесной', 'Коммунистическая', '43');
INSERT INTO public.pickup_point VALUES (27, 660540, 'Лесной', 'Солнечная', '25');
INSERT INTO public.pickup_point VALUES (28, 125837, 'Лесной', 'Шоссейная', '40');
INSERT INTO public.pickup_point VALUES (29, 125703, 'Лесной', 'Партизанская', '49');
INSERT INTO public.pickup_point VALUES (30, 625283, 'Лесной', 'Победы', '46');
INSERT INTO public.pickup_point VALUES (31, 614753, 'Лесной', 'Полевая', '35');
INSERT INTO public.pickup_point VALUES (32, 426030, 'Лесной', 'Маяковского', '44');
INSERT INTO public.pickup_point VALUES (33, 450375, 'Лесной', 'Клубная', '44');
INSERT INTO public.pickup_point VALUES (34, 625560, 'Лесной', 'Некрасова', '12');
INSERT INTO public.pickup_point VALUES (35, 630201, 'Лесной', 'Комсомольская', '17');
INSERT INTO public.pickup_point VALUES (36, 190949, 'Лесной', 'Мичурина', '26');

INSERT INTO public.role VALUES (1, 'Администратор');
INSERT INTO public.role VALUES (2, 'Менеджер');
INSERT INTO public.role VALUES (3, 'Авторизированный клиент');

INSERT INTO public."user" VALUES (1, 1, 'Никифорова', 'Весения', 'Николаевна', '94d5ous@gmail.com', 'uzWC67');
INSERT INTO public."user" VALUES (2, 1, 'Сазонов', 'Руслан', 'Германович', 'uth4iz@mail.com', '2L6KZG');
INSERT INTO public."user" VALUES (3, 1, 'Одинцов', 'Серафим', 'Артёмович', 'yzls62@outlook.com', 'JlFRCZ');
INSERT INTO public."user" VALUES (4, 2, 'Степанов', 'Михаил', 'Артёмович', '1diph5e@tutanota.com', '8ntwUp');
INSERT INTO public."user" VALUES (5, 2, 'Ворсин', 'Петр', 'Евгеньевич', 'tjde7c@yahoo.com', 'YOyhfR');
INSERT INTO public."user" VALUES (6, 2, 'Старикова', 'Елена', 'Павловна', 'wpmrc3do@tutanota.com', 'RSbvHv');
INSERT INTO public."user" VALUES (7, 3, 'Михайлюк', 'Анна', 'Вячеславовна', '5d4zbu@tutanota.com', 'rwVDh9');
INSERT INTO public."user" VALUES (8, 3, 'Ситдикова', 'Елена', 'Анатольевна', 'ptec8ym@yahoo.com', 'LdNyos');
INSERT INTO public."user" VALUES (9, 3, 'Ворсин', 'Петр', 'Евгеньевич', '1qz4kw@mail.com', 'gynQMT');
INSERT INTO public."user" VALUES (10, 3, 'Старикова', 'Елена', 'Павловна', '4np6se@mail.com', 'AtnDjr');

INSERT INTO public.producer VALUES (1, 'Kari');
INSERT INTO public.producer VALUES (2, 'Marco Tozzi');
INSERT INTO public.producer VALUES (3, 'Рос');
INSERT INTO public.producer VALUES (4, 'Rieker');
INSERT INTO public.producer VALUES (5, 'Alessio Nesca');
INSERT INTO public.producer VALUES (6, 'CROSBY');

INSERT INTO public.provider VALUES (1, 'Kari');
INSERT INTO public.provider VALUES (2, 'Обувь для вас');

INSERT INTO public.status VALUES (1, 'Завершен');
INSERT INTO public.status VALUES (2, 'Новый ');

INSERT INTO public.type VALUES (1, 'Ботинки');
INSERT INTO public.type VALUES (2, 'Туфли');
INSERT INTO public.type VALUES (3, 'Кроссовки');
INSERT INTO public.type VALUES (4, 'Полуботинки');
INSERT INTO public.type VALUES (5, 'Кеды');
INSERT INTO public.type VALUES (6, 'Тапочки');
INSERT INTO public.type VALUES (7, 'Сапоги');

INSERT INTO public.unit VALUES (1, 'шт.');

INSERT INTO public.category VALUES (1, 'Женская обувь');
INSERT INTO public.category VALUES (2, 'Мужская обувь');

INSERT INTO public.product VALUES (1, 'А112Т4', 1, 1, 4990, 1, 1, 1, 3, 6, 'Женские Ботинки демисезонные kari', '1.jpg');
INSERT INTO public.product VALUES (2, 'F635R4', 1, 1, 3244, 2, 2, 1, 2, 13, 'Ботинки Marco Tozzi женские демисезонные, размер 39, цвет бежевый', '2.jpg');
INSERT INTO public.product VALUES (3, 'H782T5', 2, 1, 4499, 1, 1, 2, 4, 5, 'Туфли kari мужские классика MYZ21AW-450A, размер 43, цвет: черный', '3.jpg');
INSERT INTO public.product VALUES (4, 'G783F5', 1, 1, 5900, 1, 3, 2, 2, 8, 'Мужские ботинки Рос-Обувь кожаные с натуральным мехом', '4.jpg');
INSERT INTO public.product VALUES (5, 'J384T6', 1, 1, 3800, 2, 4, 2, 2, 16, 'B3430/14 Полуботинки мужские Rieker', '5.jpg');
INSERT INTO public.product VALUES (6, 'D572U8', 3, 1, 4100, 2, 3, 2, 3, 6, '129615-4 Кроссовки мужские', '6.jpg');
INSERT INTO public.product VALUES (7, 'F572H7', 2, 1, 2700, 1, 2, 1, 2, 14, 'Туфли Marco Tozzi женские летние, размер 39, цвет черный', '7.jpg');
INSERT INTO public.product VALUES (8, 'D329H3', 4, 1, 1890, 2, 5, 1, 4, 4, 'Полуботинки Alessio Nesca женские 3-30797-47, размер 37, цвет: бордовый', '8.jpg');
INSERT INTO public.product VALUES (9, 'B320R5', 2, 1, 4300, 1, 4, 1, 2, 6, 'Туфли Rieker женские демисезонные, размер 41, цвет коричневый', '9.jpg');
INSERT INTO public.product VALUES (10, 'G432E4', 2, 1, 2800, 1, 1, 1, 3, 15, 'Туфли kari женские TR-YR-413017, размер 37, цвет: черный', '10.jpg');
INSERT INTO public.product VALUES (11, 'S213E3', 4, 1, 2156, 2, 6, 2, 3, 6, '407700/01-01 Полуботинки мужские CROSBY', NULL);
INSERT INTO public.product VALUES (12, 'E482R4', 4, 1, 1800, 1, 1, 1, 2, 14, 'Полуботинки kari женские MYZ20S-149, размер 41, цвет: черный', NULL);
INSERT INTO public.product VALUES (13, 'S634B5', 5, 1, 5500, 2, 6, 2, 3, 6, 'Кеды Caprice мужские демисезонные, размер 42, цвет черный', NULL);
INSERT INTO public.product VALUES (14, 'K345R4', 4, 1, 2100, 2, 6, 2, 2, 3, '407700/01-02 Полуботинки мужские CROSBY', NULL);
INSERT INTO public.product VALUES (15, 'O754F4', 2, 1, 5400, 2, 4, 1, 4, 18, 'Туфли женские демисезонные Rieker артикул 55073-68/37', NULL);
INSERT INTO public.product VALUES (16, 'G531F4', 1, 1, 6600, 1, 1, 1, 2, 9, 'Ботинки женские зимние ROMER арт. 893167-01 Черный', NULL);
INSERT INTO public.product VALUES (17, 'J542F5', 6, 1, 500, 1, 1, 2, 3, 12, 'Тапочки мужские Арт.70701-55-67син р.41', NULL);
INSERT INTO public.product VALUES (18, 'B431R5', 1, 1, 2700, 2, 4, 2, 2, 5, 'Мужские кожаные ботинки/мужские ботинки', NULL);
INSERT INTO public.product VALUES (19, 'P764G4', 2, 1, 6800, 1, 6, 1, 3, 15, 'Туфли женские, ARGO, размер 38', NULL);
INSERT INTO public.product VALUES (20, 'C436G5', 1, 1, 10200, 1, 5, 1, 2, 9, 'Ботинки женские, ARGO, размер 40', NULL);
INSERT INTO public.product VALUES (21, 'F427R5', 1, 1, 11800, 2, 4, 1, 4, 11, 'Ботинки на молнии с декоративной пряжкой FRAU', NULL);
INSERT INTO public.product VALUES (22, 'N457T5', 4, 1, 4600, 1, 6, 1, 3, 13, 'Полуботинки Ботинки черные зимние, мех', NULL);
INSERT INTO public.product VALUES (23, 'D364R4', 2, 1, 12400, 1, 1, 1, 2, 5, 'Туфли Luiza Belly женские Kate-lazo черные из натуральной замши', NULL);
INSERT INTO public.product VALUES (24, 'S326R5', 6, 1, 9900, 2, 6, 2, 3, 15, 'Мужские кожаные тапочки Профиль С.Дали ', NULL);
INSERT INTO public.product VALUES (25, 'L754R4', 4, 1, 1700, 1, 1, 1, 2, 7, 'Полуботинки kari женские WB2020SS-26, размер 38, цвет: черный', NULL);
INSERT INTO public.product VALUES (26, 'M542T5', 3, 1, 2800, 2, 4, 2, 5, 3, 'Кроссовки мужские TOFA', NULL);
INSERT INTO public.product VALUES (27, 'D268G5', 2, 1, 4399, 2, 4, 1, 3, 12, 'Туфли Rieker женские демисезонные, размер 36, цвет коричневый', NULL);
INSERT INTO public.product VALUES (28, 'T324F5', 7, 1, 4699, 1, 6, 1, 2, 5, 'Сапоги замша Цвет: синий', NULL);
INSERT INTO public.product VALUES (29, 'K358H6', 6, 1, 599, 1, 4, 2, 3, 2, 'Тапочки мужские син р.41', NULL);
INSERT INTO public.product VALUES (30, 'H535R5', 1, 1, 2300, 2, 4, 1, 2, 7, 'Женские Ботинки демисезонные', NULL);

INSERT INTO public."order" VALUES (1, '2025-02-27', '2025-04-20', '1', 4, 901, 1);
INSERT INTO public."order" VALUES (2, '2022-09-28', '2025-04-21', '11', 1, 902, 1);
INSERT INTO public."order" VALUES (3, '2025-03-21', '2025-04-22', '2', 2, 903, 1);
INSERT INTO public."order" VALUES (4, '2025-02-20', '2025-04-23', '11', 3, 904, 1);
INSERT INTO public."order" VALUES (5, '2025-03-17', '2025-04-24', '2', 4, 905, 1);
INSERT INTO public."order" VALUES (6, '2025-03-01', '2025-04-25', '15', 1, 906, 1);
INSERT INTO public."order" VALUES (7, '2025-02-28', '2025-04-26', '3', 2, 907, 1);
INSERT INTO public."order" VALUES (8, '2025-03-31', '2025-04-27', '19', 3, 908, 2);
INSERT INTO public."order" VALUES (9, '2025-04-02', '2025-04-28', '5', 4, 909, 2);
INSERT INTO public."order" VALUES (10, '2025-04-03', '2025-04-29', '19', 4, 910, 2);

INSERT INTO public.product_in_order VALUES (1, 1, 1, 2);
INSERT INTO public.product_in_order VALUES (2, 2, 3, 1);
INSERT INTO public.product_in_order VALUES (3, 3, 5, 10);
INSERT INTO public.product_in_order VALUES (4, 4, 7, 5);
INSERT INTO public.product_in_order VALUES (5, 5, 1, 2);
INSERT INTO public.product_in_order VALUES (6, 6, 3, 1);
INSERT INTO public.product_in_order VALUES (7, 7, 5, 10);
INSERT INTO public.product_in_order VALUES (8, 8, 7, 5);
INSERT INTO public.product_in_order VALUES (9, 9, 9, 5);
INSERT INTO public.product_in_order VALUES (10, 10, 11, 5);
INSERT INTO public.product_in_order VALUES (11, 1, 2, 2);
INSERT INTO public.product_in_order VALUES (12, 2, 4, 1);
INSERT INTO public.product_in_order VALUES (13, 3, 6, 10);
INSERT INTO public.product_in_order VALUES (14, 4, 8, 4);
INSERT INTO public.product_in_order VALUES (15, 5, 2, 2);
INSERT INTO public.product_in_order VALUES (16, 6, 4, 1);
INSERT INTO public.product_in_order VALUES (17, 7, 6, 10);
INSERT INTO public.product_in_order VALUES (18, 8, 8, 4);
INSERT INTO public.product_in_order VALUES (19, 9, 10, 1);
INSERT INTO public.product_in_order VALUES (20, 10, 12, 5);

SELECT setval('pickup_point_id_seq', (SELECT MAX(id) FROM pickup_point));
SELECT setval('role_id_seq', (SELECT MAX(id) FROM role));
SELECT setval('user_id_seq', (SELECT MAX(id) FROM "user"));
SELECT setval('type_id_seq', (SELECT MAX(id) FROM type));
SELECT setval('unit_id_seq', (SELECT MAX(id) FROM unit));
SELECT setval('producer_id_seq', (SELECT MAX(id) FROM producer));
SELECT setval('provider_id_seq', (SELECT MAX(id) FROM provider));
SELECT setval('category_id_seq', (SELECT MAX(id) FROM category));
SELECT setval('status_id_seq', (SELECT MAX(id) FROM status));
SELECT setval('product_id_seq', (SELECT MAX(id) FROM product));
SELECT setval('order_id_seq', (SELECT MAX(id) FROM "order"));
SELECT setval('product_in_order_id_seq', (SELECT MAX(id) FROM product_in_order));