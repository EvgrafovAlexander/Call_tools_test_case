select id,
	title,
	text
from article
where id not in (select article_id from comment);
