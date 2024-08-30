INSERT INTO  wp_posts (
    ID, post_author, post_date, post_date_gmt, post_content, post_title, 
    post_excerpt, post_status, comment_status, ping_status, post_password, 
    post_name, to_ping, pinged, post_modified, post_modified_gmt, 
    post_content_filtered, post_parent, guid, menu_order, post_type, 
    post_mime_type, comment_count) 
VALUES (
    99999, 1, NOW(), NOW(), '', 
    'test_coupon', '', 'publish', 'closed', 'closed', '', 'test_coupon', 
    '', '', NOW(), NOW(), '', 0, 
    'http://testsite.local/?post_type=shop_coupon&p=99999', 0, 
    'shop_coupon', '', 0
);

INSERT INTO wp_postmeta ( post_id, meta_key, meta_value)
VALUES (99999, 'coupon_amount', '100');
