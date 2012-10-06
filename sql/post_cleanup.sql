/*
select count(*) from open_product as by_product
union
select count(*) from open_by_model as  by_model
union
select count(*) from open_by_year as by_year;
*/
delete from  open_product WHERE time > current_timestamp();
delete from  open_product WHERE price > 200 or price is Null;
call init_by_model;
call init_by_year;
call cleanup_before_sync;

/*
select count(*) from open_product as by_product
union
select count(*) from open_by_model as  by_model
union
select count(*) from open_by_year as by_year;
*/

call sync_by_model;
call sync_by_year;